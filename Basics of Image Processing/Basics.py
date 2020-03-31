import cv2
import numpy as np

def main():
   ####################################Read the Images#########################################
   img1 = cv2.imread("C:\\Users\\Administrator\\Desktop\\Image Processing\\misc\\4.1.01.tiff",1)
   img2 = cv2.imread("C:\\Users\\Administrator\\Desktop\\Image Processing\\misc\\4.1.02.tiff",1)
   ############################################End##############################################
 
   #################Arithmatic Operations on Images##################
   add=img1+img2
   subtract1 = img2-img1
   subtract2 = img1-img2
   Multiply = img1*img2
   Division1 = img1/img2
   Division2 = img2/img1
   #############################End###################################

   ##########################Kernels and Filters##########################
   identity_kernel = np.array(([0,0,0],[0,1,0],[0,0,0]),np.float32)
   edge_detection_kernel1 = np.array(([1,0,-1],[0,0,0],[-1,0,1]),np.float32)
   edge_detection_kernel2 = np.array(([-1,-1,-1],[-1,8,-1],[-1,-1,-1]),np.float32)
   edge_detection_kernel3 = np.array(([0,1,0],[1,-4,1],[0,1,0]),np.float32)
   sharpen_kernel = np.array(([0,-1,0],[-1,5,-1],[0,-1,0]),np.float32)
   box_blur_kernel = np.array(([1,1,1],[1,1,1],[1,1,1]),np.float32)/9
   gaussian_blur_kernel = np.array(([1,2,1],[2,4,2],[1,2,1]),np.float32)/16
   unsharp_masking_kernel = np.array(([1,4,6,4,1],[4,16,24,16,4],[6,24,-476,24,6],[4,16,24,16,4],[1,4,6,4,1]),np.float32)/-256

   denoised_image=cv2.medianBlur(img1,3)
   filtered_image = cv2.filter2D(img1,-1,unsharp_masking_kernel)


   ##################################End#################################

   #####################Add Weighted Operation#####################
   alpha=0.5
   beta=0.5
   gamma=0
   output=cv2.addWeighted(img1,alpha,img2,beta,gamma)
   #output=(img1*alpha)+(img2*beta) +gamma

   ########################End####################################

   ######################Splitting and merging#####################
   r1,g1,b1 = cv2.split(img1)
   img1[:,:,2]=0
   img1[:,:,1]=0
   cv2.merge((r1,g1,b1))

   #############################End##################################

   #######################How to Operate VideoCam##################
   cap= cv2.VideoCapture(0)
   if cap.isOpened():
      ret,frame=cap.read()

   else:
      ret=False

   while ret:
      ret,frame=cap.read()

      cv2.imshow('live feed',frame)
      cv2.imshow('image',frame)
      if cv2.waitKey(1)==27:
         #break
   
   cv2.destroyWindow('live feed')
   cap.release()
   
   #############################End################################


   #####################Colorspaces#################################
   RGB = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
   HSV = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
   GRAY = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
   
   #######################End###################################

   ############Display the Image and its Properties##################
   #print(type(img))
   #cv2.imshow('Image Addition',add)
   #cv2.imshow('Image Subtraction1',subtract1)
   #cv2.imshow('Image Subtraction2',subtract2)
   #cv2.imshow('Image Multiplication',Multiply)
   #cv2.imshow('Image Division1',Division1)
   #cv2.imshow('Image Division2',Division2)
   #cv2.imshow('Blending Effect',output)
   #cv2.imshow('R',img1)
   cv2.imshow('Filtered image',filtered_image)
   #cv2.waitKey(0)
   #cv2.destroyWindow('window')
   ############################End#####################################

   
if __name__ =="__main__":
    main()
