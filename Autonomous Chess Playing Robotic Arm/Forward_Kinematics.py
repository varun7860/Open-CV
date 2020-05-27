from numpy import*
import math
import numpy as np

#######Link Lengths in cm #########
l1 = 4.5
l2 = 10.5
l3 = 15.0
################End################

##########Angles in Floating Point############
theta_1 = 0.0
theta_2 = 90.0
theta_3 = 90.0

alpha_1 = 90.0
alpha_2 = 0.0
alpha_3 = 0.0

######################End#####################

######Convert it to Radians####
theta_1 = (theta_1/180.0)*np.pi
theta_2 = (theta_2/180.0)*np.pi
theta_3 = (theta_3/180.0)*np.pi

alpha_1 = (alpha_1/180.0)*np.pi
alpha_2 = (alpha_2/180.0)*np.pi
alpha_3 = (alpha_3/180.0)*np.pi

############End################

############DH Paramters############

####Create a DH Parameter Table######

p=[[theta_1,alpha_1,0,l1],
   [theta_2,alpha_2,l2,0],
   [-theta_3,alpha_3,l3,0]]

################End##################

###############################Transformation Matrices############################################
i=0                                                                                         
T0_1 = [[np.cos(p[i][0]), -np.sin(p[i][0])*np.cos(p[i][1]),np.sin(p[i][0])*np.sin(p[i][1]),p[i][2]*np.cos(p[i][0])],
        [np.sin(p[i][0]), np.cos(p[i][0])*np.cos(p[i][1]),-np.cos(p[i][0])*np.sin(p[i][1]),p[i][2]*np.sin(p[i][0])],
        [0, np.sin(p[i][1]), np.cos(p[i][1]), p[i][3]],
        [0,0,0,1]]

j= 1
T0_2 = [[np.cos(p[j][0]), -np.sin(p[j][0])*np.cos(p[j][1]),np.sin(p[j][0])*np.sin(p[j][1]),p[j][2]*np.cos(p[j][0])],
        [np.sin(p[j][0]),  np.cos(p[j][0])*np.cos(p[j][1]),-np.cos(p[j][0])*np.sin(p[j][1]),p[j][2]*np.sin(p[j][0])],
        [0, np.sin(p[j][1]), np.cos(p[j][1]), p[j][3]],
        [0,0,0,1]]

k=2
T0_3 = [[np.cos(p[k][0]), -np.sin(p[k][0])*np.cos(p[k][1]),np.sin(p[k][0])*np.sin(p[k][1]),p[k][2]*np.cos(p[k][0])],
        [np.sin(p[k][0]), np.cos(p[k][0])*np.cos(p[k][1]),-np.cos(p[k][0])*np.sin(p[k][1]),p[k][2]*np.sin(p[k][0])],
        [0, np.sin(p[k][1]), np.cos(p[k][1]), p[k][3]],
        [0,0,0,1]]


print("T0_1 =  ")
print(matrix(T0_1))
print("T0_2 =  ")
print(matrix(T0_2))
print("T0_3 = ")
print(matrix(T0_3))
##########################################End####################################################     

###############Final Transformation Matrix#################

H0_1 = dot(T0_1,T0_2)

H0_2 = dot(H0_1,T0_3)


print("H0_2 =  ")
print(matrix(H0_2))
print("                              ")

print("x,y,z cordinates of end effector:",(H0_2[0][3],H0_2[1][3],H0_2[2][3]))

#############################End##########################
