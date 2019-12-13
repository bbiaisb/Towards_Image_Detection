import cv2 as cv
import os

def faces(name):
    """Give the cordinates of all faces on an immage.
    
    Arguments: 
        name(str): name of the to be processed image
    
    Returns:
        list: list of the lists of cordinates [x_start,y_start,width,hight] 
            of each detected face
    """
    face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv.imread(name,2)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    return faces

def suffix(name):
    """Cut off the type suffix of a document name.
    
    Arguments: 
        name(str): Str of the to be processed document name
    
    Returns:
        str: name without type suffix
    """
    dot = name.find(".")
    end = name[dot:]
    s_name = name.replace(end,"")
    return s_name

def save_img(name,img):
    """Ask user to decide which and how displayed images should be saved.
    
    Displays an immage and prints the question to the user how he/she 
    want's that save immage. User can respond by pressing different keys and 
    thus save the image in different ways or discard it.
    
    Arguments: 
        name(str): Str of the to be processed image
        img(numpy.ndarray): to be processed image
    
    Returns:
        int: Int of 1, if face has been detected or user wants to discard image
            Int of 0 if face hasn't been detected or user wants to skip to next image
    """
    cv.imshow('Is Big Brother watching you?', img)
    print('\nTo save image press "y" (yes) or "n" (no) depending on whether BB \
          sees you or not.\nPress "Esc" to skip to next image.\nPress any other button to discard image.')   
    k = cv.waitKey()
    if k == 121:
        cv.imwrite(suffix(name)+"_BB sees you.jpg",img)
        cv.destroyAllWindows()
        return 1
    elif k == 110:
        cv.imwrite(suffix(name)+"_save from BB.jpg",img)
        cv.destroyAllWindows()
        return 0
    elif k == 27:
        cv.destroyAllWindows()
        return 0
    else:
        cv.destroyAllWindows()
        return 1
    

def face_detection(name):
    """Draw rectangle around all detected images.
    
    Arguments: 
        name(str): Name of the to be processed image 
    
    Returns:
        int: Returns output of save_img function:
            Int of 1, if face has been detected or user wants to discard image
            Int of 0 if face hasn't been detected or user wants to skip to next image
    """
    img = cv.imread(name)
    for (x, y, w, h) in faces(name):
        cv.rectangle(img, (x, y), (x + w, y + h), (0,0,255), 2)
        
    res=save_img(name,img)
    return res



def face_protect(name,count,find="auto",mean="blur"):
    """Modify faces in such ways, that they can't be recognized.
    
    This function modifies an image containing faces in such ways,
    that the faces can't be recognized by a computer algorithm and saves it. 
    The area to be modified can either be found automatically
    or manually. There are three means to modify the image.
    
    Arguments:
        name(str): name of the image that is to be modified
        count(int): Adds additional size to kernel, 
            (count*15)**2 pixels are added to kernel,
            Kernelsize influences strenght of blur
        
    Keyword arguments:
        find(str): The area to be modified can either be selected automatically("auto") 
            or manually if one gives a Tuple of 4 ints (x_start,y_start,width,hight).
            (defaults to "auto")
        mean(str): Means of protection: blur("blur"), blacken("black"), 
            hide by telling truth("truth"). (defaults to "blur")
    Returns:
        "wrong": if size of selected area to be modified isn't compatible
        1: in all other cases
    """
    img= cv.imread(name)
    for (x, y, w, h) in faces(name):
        if find != "auto":
            (x,y,w,h) = find
        if h > img.shape[0]-100 or w > img.shape[1]-100:
            print("\nh must be smaller than",str(img.shape[0]-100)+". w must be smaller than",str(img.shape[1]-100)+".")
            return "wrong"
        
        if mean == "blur":
            kernel = int(0.55*w)+count*15
            if kernel%2 == 0:
                kernel+=1
            img[y:y+h,x:x+w] = cv.GaussianBlur(img[y:y+h,x:x+w],(kernel, kernel), 0) #101 is too less
        
        elif mean == "black":
            cv.rectangle(img, (x, y), (x + w, y + h), (0,0,0),-1)
        
        elif mean == "truth":
            if h > 1000 or w>1000:
                print("\nw and h must be smaller than 1000")
                return "wrong"

            truth=cv.imread("truth.png")
            img[y:y+h,x:x+w] = truth[0:h,0:w]
        
        if find != "auto":
            break
    
    cv.imwrite(suffix(name)+"_activated protection.jpg",img)
    return 1
    

####################### Main body sample code ################################
    
#change names in "listofimages" to process different images
#change keyword arguments in function "face_protect" to process images differently
    

listofimages=["image21.jpg","image11.jpg","image13.jpg","image17.png","image31.jpg","image32.png"]
for name in listofimages: 
    flag = face_detection(name)
    count = 0
    while flag == 1:
        flag = face_protect(name,count,find="auto",mean="blur")
        if flag == "wrong":
            break
        count += 1
        flag = face_detection(suffix(name)+"_activated protection.jpg")
        
        os.remove(suffix(name)+"_activated protection.jpg")
