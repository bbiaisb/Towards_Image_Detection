import cv2 as cv
import os

def faces(name):
    face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv.imread(name,2)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    return faces

def suffix(name):
    dot = name.find(".")
    end = name[dot:]
    s_name = name.replace(end,"")
    return s_name

def save_img(name,img):  #folowing part of the code decides which and how images should be saved
    cv.imshow('Is Big Brother watching you?', img)
    print('\nTo save image press "y" (yes) or "n" (no) depending on whether BB \
          sees you or not.\nPress any other button to discard image.')   
    k = cv.waitKey()
    if k == 121:
        cv.imwrite(suffix(name)+"_BB sees you.jpg",img)
        cv.destroyAllWindows()
        flag=1
    elif k == 110:
        cv.imwrite(suffix(name)+"_save from BB.jpg",img)
        cv.destroyAllWindows()
        flag = 0
    else:
        cv.destroyAllWindows()
        flag = 1
        
    return flag
    

def face_detection(name):
    img = cv.imread(name)
    for (x, y, w, h) in faces(name):
        cv.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)
        
    res=save_img(name,img)
    return res



def face_protect(name,find="auto",mean="blur"):
    """Modify faces in such ways, that they can't be recognized.
    
    This fubction modifies an image containing faces in such ways,
    that the faces can't be recognized by a computer algorithm. The modified area can either be 
    selected automatically("auto") or manually("man").
    
    Arguments:
        name(str): name of the image that is to be modified
        
    Keyword arguments:
        find(str): The modified area can either be selected automatically("auto") 
            or manually if one gives a Tuple of 4 ints (x,y,w,h). (defaults to "auto")
        mean(str): Means of protection: blur ("blur"), blacken("black"), 
            hide by blending in("truth"). (defaults to "blur")
        kernel(int): Kernel**2 is kernelsize. Kernel must be given in odd number
            Kernelsize influences strenght of blur. (defaults to 111)
        
    """
    img= cv.imread(name)
    for (x, y, w, h) in faces(name):
        size = "correct"
        if find != "auto":
            (x,y,w,h) = find
        if h > img.shape[0]-100 or w > img.shape[1]-100:
            print("\nh must be smaller than",str(img.shape[0]-100)+". w must be smaller than",str(img.shape[1]-100)+".")
            size = "wrong"
            break
        
        if mean == "blur":
            kernel = int(0.6*w)
            if kernel%2 == 0:
                kernel+=1
            img[y:y+h,x:x+w] = cv.GaussianBlur(img[y:y+h,x:x+w],(kernel, kernel), 0) #101 is too less
        
        elif mean == "black":
            cv.rectangle(img, (x, y), (x + w, y + h), (0,0,0),-1)
        
        elif mean == "truth":
            if h > 1000 or w>1000:
                print("\nw and h must be smaller than 1000")
                size = "wrong"
                break

            truth=cv.imread("truth.png")
            img[y:y+h,x:x+w] = truth[0:h,0:w]
        
        if find != "auto":
            break
    
    if size == "correct":
        cv.imwrite(suffix(name)+"_activated protection.jpg",img)
    return size
    
    
#listofimages=["image13.jpg","image11.jpg","image12.jpg","image21.jpg","image22.png"]
#listofimages = ["image13.jpg",] #"image21.jpg"
#listofimages=["image13.jpg"]
listofimages=["image11.jpg","image13.jpg"]
#listofimages=["image11.jpg","image12.jpg","image15.jpg","image22.png","image31.jpg"]
#listofimages=["image11.jpg","image12.jpg","image21.jpg","image22.png"]


for name in listofimages:

    face_detection(name)   #find=(50,50,300,300),
    flag = face_protect(name,mean="blur")
    if flag == "wrong":
        continue
    face_detection(suffix(name)+"_activated protection.jpg")
    os.remove(suffix(name)+"_activated protection.jpg")
    
    
#    #this code can be used if one wants gradually stronger bluring
    
#    flag = face_detection(name)
#    count = 0
#    while flag == 1 or flag == "correct":
#        flag = face_protect(name,find=(50,50,300,825))
#        if flag == "wrong":
#            break
#        count += 1
#        flag = face_detection(suffix(name)+"_activated protection.jpg")
#    os.remove(suffix(name)+"_activated protection.jpg")
    
    
    import cv2 as cv
import os

def faces(name):
    face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv.imread(name,2)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    return faces

def suffix(name):
    dot = name.find(".")
    end = name[dot:]
    s_name = name.replace(end,"")
    return s_name

def save_img(name,img):  #folowing part of the code decides which and how images should be saved
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
    img = cv.imread(name)
    for (x, y, w, h) in faces(name):
        cv.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)
        
    res=save_img(name,img)
    return res



def face_protect(name,find="auto",mean="blur"):
    """Modify faces in such ways, that they can't be recognized.
    
    This fubction modifies an image containing faces in such ways,
    that the faces can't be recognized by a computer algorithm. The modified area can either be 
    selected automatically("auto") or manually("man").
    
    Arguments:
        name(str): name of the image that is to be modified
        
    Keyword arguments:
        find(str): The modified area can either be selected automatically("auto") 
            or manually if one gives a Tuple of 4 ints (x,y,w,h). (defaults to "auto")
        mean(str): Means of protection: blur ("blur"), blacken("black"), 
            hide by blending in("truth"). (defaults to "blur")
        kernel(int): Kernel**2 is kernelsize. Kernel must be given in odd number
            Kernelsize influences strenght of blur. (defaults to 111)
        
    """
    img= cv.imread(name)
    for (x, y, w, h) in faces(name):
        if find != "auto":
            (x,y,w,h) = find
        if h > img.shape[0]-100 or w > img.shape[1]-100:
            print("\nh must be smaller than",str(img.shape[0]-100)+". w must be smaller than",str(img.shape[1]-100)+".")
            return "wrong"
        
        if mean == "blur":
            kernel = int(0.6*w)
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
    
    
#listofimages=["image13.jpg","image11.jpg","image12.jpg","image21.jpg","image22.png"]
#listofimages = ["image13.jpg",] #"image21.jpg"
#listofimages=["image13.jpg"]
listofimages=["image11.jpg","image13.jpg"]
#listofimages=["image11.jpg","image12.jpg","image15.jpg","image22.png","image31.jpg"]
#listofimages=["image11.jpg","image12.jpg","image21.jpg","image22.png"]


for name in listofimages:
#
#    face_detection(name)   #find=(50,50,300,300),
#    flag = face_protect(name,find=(50,50,300,300),mean="blur")
#    if flag == "wrong":
#        continue
#    face_detection(suffix(name)+"_activated protection.jpg")
#    os.remove(suffix(name)+"_activated protection.jpg")
    
    
#    #this code can be used if one wants gradually stronger bluring
    
    flag = face_detection(name)
    count = 0
    while flag == 1:
        flag = face_protect(name,find=(50,50,300,625))
        if flag == "wrong":
            break
        count += 1
        flag = face_detection(suffix(name)+"_activated protection.jpg")
        
        os.remove(suffix(name)+"_activated protection.jpg")
#        if flag != "wrong":
#            os.remove(suffix(name)+"_activated protection.jpg")