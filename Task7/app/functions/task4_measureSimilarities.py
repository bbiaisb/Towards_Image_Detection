from skimage.metrics import structural_similarity
import cv2


def measure_similarities(before, after):

    if before.shape[1] != after.shape[1] or before.shape[0] != after.shape[0]:
        width = before.shape[1]
        height = before.shape[0]
        dim = (width, height)
        after = cv2.resize(after, dim, interpolation=cv2.INTER_AREA)

    (score, diff) = structural_similarity(before, after, full=True)  # comparing images with skimage function (Structural Similarity Index (SSIM) -> degregation of the image)
    diff = (diff * 255).astype("uint8")
    
    if score >= 0.3:
        perc_score = round(score, 2)*100
        return str(int(perc_score))+"%"
    
    thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]   # finding the differences
    contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)   # contours, CHAIN_APPROX_SIMPLE does need less memory
    contours = contours[0] if len(contours) == 2 else contours[1]

    edged = cv2.Canny(before, 30, 200)
    contoursImg, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:   # drawing the contours around the differences
        for cI in contoursImg:
            area = cv2.contourArea(c)
            contourImg = cv2.contourArea(cI)
            if area == contourImg:
                perc_score = round(score, 2) * 100
                return "Both images have no significant similarities! "+str(int(perc_score)) + "%"
    perc_score = round(score, 2) * 100

    return "There are some minor similarities! " +  str(int(perc_score)) + "%"
