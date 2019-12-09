from skimage.measure import compare_ssim
import cv2
import numpy as np


def measureSimilarities(before, after):

    print(before)
    print(after)

    """
    img_temp = cv2.imread(img2)

    scale_percent = 60  # percent of original size
    width = int(img_temp.shape[1] * scale_percent / 100)
    height = int(img_temp.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    img2 = cv2.resize(img_temp, dim, interpolation=cv2.INTER_AREA)
    

    try:
        before = cv2.imread(img1)
    except:
        before = img1
    try:
        after = cv2.imread(img2)
    except:
        after = img2
    """


    if before.shape[1] != after.shape[1] or before.shape[0] != after.shape[0]:
        width = before.shape[1]
        height = before.shape[0]
        dim = (width, height)
        after = cv2.resize(after, dim, interpolation=cv2.INTER_AREA)


    #before_gray = cv2.cvtColor(before, cv2.COLOR_BGR2GRAY) #changing color to gray to measure differences better (cv2.threshold)
    #after_gray = cv2.cvtColor(after, cv2.COLOR_BGR2GRAY)


    (score, diff) = compare_ssim(before, after, full=True) #comparing images with skimage function (Structural Similarity Index (SSIM) -> degregation of the image)

    diff = (diff * 255).astype("uint8") #diff contains the differences of the image


    thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1] #finding the differences
    contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #contours, CHAIN_APPROX_SIMPLE does need less memory
    contours = contours[0] if len(contours) == 2 else contours[1]

    edged = cv2.Canny(before, 30, 200)
    contoursImg, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    mask = np.zeros(before.shape, dtype='uint8')
    filled_after = after.copy()

    for c in contours:# drawing the contours around the differences
        for cI in contoursImg:
            area = cv2.contourArea(c)
            contourImg = cv2.contourArea(cI)
            if area == contourImg:
                return "Both images have no significant similarities!"
            else:
                for c in contours: #drawing the contours around the differences
                    area = cv2.contourArea(c)
                    if area > 40:
                        x, y, w, h = cv2.boundingRect(c)
                        cv2.rectangle(before, (x, y), (x + w, y + h), (36, 255, 12), 2)
                        cv2.rectangle(after, (x, y), (x + w, y + h), (36, 255, 12), 2)
                        cv2.drawContours(mask, [c], 0, (0, 255, 0), -1)
                        cv2.drawContours(filled_after, [c], 0, (0, 255, 0), -1)
    # before & after
    return str(score)


