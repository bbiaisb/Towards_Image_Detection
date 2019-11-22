from skimage.measure import compare_ssim
import cv2
import numpy as np


def measureSimilarities(img1, img2):
    before = cv2.imread(img1)
    after = cv2.imread(img2)

    before_gray = cv2.cvtColor(before, cv2.COLOR_BGR2GRAY)
    after_gray = cv2.cvtColor(after, cv2.COLOR_BGR2GRAY)

    (score, diff) = compare_ssim(before_gray, after_gray, full=True)
    print("Image similarity", score)

    diff = (diff * 255).astype("uint8")

    thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]

    mask = np.zeros(before.shape, dtype='uint8')
    filled_after = after.copy()

    for c in contours:
        area = cv2.contourArea(c)
        if area > 40:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(before, (x, y), (x + w, y + h), (36, 255, 12), 2)
            cv2.rectangle(after, (x, y), (x + w, y + h), (36, 255, 12), 2)
            cv2.drawContours(mask, [c], 0, (0, 255, 0), -1)
            cv2.drawContours(filled_after, [c], 0, (0, 255, 0), -1)

    cv2.imshow('before', before)
    cv2.imshow('after', after)
    #cv2.imshow('diff', diff)
    #cv2.imshow('mask', mask)
    #cv2.imshow('filled after', filled_after)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("done")


measureSimilarities("test.jpg", "test_edit2.jpg")
