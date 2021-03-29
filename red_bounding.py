import numpy as np
import cv2  
import os

rectag = []
result = []

def image_show(name,img):
    cv2.namedWindow(name,cv2.WINDOW_NORMAL)
    cv2.imshow(name, img)

#frame = cv2.imread('/home/anhdong/data_hdd/Viet_Uc/chat_luong_tom/061916d0a433586d0122.jpg')







def drawing_boundingbox(frame):
    result = []
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # define range of red color in HSV
    lower_red_1 = np.array([0, 70, 50])
    upper_red_1 = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red_1, upper_red_1)


    lower_red_2 = np.array([170, 70, 50])
    upper_red_2 = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red_2, upper_red_2)



    mask = mask1 + mask2 
    # cv2.namedWindow("test_image",cv2.WINDOW_NORMAL)
    # cv2.imshow("test_image",mask)
    contours, _ = cv2.findContours(mask.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2:]
    for c in contours:
        if cv2.contourArea(c) > 20000 and cv2.contourArea(c) < 250000:
            rect = cv2.boundingRect(c)
            #print(rect[2],rect[3])
            #if rect[2] < 100 or rect[3] < 100: continue
            #print(cv2.contourArea(c))
            x,y,w,h = rect
            rectag = [x,y,w,h+20]
            result.append(rectag)
            #cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    #print(result)
    return result
#     #cv2.putText(im,'Moth Detected',(x+w+10,y+h),0,0.3,(0,255,0))

##############################################roi_to_folder#######################

# directory = "/home/anhdong/data_hdd/Viet_Uc/chat_luong_tom/images/so mau tom"
# save_directory = "/home/anhdong/custom_haar_cascade/positive_images"




# for file_name in os.listdir(directory):
#     #output_file_name = os.path.join(save_directory, file_name)
#     img = cv2.imread(os.path.join(directory, file_name))
#     rects = drawing_boundingbox(img)
#     count = 1
#     file_name_ = file_name
#     for rect in rects:
#         x,y,w,h = rect
#         roi = img[y:y+h, x:x+w]
#         file_name = str(count) + "_" + file_name
#         print(file_name)
#         output_file_name = os.path.join(save_directory, file_name)
#         cv2.imwrite(output_file_name,roi)
        
#         file_name = file_name_
#         count+=1
        


#######################################################################################


# # # computes the bounding box for the contour, and draws it on the frame,
# # for contour, hier in zip(contours, hierarchy):
# #     (x,y,w,h) = cv2.boundingRect(contour)
# #     min_x, max_x = min(x, min_x), max(x+w, max_x)
# #     min_y, max_y = min(y, min_y), max(y+h, max_y)
# #     if w > 80 and h > 80:
# #         cv2.rectangle(frame, (x,y), (x+w,y+h), (255, 0, 0), 2)

# # if max_x - min_x > 0 and max_y - min_y > 0:
# #     cv2.rectangle(frame, (min_x, min_y), (max_x, max_y), (255, 0, 0), 2)




# # if len(contours) > 0:
# #     for j, contour in enumerate(contours):
# #         bbox = cv2.boundingRect(contour)
# #         # Create a mask for this contour
# #         contour_mask = np.zeros_like(mask)
# #         cv2.drawContours(contour_mask, contours, j, 255, -1)
#     # red_area = max(contours, key=cv2.contourArea)
#     # x, y, w, h = cv2.boundingRect(red_area)
#     # cv2.rectangle(frame,(x, y),(x+w, y+h),(0, 0, 255), 2)


# image_show('frame', frame)
# image_show('mask', mask)

# cv2.waitKey(0)