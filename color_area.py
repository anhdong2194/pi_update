import numpy as np
import cv2

f_l = open("/home/anhdong/data_hdd/Viet_Uc/chat_luong_tom/lower.txt", "r")
lower = []
for x_l in f_l:
    out = np.array([int(i.replace(',','')) for i in x_l[x_l.find('[')+1:x_l.find(']')].split()])
    lower.append(out)
f_u = open("/home/anhdong/data_hdd/Viet_Uc/chat_luong_tom/upper.txt", "r")
upper = []
for x_u in f_u:
    out = np.array([int(i.replace(',','')) for i in x_u[x_u.find('[')+1:x_u.find(']')].split()])
    upper.append(out)
count = 0
abjust = 4
abjust_2 = 5

#print(lower[1])
def color_area(img):
    area_ = []
    area = []
    hsvFrame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    global count

    redB1_lower = np.array([-3,118,138]) + abjust #, np.uint8) 
    redB1_upper = np.array([17,138,218]) - abjust #, np.uint8) 
    redB1_mask = cv2.inRange(hsvFrame, redB1_lower, redB1_upper) 

    redB11_lower = np.array([-3,117,135]) + abjust#, np.uint8) 
    redB11_upper = np.array([17,138,215]) - abjust#, np.uint8) 
    redB11_mask = cv2.inRange(hsvFrame, redB11_lower, redB11_upper)

    redB12_lower = np.array([-3,120,133]) + abjust#, np.uint8) 
    redB12_upper = np.array([17,140,213]) - abjust#, np.uint8) 
    redB12_mask = cv2.inRange(hsvFrame, redB12_lower, redB12_upper)

    redB13_lower = np.array([-3,115,139]) + abjust#, np.uint8) 
    redB13_upper = np.array([17,135,219]) - abjust#, np.uint8) 
    redB13_mask = cv2.inRange(hsvFrame, redB13_lower, redB13_upper)

    redB14_lower = np.array([-2,114,135]) + abjust#, np.uint8) 
    redB14_upper = np.array([18,134,215]) - abjust#, np.uint8) 
    redB14_mask = cv2.inRange(hsvFrame, redB14_lower, redB14_upper)

    redB15_lower = np.array([-3,116,138]) + abjust#, np.uint8) 
    redB15_upper = np.array([17,136,218]) - abjust#, np.uint8) 
    redB15_mask = cv2.inRange(hsvFrame, redB15_lower, redB15_upper)


    redB16_lower = np.array([-3,110,123]) + abjust#, np.uint8) 
    redB16_upper = np.array([17,130,203]) - abjust#, np.uint8) 
    redB16_mask = cv2.inRange(hsvFrame, redB16_lower, redB16_upper)

    redB17_lower = np.array([-3,106,134]) + abjust#, np.uint8) 
    redB17_upper = np.array([17,126,214]) - abjust#, np.uint8) 
    redB17_mask = cv2.inRange(hsvFrame, redB17_lower, redB17_upper)

    redB18_lower = np.array([-3,108,127]) + abjust#, np.uint8) 
    redB18_upper = np.array([17,128,207]) - abjust#, np.uint8) 
    redB18_mask = cv2.inRange(hsvFrame, redB18_lower, redB18_upper)

    redB2_lower = np.array([-3,133,138]) + abjust_2#, np.uint8) 
    redB2_upper = np.array([17,153,218]) - abjust_2#, np.uint8) 
    redB2_mask = cv2.inRange(hsvFrame, redB2_lower, redB2_upper) 

    redB21_lower = np.array([-3,123,134]) + abjust_2#, np.uint8) 
    redB21_upper = np.array([17,143,214]) - abjust_2#, np.uint8) 
    redB21_mask = cv2.inRange(hsvFrame, redB21_lower, redB21_upper)  

    redB22_lower = np.array([-3,131,124]) + abjust_2#, np.uint8) 
    redB22_upper = np.array([17,151,204]) - abjust_2#, np.uint8) 
    redB22_mask = cv2.inRange(hsvFrame, redB22_lower, redB22_upper)  

    redB23_lower = np.array([-6,119,122]) + abjust_2#, np.uint8) 
    redB23_upper = np.array([14,139,202]) - abjust_2#, np.uint8) 
    redB23_mask = cv2.inRange(hsvFrame, redB23_lower, redB23_upper)  

    redB24_lower = np.array([-3,127,129]) + abjust_2#, np.uint8) 
    redB24_upper = np.array([17,147,209]) - abjust_2#, np.uint8) 
    redB24_mask = cv2.inRange(hsvFrame, redB24_lower, redB24_upper)  

    redB25_lower = np.array([-5,121,118]) + abjust_2#, np.uint8) 
    redB25_upper = np.array([15,141,198]) - abjust_2#, np.uint8) 
    redB25_mask = cv2.inRange(hsvFrame, redB25_lower, redB25_upper) 

    redB26_lower = np.array([-6,119,122])#, np.uint8) 
    redB26_upper = np.array([14,139,202])#, np.uint8) 
    redB26_mask = cv2.inRange(hsvFrame, redB26_lower, redB26_upper)


    redB27_lower = np.array([-3,127,129]) + abjust_2#, np.uint8) 
    redB27_upper = np.array([17,147,209]) - abjust_2#, np.uint8) 
    redB27_mask = cv2.inRange(hsvFrame, redB27_lower, redB27_upper)

    redB28_lower = np.array([-3,129,122]) + abjust_2#, np.uint8) 
    redB28_upper = np.array([17,149,202]) - abjust_2#, np.uint8) 
    redB28_mask = cv2.inRange(hsvFrame, redB28_lower, redB28_upper) 

    redB29_lower = np.array([1,130,164]) + abjust_2#, np.uint8) 
    redB29_upper = np.array([11,140,184]) - abjust_2#, np.uint8) 
    redB29_mask = cv2.inRange(hsvFrame, redB29_lower, redB29_upper) 

    redB20_lower = np.array([-3,123,129]) + abjust_2#, np.uint8) 
    redB20_upper = np.array([17,143,209]) - abjust_2#, np.uint8) 
    redB20_mask = cv2.inRange(hsvFrame, redB20_lower, redB20_upper)



    



    ###############################################################
    

    red1_lower = lower[0] #, np.uint8) 
    red1_upper = upper[0]#, np.uint8) 
    red1_mask = cv2.inRange(hsvFrame, red1_lower, red1_upper) # + redB1_mask + redB11_mask + redB12_mask + redB13_mask + redB14_mask + redB15_mask  + redB16_mask + redB17_mask + redB18_mask


    red2_lower = lower[1]#, np.uint8) 
    red2_upper = upper[1]#, np.uint8) 
    red2_mask = cv2.inRange(hsvFrame, red2_lower, red2_upper) #+ redB2_mask + redB21_mask + redB22_mask + redB23_mask + redB24_mask + redB25_mask + redB26_mask + redB27_mask + redB28_mask + redB29_mask + redB20_mask

    

    red3_lower = lower[2]#, np.uint8) 
    red3_upper = upper[2]#, np.uint8) 
    red3_mask = cv2.inRange(hsvFrame, red3_lower, red3_upper)


    red4_lower = lower[3]#, np.uint8) 
    red4_upper = upper[3]#, np.uint8) 
    red4_mask = cv2.inRange(hsvFrame, red4_lower, red4_upper)

    red5_lower = lower[4]#, np.uint8) 
    red5_upper = upper[4]#, np.uint8) 
    red5_mask = cv2.inRange(hsvFrame, red5_lower, red5_upper)

    red6_lower = lower[5]#, np.uint8) 
    red6_upper = upper[5]#, np.uint8) 
    red6_mask = cv2.inRange(hsvFrame, red6_lower, red6_upper)


    red7_lower = lower[6]#, np.uint8) 
    red7_upper = upper[6]#, np.uint8) 
    red7_mask = cv2.inRange(hsvFrame, red7_lower, red7_upper)


    red8_lower = lower[7]#, np.uint8) 
    red8_upper = upper[7]#, np.uint8) 
    red8_mask = cv2.inRange(hsvFrame, red8_lower, red8_upper)


    red9_lower = lower[8]#, np.uint8) 
    red9_upper = upper[8]#, np.uint8) 
    red9_mask = cv2.inRange(hsvFrame, red9_lower, red9_upper)

    red10_lower = lower[9]#, np.uint8) 
    red10_upper = upper[9]#, np.uint8) 
    red10_mask = cv2.inRange(hsvFrame, red10_lower, red10_upper)


    red11_lower = lower[10]#, np.uint8) 
    red11_upper = upper[10]#, np.uint8) 
    red11_mask = cv2.inRange(hsvFrame, red11_lower, red11_upper)


    red12_lower = lower[11]#, np.uint8) 
    red12_upper = upper[11]#, np.uint8) 
    red12_mask = cv2.inRange(hsvFrame, red12_lower, red12_upper)


    red13_lower = lower[12]#, np.uint8) 
    red13_upper = upper[12]#, np.uint8) 
    red13_mask = cv2.inRange(hsvFrame, red13_lower, red13_upper)


    red14_lower = lower[13]#, np.uint8) 
    red14_upper = upper[13]#, np.uint8) 
    red14_mask = cv2.inRange(hsvFrame, red14_lower, red14_upper)


    red15_lower = lower[14]#, np.uint8) 
    red15_upper = upper[14]#, np.uint8) 
    red15_mask = cv2.inRange(hsvFrame, red15_lower, red15_upper)


    ###############################################################

    kernal = np.ones((5, 5), "uint8") 

    ######red-1 mask

    red1_mask = cv2.dilate(red1_mask, kernal) 
    res1_red = cv2.bitwise_and(img, img, mask = red1_mask) 

    ######red-2 mask

    red2_mask = cv2.dilate(red2_mask, kernal) 
    res2_red = cv2.bitwise_and(img, img, mask = red2_mask) 

    #####red-3 mask

    red3_mask = cv2.dilate(red3_mask, kernal) 
    res3_red = cv2.bitwise_and(img, img, mask = red3_mask) 


    #####red-4 mask

    red4_mask = cv2.dilate(red4_mask, kernal) 
    res4_red = cv2.bitwise_and(img, img, mask = red4_mask) 


    #####red-5 mask

    red5_mask = cv2.dilate(red5_mask, kernal) 
    res5_red = cv2.bitwise_and(img, img, mask = red5_mask) 


    #####red-3 mask

    red6_mask = cv2.dilate(red6_mask, kernal) 
    res6_red = cv2.bitwise_and(img, img, mask = red6_mask) 


    #####red-3 mask

    red7_mask = cv2.dilate(red7_mask, kernal) 
    res7_red = cv2.bitwise_and(img, img, mask = red7_mask) 


    #####red-3 mask

    red8_mask = cv2.dilate(red8_mask, kernal) 
    res8_red = cv2.bitwise_and(img, img, mask = red8_mask) 


    #####red-3 mask

    red9_mask = cv2.dilate(red9_mask, kernal) 
    res9_red = cv2.bitwise_and(img, img, mask = red9_mask) 


    #####red-3 mask

    red10_mask = cv2.dilate(red10_mask, kernal) 
    res10_red = cv2.bitwise_and(img, img, mask = red10_mask) 


    #####red-3 mask

    red11_mask = cv2.dilate(red11_mask, kernal) 
    res11_red = cv2.bitwise_and(img, img, mask = red11_mask) 


    #####red-3 mask

    red12_mask = cv2.dilate(red12_mask, kernal) 
    res12_red = cv2.bitwise_and(img, img, mask = red12_mask) 


    #####red-3 mask

    red13_mask = cv2.dilate(red13_mask, kernal) 
    res13_red = cv2.bitwise_and(img, img, mask = red13_mask) 


    #####red-3 mask

    red14_mask = cv2.dilate(red14_mask, kernal) 
    res14_red = cv2.bitwise_and(img, img, mask = red14_mask) 


    #####red-3 mask

    red15_mask = cv2.dilate(red15_mask, kernal) 
    res15_red = cv2.bitwise_and(img, img, mask = red15_mask) 


    contours, hierarchy = cv2.findContours(red1_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2:]
    for cnt in contours:
        area_.append(cv2.contourArea(cnt))
    area.append(sum(area_))
    area_ = []

    contours, hierarchy = cv2.findContours(red2_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2:]
    for cnt in contours:
        area_.append(cv2.contourArea(cnt))
    area.append(sum(area_))
    area_ = []

    contours, hierarchy = cv2.findContours(red3_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2:]
    for cnt in contours:
        area_.append(cv2.contourArea(cnt))
    area.append(sum(area_))
    area_ = []

    contours, hierarchy = cv2.findContours(red4_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2:]
    for cnt in contours:
        area_.append(cv2.contourArea(cnt))
    area.append(sum(area_))
    area_ = []


    contours, hierarchy = cv2.findContours(red5_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2:]
    for cnt in contours:
        area_.append(cv2.contourArea(cnt))
    area.append(sum(area_))
    area_ = []


    contours, hierarchy = cv2.findContours(red6_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2:]
    for cnt in contours:
        area_.append(cv2.contourArea(cnt))
    area.append(sum(area_))
    area_ = []


    contours, hierarchy = cv2.findContours(red7_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2:]
    for cnt in contours:
        area_.append(cv2.contourArea(cnt))
    area.append(sum(area_))
    area_ = []


    contours, hierarchy = cv2.findContours(red8_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2:]
    for cnt in contours:
        area_.append(cv2.contourArea(cnt))
    area.append(sum(area_))
    area_ = []


    contours, hierarchy = cv2.findContours(red9_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2:]
    for cnt in contours:
        area_.append(cv2.contourArea(cnt))
    area.append(sum(area_))
    area_ = []


    contours, hierarchy = cv2.findContours(red10_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2:]
    for cnt in contours:
        area_.append(cv2.contourArea(cnt))
    area.append(sum(area_))
    area_ = []


    contours, hierarchy = cv2.findContours(red11_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2:]
    for cnt in contours:
        area_.append(cv2.contourArea(cnt))
    area.append(sum(area_))
    area_ = []


    contours, hierarchy = cv2.findContours(red12_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2:]
    for cnt in contours:
        area_.append(cv2.contourArea(cnt))
    area.append(sum(area_))
    area_ = []

    contours, hierarchy = cv2.findContours(red13_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2:]
    for cnt in contours:
        area_.append(cv2.contourArea(cnt))
    area.append(sum(area_))
    area_ = []

    contours, hierarchy = cv2.findContours(red14_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2:]
    for cnt in contours:
        area_.append(cv2.contourArea(cnt))
    area.append(sum(area_))
    area_ = []


    contours, hierarchy = cv2.findContours(red15_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2:]
    for cnt in contours:
        area_.append(cv2.contourArea(cnt))
    area.append(sum(area_))
    area_ = []
    # idx = np.where(area == np.amax(area))[0] + 1
    # # print(idx)
    # cv2.imshow("res{}_red_{}".format(idx,count),eval('res%d_red'% (idx)))
    # count += 1
    return area#res1_red,res2_red,res3_red,area
    

