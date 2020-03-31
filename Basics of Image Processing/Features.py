import cv2
import glob
import numpy as np

def image_to_feature_vector(image, size=(720,720)):
    return cv2.resize(image, size)


def Harris_Corner_Detection(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray,2,3,0.04)
    dst = cv2.dilate(dst,None)
    image[dst>0.01*dst.max()] = [0,0,255]
    return image

def shi_tomasi_corner_detection(image,corners=100,Quality_Level=0.01,Euclidean_Distance=10):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray,9,81,81)
    corners = cv2.goodFeaturesToTrack(gray,corners,Quality_Level,Euclidean_Distance)
    corners = np.int0(corners)
    array = []
    for i in corners:
        x,y = i.ravel()
        #c = (x,y)
        #c = str(c)
        #array.append(c)
        #cv2.putText(image,c,(x,y),cv2.FONT_HERSHEY_SIMPLEX,  
                   #0.3,(255, 0, 0), 1, cv2.LINE_AA)
        cv2.circle(image,(x,y),4,255,-1)
    #array.sort()
    #print(array) 
    return image

def ChessBoard_Corners(image):
    pattern_size = (10,7)
    res,corners = cv2.findChessboardCorners(image,pattern_size)
    return res
    
def SIFT(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sift = cv2.xfeatures2d.SIFT_create()
    kp = sift.detect(gray_image,None)
    cv2.drawKeypoints(gray_image,kp,image)
    return image

def Erosion(image):
    erosion_kernel = np.ones((5,5),np.uint8)
    erosion = cv2.erode(image, erosion_kernel,iterations = 1)
    return erosion

def Dilation(image):
    dilation_kernel = np.ones((5,5),np.uint8)
    dilation = cv2.dilate(image,dilation_kernel,iterations = 1)
    return dilation

def opening(image):
    opening_kernel = np.ones((5,5),np.uint8)
    opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, opening_kernel)
    return opening

def closing(image):
    closing_kernel = np.ones((5,5),np.uint8)
    closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, closing_kernel)
    return closing

def Morphological_Gradient(image):
    gradient_kernel = np.ones((5,5),np.uint8)
    gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, gradient_kernel)
    return gradient

def contour(image):
    gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gray_image = cv2.bilateralFilter(gray_image,9,95,95)
    ret,thresh = cv2.threshold(gray_image,120,255,cv2.THRESH_BINARY)
    im,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        M = cv2.moments(c)
        if M["m00"]!=0:
          cX = int(M["m10"]/M["m00"])
          cY = int(M["m01"]/M["m00"])
        else:
          cX,cY = 0,0
        y = (cX,cY)
        y = str(y)
        cv2.circle(image, (cX, cY), 5, (0, 255, 0), -1)
        cv2.putText(image, y, (cX , cY),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

    cv2.drawContours(image,contours,-1,(0,255,0),2)
    return image

def canny_edge_detector(image):
    edges = cv2.Canny(image,100,200)
    return edges

def binary_image(image):
    gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    ret,threshold_image = cv2.threshold(gray_image,140,255,cv2.THRESH_BINARY)
    threshold_image2 = cv2.adaptiveThreshold(gray_image,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
    cv2.THRESH_BINARY,11,2)
    return treshold_image2

def background_removal(image):
    mask = np.zeros(image.shape[:2],np.uint8)
    bgd = np.zeros((1,65),np.float64)
    fgd = np.zeros((1,65),np.float64)
    rect = (10,100,1000,1000)
    grabcut = cv2.grabCut(image,mask,rect,bgd,fgd,5,cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    grabcut_image = image*mask2[:,:,np.newaxis]
    return grabcut_image


def adjust_gamma(image,gamma=0.8):
    invGamma = 1.0/gamma
    table = np.array([((i/255.0)**invGamma)*255
      for i in np.arange(0,256)]).astype("uint8")

    return cv2.LUT(image,table)
                      

def polygon_approximation(image):
    gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gray_image = cv2.medianBlur(gray_image,1)
    #ret,thresh = cv2.threshold(gray_image,128,255,0)
    _,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[4]
    for cnt in contours:
       epsilon = 0.03*cv2.arcLength(cnt,True)
       approx = cv2.approxPolyDP(cnt,epsilon,True)
       cv2.drawContours(image, [approx], 0, (0,0,255), 3)
    return image

#cap = cv2.VideoCapture(1)
def main():
  while(True):
      path = " "
      image = cv2.imread(path, 1)
      ret,image = cap.read()
      image = image_to_feature_vector(image)
      cv2.imshow("window", Test_image)
      if cv2.waitKey(1) & 0xFF == ord('q'):
            break

  cap.release()
  cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
    
