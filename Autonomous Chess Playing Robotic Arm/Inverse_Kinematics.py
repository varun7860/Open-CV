from numpy import *
import math

#######Length of links in cm########
l1 = 4.5
l2 = 10.5
l3 = 15.0
###############End##################

######Desired Position of End effector######### 
x = -9.5
y = 12.8
z = 2.0
####################End#######################

###Equations for Inverse kinematics#####
theta_1 = math.atan2(y,x)
r1 = sqrt(pow(x,2)+pow(y,2))
r2 = z-l1
r3 = sqrt(pow(r1,2)+pow(r2,2))
phi_1 = math.acos((pow(l3,2)-pow(l2,2)- pow(r3,2))/(-2*l2*r3))
phi_2 = math.atan2(r2,r1)
phi_3 = math.acos((pow(r3,2)-pow(l2,2)-pow(l3,2))/(-2*l2*l3))
theta_2 =(phi_1 + phi_2)
theta_3 = -(3.14159 - phi_3)
##############End#######################

#######Caliberation of angles obtained####
final_1 = theta_2
final_1 = rad2deg(final_1)
offset_1 = 90-final_1
final_theta_2 =  90 + offset_1    

final_2 = theta_3
final_2 = rad2deg(final_2)
final_theta_3 = final_2 - 51
final_theta_3 = -(final_theta_3)

##################End#####################

##########Print the Results#########
print('theta_1: ', rad2deg(theta_1))
print('theta_2: ', rad2deg(theta_2))
print('theta_3: ', round(rad2deg(theta_3)))

print("Final Value of Theta 2 for your Robot: " ,final_theta_2 )
print("Final Value of Theta 3 for your Robot: " ,final_theta_3 )
##############End###################
