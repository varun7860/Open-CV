import math
import cv2
import numpy as np
from numpy import*
import time
import pyfirmata
import chess
import chess.engine


chessboard_1 = {'12.8':'R1', '15.7':'R2' , '18.3':'R3', '21.0':'R4',
              '23.5':'R5' ,'26.1':'R6','28.9':'R7','31.5':'R8'}
              
chessboard_2 = {'-9.5':'C1','-6.8':'C2','-4.0':'C3','-1.1':'C4',
                '1.4':'C5','4.2':'C6','7.0':'C7','9.8':'C8'}

Square   =     {'R1C1':'h8','R1C2':'g8','R1C3':'f8','R1C4':'e8','R1C5':'d8','R1C6':'c8','R1C7':'b8','R1C8':'a8',
                'R2C1':'h7','R2C2':'g7','R2C3':'f7','R2C4':'e7','R2C5':'d7','R2C6':'c7','R2C7':'b7','R2C8':'a7',
                'R3C1':'h6','R3C2':'g6','R3C3':'f6','R3C4':'e6','R3C5':'d6','R3C6':'c6','R3C7':'b6','R3C8':'a6',
                'R4C1':'h5','R4C2':'g5','R4C3':'f5','R4C4':'e5','R4C5':'d5','R4C6':'c5','R4C7':'b5','R4C8':'a5',
                'R5C1':'h4','R5C2':'g4','R5C3':'f4','R5C4':'e4','R5C5':'d4','R5C6':'c4','R5C7':'b4','R5C8':'a4',
                'R6C1':'h3','R6C2':'g3','R6C3':'f3','R6C4':'e3','R6C5':'d3','R6C6':'c3','R6C7':'b3','R6C8':'a3',
                'R7C1':'h2','R7C2':'g2','R7C3':'f2','R7C4':'e2','R7C5':'d2','R7C6':'c2','R7C7':'b2','R7C8':'a2',
                'R8C1':'h1','R8C2':'g1','R8C3':'f1','R8C4':'e1','R8C5':'d1','R8C6':'c1','R8C7':'b1','R8C8':'a1'}


chessboard_black = {'h8':(12.8,-9.5), 'g8':(12.8,-6.8), 'f8':(12.8,-4.0), 'e8':(12.8,-1.1), 'd8':(12.8,1.4), 'c8':(12.8,4.2), 'b8':(12.8,7.0),'a8':(12.8,9.8),
                    'h7':(15.7,-9.5), 'g7':(15.7,-6.8), 'f7':(15.7,-4.0), 'e7':(15.7,-1.1), 'd7':(15.7,1.4), 'c7':(15.7,4.2), 'b7':(15.7,7.0),'a7':(15.7,9.8),
                    'h6':(18.3,-9.5), 'g6':(18.3,-6.8), 'f6':(18.3,-4.0), 'e6':(18.3,-1.1), 'd6':(18.3,1.4), 'c6':(18.3,4.2), 'b6':(18.3,7.0),'a6':(18.3,9.8),
                    'h5':(21.0,-9.5), 'g5':(21.0,-6.8), 'f5':(21.0,-4.0), 'e5':(21.0,-1.1), 'd5':(21.0,1.4), 'c5':(21.0,4.2), 'b5':(21.0,7.0),'a5':(21.0,9.8),
                    'h4':(23.5,-9.5), 'g4':(23.5,-6.8), 'f4':(23.5,-4.0), 'e4':(23.5,-1.1), 'd4':(23.5,1.4), 'c4':(23.5,4.2), 'b4':(23.5,7.0),'a4':(23.5,9.8),
                    'h3':(26.1,-9.5), 'g3':(26.1,-6.8), 'f3':(26.1,-4.0), 'e3':(26.1,-1.1), 'd3':(26.1,1.4), 'c3':(26.1,4.2), 'b3':(26.1,7.0),'a3':(26.1,9.8),
                    'h2':(28.9,-9.5), 'g2':(28.9,-6.8), 'f2':(28.9,-4.0), 'e2':(28.9,-1.1), 'd2':(28.9,1.4), 'c2':(28.9,4.2), 'b2':(28.9,7.0),'a2':(28.9,9.8),
                    'h1':(31.5,-9.5), 'g1':(31.5,-6.8), 'f1':(31.5,-4.0), 'e1':(31.5,-1.1), 'd1':(31.5,1.4), 'c1':(31.5,4.2), 'b1':(31.5,7.0),'a1':(31.5,9.8)}

chessboard_white = {'a1':(12.8,-9.5), 'b1':(12.8,-6.8), 'c1':(12.8,-4.0), 'd1':(12.8,-1.1), 'e1':(12.8,1.4), 'f1':(12.8,4.2), 'g1':(12.8,7.0),'h1':(12.8,9.8),
                    'a2':(15.7,-9.5), 'b2':(15.7,-6.8), 'c2':(15.7,-4.0), 'd2':(15.7,-1.1), 'e2':(15.7,1.4), 'f2':(15.7,4.2), 'g2':(15.7,7.0),'h2':(15.7,9.8),
                    'a3':(18.3,-9.5), 'b3':(18.3,-6.8), 'c3':(18.3,-4.0), 'd3':(18.3,-1.1), 'e3':(18.3,1.4), 'f3':(18.3,4.2), 'g3':(18.3,7.0),'h3':(18.3,9.8),
                    'a4':(21.0,-9.5), 'b4':(21.0,-6.8), 'c4':(21.0,-4.0), 'd4':(21.0,-1.1), 'e4':(21.0,1.4), 'f4':(21.0,4.2), 'g4':(21.0,7.0),'h4':(21.0,9.8),
                    'a5':(23.5,-9.5), 'b5':(23.5,-6.8), 'c5':(23.5,-4.0), 'd5':(23.5,-1.1), 'e5':(23.5,1.4), 'f5':(23.5,4.2), 'g5':(23.5,7.0),'h5':(23.5,9.8),
                    'a6':(26.1,-9.5), 'b6':(26.1,-6.8), 'c6':(26.1,-4.0), 'd6':(26.1,-1.1), 'e6':(26.1,1.4), 'f6':(26.1,4.2), 'g6':(26.1,7.0),'h6':(26.1,9.8),
                    'a7':(28.9,-9.5), 'b7':(28.9,-6.8), 'c7':(28.9,-4.0), 'd7':(28.9,-1.1), 'e7':(28.9,1.4), 'f7':(28.9,4.2), 'g7':(28.9,7.0),'h7':(28.9,9.8),
                    'a8':(31.5,-9.5), 'b8':(31.5,-6.8), 'c8':(31.5,-4.0), 'd8':(31.5,-1.1), 'e8':(31.5,1.4), 'f8':(31.5,4.2), 'g8':(31.5,7.0),'h8':(31.5,9.8)}

castling_black = []
castling_white = []

destination_squares_black = ['e5', 'c6', 'c5']
present_squares_black   =   ['e7','b8','f8']

destination_squares_white= ['e4', 'f3', 'c4']
present_squares_white   =   ['e2','g1','f1']

sample_1 = []
sample_2 = [0]
game_played = []


N = 0
M = 0
Z = 3.8
f = 0
counter = 0

Gripper_angle_1 = 130
Gripper_angle_2 = 80

motion = False


board = pyfirmata.Arduino('com8')
servo_pin1 = board.get_pin('d:3:s')
servo_pin2 = board.get_pin('d:5:s')
servo_pin3 = board.get_pin('d:6:s')
servo_pin4 = board.get_pin('d:9:s')

initialising_angle_1 = 0
initialising_angle_2 = 0
initialising_angle_3 = 0


while(initialising_angle_1<60):
    servo_pin2.write(initialising_angle_1)
    initialising_angle_1 = initialising_angle_1+1
    time.sleep(0.015)

while(initialising_angle_2<90):
    servo_pin3.write(initialising_angle_2)
    initialising_angle_2 = initialising_angle_2+1
    time.sleep(0.015)

while(initialising_angle_3<80):
    servo_pin4.write(initialising_angle_3)
    initialising_angle_3 = initialising_angle_3+1
    time.sleep(0.015)
    



def Robot_moves_black():
    global N,M,Z,error
    error = 4.5
        
    p1 = present_squares_black [N]
    p2 = destination_squares_black[M]

    T1 = chessboard_black[p1]
    T2 = chessboard_black[p2]
    
    N = N+1
    M = M+1

    if N > len(present_squares_black):
        N = 0
    if M > len(destination_squares_black):
        M = 0

    X1 = T1[1]
    Y1 = T1[0]

    X2 = T2[1]
    Y2 = T2[0]

    print(X1,Y1,X2,Y2)

    Theta_1,Theta_2,Theta_3  = Inverse_Kinematics(X1,Y1,Z)
    Z = 4.2
    Theta_4,Theta_5,Theta_6  = Inverse_Kinematics(X2,Y2,Z)
    Theta_1 = Theta_1 - error
    Theta_2 = Theta_2 + 3.0
    Theta_4 = Theta_4 - error
    Theta_5 = Theta_5 - 9.0
    Theta_6 = Theta_6 + 8.0
    print(Theta_1,Theta_2,Theta_3)
    print(Theta_4,Theta_5,Theta_6)

    
    i = servo_pin1.read()
    j = servo_pin2.read()
    k = servo_pin3.read()
    l = servo_pin4.read()

    if i<Theta_1:
        while(i< Theta_1):
            servo_pin1.write(i)
            i = i+1
            time.sleep(0.02)

    if i>Theta_1:
        while(i>Theta_1):
            servo_pin1.write(i)
            i = i-1
            time.sleep(0.02)


    if j<Theta_2:
        while(j< Theta_2):
            servo_pin2.write(j)
            j = j+1
            time.sleep(0.02)

    if j>Theta_2:
        while(j>Theta_2):
            servo_pin2.write(j)
            j = j-1
            time.sleep(0.02)

    if k<Theta_3:
        while(k< Theta_3):
            servo_pin3.write(k)
            k = k+1
            time.sleep(0.02)

    if k>Theta_3:
        while(k> Theta_3):
            servo_pin3.write(k)
            k = k-1
            time.sleep(0.02)

    if l<Gripper_angle_1:
        while(l< Gripper_angle_1):
            servo_pin4.write(l)
            l = l+1
            time.sleep(0.02)
            
    if l>Gripper_angle_1:
        while(l> Gripper_angle_1):
            servo_pin4.write(l)
            l = l-1
            time.sleep(0.02)

    time.sleep(0.1)
    u = servo_pin2.read()
    correcting_angle = 90
    
    if u<correcting_angle:
       while(u<correcting_angle):
           servo_pin2.write(u)
           u = u+1
           time.sleep(0.02)

    if u>correcting_angle:
       while(u>correcting_angle):
           servo_pin2.write(u)
           u = u-1
           time.sleep(0.02)
    
     
    time.sleep(0.5)
    i = servo_pin1.read()
    j = servo_pin2.read()
    k = servo_pin3.read()
    l = servo_pin4.read()


    if i<Theta_4:
        while(i< Theta_4):
            servo_pin1.write(i)
            i = i+1
            time.sleep(0.02)
            
    if i>Theta_4:
        while(i>Theta_4):
            servo_pin1.write(i)
            i = i-1
            time.sleep(0.02)


    if k<Theta_6:
        while(k< Theta_6):
            servo_pin3.write(k)
            k = k+1
            time.sleep(0.02)

    if k>Theta_6:
        while(k>Theta_6):
            servo_pin3.write(k)
            k = k-1
            time.sleep(0.02)

    if j<Theta_5:
        while(j< Theta_5):
            servo_pin2.write(j)
            j = j+1
            time.sleep(0.02)

    if j>Theta_5:
        while(j> Theta_5):
            servo_pin2.write(j)
            j = j-1
            time.sleep(0.02)

    if l<Gripper_angle_2:
        while(l< Gripper_angle_2):
            servo_pin4.write(l)
            l = l+1
            time.sleep(0.02)
            
    if l>Gripper_angle_2:
        while(l> Gripper_angle_2):
            servo_pin4.write(l)
            l = l-1
            time.sleep(0.02)


    time.sleep(0.5)
    i = servo_pin1.read()
    j = servo_pin2.read()
    k = servo_pin3.read()
    l = servo_pin4.read()

    angle_1 = 0
    angle_2 = 80
    angle_3 = 60

    if j >angle_2:
        while(j>angle_2):
            servo_pin2.write(j)
            j = j-1
            time.sleep(0.01)

    if k >angle_3:
        while(k>angle_3):
            servo_pin3.write(k)
            k = k-1
            time.sleep(0.01)
              
    if i >angle_1:
        while(i>angle_1):
            servo_pin1.write(i)
            i = i-1
            time.sleep(0.01)
    Z = 3.8          

def Robot_moves_white():
    global N,M,motion
    p1 = present_squares_white [N]
    p2 = destination_squares_white[M]

    T1 = chessboard_white[p1]
    T2 = chessboard_white[p2]
    
    if N > len(present_squares_white):
        N = 0
    if M > len(destination_squares_white):
        M = 0
        
    N = N+1
    M = M+1

    X1 = T1[1]
    Y1 = T1[0]

    X2 = T2[1]
    Y2 = T2[0]

    Theta_1,Theta_2,Theta_3  = Inverse_Kinematics(X1,Y1,Z)
    Z = 4.2
    Theta_4,Theta_5,Theta_6  = Inverse_Kinematics(X2,Y2,Z)

    print(Theta_1,Theta_2,Theta_3)
    print(Theta_4,Theta_5,Theta_6)

    
    i = servo_pin1.read()
    j = servo_pin2.read()
    k = servo_pin3.read()
    l = servo_pin4.read()

    if i<Theta_1:
        while(i< Theta_1):
            servo_pin1.write(i)
            i = i+1
            time.sleep(0.02)

    if i>Theta_1:
        while(i>Theta_1):
            servo_pin1.write(i)
            i = i-1
            time.sleep(0.02)


    if j<Theta_2:
        while(j< Theta_2):
            servo_pin2.write(j)
            j = j+1
            time.sleep(0.02)

    if j>Theta_2:
        while(j>Theta_2):
            servo_pin2.write(j)
            j = j-1
            time.sleep(0.02)

    if k<Theta_3:
        while(k< Theta_3):
            servo_pin3.write(k)
            k = k+1
            time.sleep(0.02)

    if k>Theta_3:
        while(k> Theta_3):
            servo_pin3.write(k)
            k = k-1
            time.sleep(0.02)

    if l<Gripper_angle_1:
        while(l< Gripper_angle_1):
            servo_pin4.write(l)
            l = l+1
            time.sleep(0.02)
            
    if l>Gripper_angle_1:
        while(l> Gripper_angle_1):
            servo_pin4.write(l)
            l = l-1
            time.sleep(0.02)

    time.sleep(0.1)
    u = servo_pin2.read()
    correcting_angle = 90
    
    if u<correcting_angle:
       while(u<correcting_angle):
           servo_pin2.write(u)
           u = u+1
           time.sleep(0.02)

    if u>correcting_angle:
       while(u>correcting_angle):
           servo_pin2.write(u)
           u = u-1
           time.sleep(0.02)

    time.sleep(0.5)
    i = servo_pin1.read()
    j = servo_pin2.read()
    k = servo_pin3.read()
    l = servo_pin4.read()


    if i<Theta_4:
        while(i< Theta_4):
            servo_pin1.write(i)
            i = i+1
            time.sleep(0.02)
            
    if i>Theta_4:
        while(i>Theta_4):
            servo_pin1.write(i)
            i = i-1
            time.sleep(0.02)


    if k<Theta_6:
        while(k< Theta_6):
            servo_pin3.write(k)
            k = k+1
            time.sleep(0.02)

    if k>Theta_6:
        while(k>Theta_6):
            servo_pin3.write(k)
            k = k-1
            time.sleep(0.02)

    if j<Theta_5:
        while(j< Theta_5):
            servo_pin2.write(j)
            j = j+1
            time.sleep(0.02)

    if j>Theta_5:
        while(j> Theta_5):
            servo_pin2.write(j)
            j = j-1
            time.sleep(0.02)

    if l<Gripper_angle_2:
        while(l< Gripper_angle_1):
            servo_pin4.write(l)
            l = l+1
            time.sleep(0.02)
            
    if l>Gripper_angle_2:
        while(l> Gripper_angle_1):
            servo_pin4.write(l)
            l = l-1
            time.sleep(0.02)


    time.sleep(0.5)
    i = servo_pin1.read()
    j = servo_pin2.read()
    k = servo_pin3.read()
    l = servo_pin4.read()

    angle_1 = 0
    angle_2 = 70
    angle_3 = 90

    if j >angle_2:
        while(j>angle_2):
            servo_pin2.write(j)
            j = j-1
            time.sleep(0.01)

    if k >angle_3:
        while(k>angle_3):
            servo_pin3.write(k)
            k = k-1
            time.sleep(0.01)
              
    if i >angle_1:
        while(i>angle_1):
            servo_pin1.write(i)
            i = i-1
            time.sleep(0.01)
            
    Z = 4.0

def Inverse_Kinematics(X,Y,Z):

    l1 = 4.5
    l2 = 10.5
    l3 = 15.0

    
    x = X
    y = Y
    z = Z

    theta_1 = math.atan2(y,x)
    theta_1 = rad2deg(theta_1)
    r1 = sqrt(pow(x,2)+pow(y,2))
    r2 = z-l1
    r3 = sqrt(pow(r1,2)+pow(r2,2))
    phi_1 = math.acos((pow(l3,2)-pow(l2,2)- pow(r3,2))/(-2*l2*r3))
    phi_2 = math.atan2(r2,r1)
    phi_3 = math.acos((pow(r3,2)-pow(l2,2)-pow(l3,2))/(-2*l2*l3))
    theta_2 =(phi_1 + phi_2)
    theta_3 = -(3.14159 - phi_3)
    

    final_1 = theta_2
    final_1 = rad2deg(final_1)
    offset_1 = 90-final_1
    final_theta_2 =  90 + offset_1

    final_2 = theta_3
    final_2 = rad2deg(final_2)
    final_theta_3 = final_2 - 51
    final_theta_3 = -(final_theta_3)


    print("Final Value of Theta 1 for your Robot: " ,theta_1 )
    print("Final Value of Theta 2 for your Robot: " ,final_theta_2 )
    print("Final Value of Theta 3 for your Robot: " ,final_theta_3 )

    theta_1 = round(theta_1,2)
    final_theta_2 = round(final_theta_2,2)
    final_theta_3= round(final_theta_3,2)


    return theta_1,final_theta_2,final_theta_3


while True :
    color = input("Enter which color Arm should Play with: " )
    color = str(color)
    if color == 'white':
        print("color set to",color)
        break

    elif color == 'black':
        print("color set to", color)
        break

    else:
        print("invalid color")
        continue


if  color == 'white':
    Robot_moves_white()
    cap = cv2.VideoCapture(1)
    counter = 1
    while True:
        _,frame_1 = cap.read()
        gray_1= cv2.cvtColor(frame_1,cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame", gray_1)
        
        if cv2.waitKey(5)==27:
            break
    
    sample_1.append(gray_1)
    print("frame captured")
    cv2.destroyWindow("frame")

    while True:
        _,frame_2 = cap.read()
        gray_2 = cv2.cvtColor(frame_2,cv2.COLOR_BGR2GRAY)

        diff = np.absolute(np.int16(gray_2)-np.int16(sample_1[0]))
        diff[diff>255] = 255
        diff = np.uint8(diff)
        
        BW = diff
        BW[BW<=110] = 0
        BW[BW>110] = 1

        a = np.count_nonzero(BW)
        time.sleep(3)

        if a == 1 or a ==2 or a == 3 or a == 4:
            a = 0

        if a>20:
            motion = True


        if motion == True:
            _,frame_3 = cap.read()
            gray_3 = cv2.cvtColor(frame_3 , cv2.COLOR_BGR2GRAY)
            if f == 0:
                subtract = np.absolute(np.int16(gray_1)-np.int16(gray_3))
            else:
                subtract = np.absolute(np.int16(sample_2[0])-np.int16(gray_3))
            subtract[subtract>255] = 255
            subtract = np.uint8(subtract)
            BW2 = subtract
            BW2[BW2<=110] = 0
            BW2[BW2>110] = 1

            b = np.count_nonzero(BW2)
            #print("value of b is: ",b)
            if b<20:
                print("No one Played ")
                motion = False
                a = 0
                continue
            else:
                copy = gray_3
                sample_1[0] = copy
                sample_2[0] = copy
                counter = counter +1
                motion = False
                a = 0
                f = 1
                
                if(counter%2 != 0):
                    print("White played. Now Black's Turn")

                if(counter%2 == 0):
                    print("Black Played. Now White's Turn")
                    Robot_moves_white
                    
                continue

        if cv2.waitKey(5)==27:
            break

        
if  color =='black':
    cap = cv2.VideoCapture(1)
    while True:
        _,frame_1 = cap.read()
        gray_1 = cv2.cvtColor(frame_1,cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame",gray_1)
        
        if cv2.waitKey(5)==27:
            break

    sample_1.append(gray_1)
    print("frame captured")
    cv2.destroyWindow("frame")
    
    while True:
        _,frame_2 = cap.read()
        gray_2 = cv2.cvtColor(frame_2,cv2.COLOR_BGR2GRAY)

        diff = np.absolute(int16(gray_2)-int16(sample_1[0]))
        diff[diff>255] = 255
        diff = np.uint8(diff)
        
        BW = diff
        BW[BW<=110] = 0
        BW[BW>110] = 1

        a = np.count_nonzero(BW)
        time.sleep(3)

        if a == 1 or a ==2 or a == 3 or a == 4:
            a = 0

        if a>20:
            motion = True


        if motion == True:
            _,frame_3 = cap.read()
            gray_3 = cv2.cvtColor(frame_3 , cv2.COLOR_BGR2GRAY)
            if f == 0:
                subtract = np.absolute(np.int16(gray_1)-np.int16(gray_3))
            else:
                subtract = np.absolute(np.int16(sample_2[0])-np.int16(gray_3))
            subtract[subtract>255] = 255
            subtract = np.uint8(subtract)
            BW2 = subtract
            BW2[BW2<=110] = 0
            BW2[BW2>110] = 1

            b = np.count_nonzero(BW2)
            print("value of b is: ",b)
            if b<20:
                print("No Moves on Board ")
                motion = False
                a = 0
                continue
            else:
                print("Someone Played ")
                copy = gray_3
                sample_1[0] = copy
                sample_2[0] = copy
                counter = counter +1
                motion = False
                a = 0
                f = 1
                
                if(counter%2 != 0):
                    print("Black's Turn")
                    Robot_moves_black()
                    print("black Played")

                if(counter%2 == 0):
                    print("White's Turn")
                    
                continue

        if cv2.waitKey(5)==27:
            break

        

