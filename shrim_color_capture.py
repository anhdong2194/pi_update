# import the necessary packages
# import the necessary packages
import argparse
import cv2
from color_area import *
from red_bounding import *
from box_detect import *
from transform import four_point_transform



from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import os
import RPi.GPIO as GPIO
import subprocess


from collections import Counter


#org = (5, 30) 
font = cv2.FONT_HERSHEY_SIMPLEX 
fontScale = 2
color = (0, 0, 255)
thickness = 2
coords = [(360,0),(500,3040),(3600,3040),(3600,0)]
count_button = 0
button_flag = 0

refPt = []
cropping = False
index = np.arange(20,35)



# capture_pin = 37
Led_white = 37
# net_control  = 40

GPIO.setwarnings(False)

# Use "GPIO" pin numbering
GPIO.setmode(GPIO.BOARD)

# Use built-in internal pullup resistor so the pin is not floating
# if using a momentary push button without a resistor.
#GPIO.setup(shutdown_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Use Qwiic pHAT's pullup resistor so that the pin is not floating
# GPIO.setup(capture_pin, GPIO.IN,pull_up_down=GPIO.PUD_UP)

GPIO.setup(Led_white, GPIO.OUT)
# GPIO.setup(net_control, GPIO.OUT)


save_directory = "/home/pi/Desktop/raspberry/image_save/"

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (4056,3040)
#camera.framerate = 30
rawCapture = PiRGBArray(camera)
# allow the camera to warmup
time.sleep(0.1)
# capture frames from the camera
count = 1
flag = 0
# GPIO.output(net_control, GPIO.HIGH)
GPIO.output(Led_white, GPIO.LOW)
# capture_flag = 0



def shut_down():
    print("shutting down")
    command = "/usr/bin/sudo /sbin/shutdown -h now"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print(output)



def white_balance(img):
    result = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    avg_a = np.average(result[:, :, 1])
    avg_b = np.average(result[:, :, 2])
    result[:, :, 1] = result[:, :, 1] - ((avg_a - 128) * (result[:, :, 0] / 255.0) * 1.1)
    result[:, :, 2] = result[:, :, 2] - ((avg_b - 128) * (result[:, :, 0] / 255.0) * 1.1)
    result = cv2.cvtColor(result, cv2.COLOR_LAB2BGR)
    return result




def color_index(t,a):
    hour = int(time.strftime("%H"))
    GPIO.output(Led_white, GPIO.HIGH)
    time.sleep(3)
    flag = 1
    button_flag = 0
    print("start capture")
    value = []
    # key = input('Enter your input:')
    # if GPIO.input(capture_pin) == False and button_flag == 0:
    #     count_button += 1
    #     if count_button > 20:
    #         button_flag = 1
    #     else:
    #         pass
    # else:
    #     count_button = 0
    #     #time.sleep(1)
    # if button_flag == 1:
    #     if GPIO.input(capture_pin) == False:
    #         # print("net up")			
    #         # GPIO.output(net_control, GPIO.LOW)
    #         GPIO.output(Led_white, GPIO.HIGH)
    #         # if hour >=17 or hour <= 5:
    #         # 	GPIO.output(Led_white, GPIO.HIGH)
    #         # 	print("led on")
    #         # else:
    #         # 	GPIO.output(Led_white, GPIO.LOW)
    #         # 	print("led off")
    #         time.sleep(3)
    #         flag = 1
    #         button_flag = 0
    #         print("start capture")

    #     else:
    #         pass
        
    while flag == 1 :
        camera.capture(rawCapture,format="bgr")
        image_ = rawCapture.array
        original_image = image_
        pts = np.array(coords, dtype = "float32")
        image = four_point_transform(image_, pts)
        #auto_result = white_balance(image)
        clone = image
        rects = []
        if len(box_detect(clone)) != 0:
            rects = drawing_boundingbox(clone) #box_detect(clone)
        else:
            rects = drawing_boundingbox(clone)

        roi_image = []
        count = 0

        for rect in rects:
            #rect = cv2.boundingRect(rect)
            x,y,w,h = rect
            roi = image[y:y+h, x:x+w]
            area = color_area(roi)
            area_sort = sorted(area)
            if sum(area) > 10:
                cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
                #print(area[0])
                # max_idx = np.where(area == np.amax(area))[0]
                # secon_idx = np.where(area == area_sort[-2])[0]
                #print(index[area.index(area_sort[2])])
                # print(area.index(area_sort[-2]))
                # print(area_sort[-2])
                # print(area_sort)


                # if area_sort[-2] > 120000:
                #     if int(area_sort[-1]-area_sort[-2]) < 30000 and int(index[area.index(area_sort[-2])] - index[area.index(area_sort[-1])]) == 1:
                #         text = str(index[area.index(area_sort[-2])])
                #         value.append(int(text))
                #         # print("area = ",area[area.index(area_sort[-2])] ,count_)
                #         #print(area.index(area_sort[-2]),"text heare ",text)
                #     else:
                #         text = str(index[area.index(area_sort[-1])])
                #         value.append(int(text))
                #         # print("area = ",area[area.index(area_sort[-1])] , count_)
                #         #print(text)
                # else:
                #     if int(area_sort[-1]-area_sort[-2]) < 12000 and int(index[area.index(area_sort[-2])] - index[area.index(area_sort[-1])]) == 1 and index[area.index(area_sort[-1])] < 22:
                #         text = str(index[area.index(area_sort[-2])])
                #         value.append(int(text))
                #     else:
                #         text = str(index[area.index(area_sort[-1])])
                #         value.append(int(text))

                # print(area_sort[-1]-area_sort[-2],"max index")
                # print(area,type(area))
                #print(area[max_idx] - area[max_idx + 1])
                #if area[max_idx] - area[max_idx + 1] > 100:
                #print(idx)
                idx = np.where(area == np.amax(area))
                if len((index[idx])) < 2:
                    text = str(int(index[idx]))
                    value.append(int(text))
                    cv2.putText(roi, text, (10,80), font,fontScale, color, thickness, cv2.LINE_AA)
                else:
                    text = str(int(max(index[idx])))
                    value.append(int(text))
                    cv2.putText(roi, text, (10,80), font,fontScale, color, thickness, cv2.LINE_AA)
                # text = str(index[idx])
                # value.append(int(text))
                cv2.putText(roi, text, (10,80), font,fontScale, color, thickness, cv2.LINE_AA)
                #image_show("roi%d"%count,roi)
                roi_image.append(roi)
                #count+=1

        else:
            strings = "NM_" + "Trai_" + t +"_" + "ao_" + a + "_"  + time.strftime("%d,%m,%Y,%H,%M,%S").replace(",","-")
            print(strings)
            output_file_name = os.path.join(save_directory,strings + ".jpg")
            ori_output = os.path.join(save_directory, strings + "_" +"orig" + ".jpg")
            cv2.imwrite(output_file_name,image)
            cv2.imwrite(ori_output,original_image)
            print("done write file to raspberry pi")
            subprocess.call(['sh','/home/pi/Desktop/raspberry/image_upload_drive/move.sh'])
            print("Done update to my drive ")
            capture_flag =0
            flag = 0
            time.sleep(1)
            GPIO.output(Led_white, GPIO.LOW)
            # cv2.namedWindow("image",cv2.WINDOW_NORMAL)
            # cv2.imshow("image",image)

            # key = cv2.waitKey(1) & 0xFF
            # if key == ord("q") or key == 27:
            #     capture_flag =0
            #     flag = 0
            #     time.sleep(1)
            #     GPIO.output(Led_white, GPIO.LOW)
            # elif key == ord("s"):
            #     strings = time.strftime("%H,%M,%S,%d,%m,%Y").replace(",","-")
            #     output_file_name = os.path.join(save_directory, strings + ".jpg")
            #     ori_output = os.path.join(save_directory, strings + "_" +"orig" + ".jpg")
            #     cv2.imwrite(output_file_name,image)
            #     cv2.imwrite(ori_output,original_image)
            #     print("done write file to raspberry pi")
            #     subprocess.call(['sh','/home/pi/Desktop/raspberry/image_upload_drive/move.sh'])
            #     print("Done update to my drive ")
            #     capture_flag =0
            #     flag = 0
            #     time.sleep(1)
            #     GPIO.output(Led_white, GPIO.LOW)
    print("Ao: " + a +" " + "trai: " + t)
    rawCapture.truncate(0)
    return image,value
    #break
    # rawCapture.truncate(0)
    # cv2.destroyAllWindows()
        # clone = image.copy()
        # if len(box_detect(clone)) != 0:
        #     rects = drawing_boundingbox(clone) #box_detect(clone)
        # else:
        #     rects = drawing_boundingbox(clone)
        











        ##################################################################################
		# if count < 6:

		# 	#GPIO.output(Led_blue, GPIO.HIGH)
		# 	#time.sleep(1)

		# 	#GPIO.output(Led_blue, GPIO.LOW)
			

		# 	strings = time.strftime("%H,%M,%S,%d,%m,%Y").replace(",","-")
		# 	output_file_name = os.path.join(save_directory, strings + ".jpg")
		# 	#print("asasd",output_file_name)
		# 	# grab the raw NumPy array representing the image, then initialize the timestamp
		# 	# and occupied/unoccupied text
		# 	time.sleep(2)
		# 	camera.capture(output_file_name)
		# 	#image = rawCapture.array




			
		# 	#cv2.imwrite(output_file_name,image)
		# 	time.sleep(2)
		# 	count += 1
		# 	# show the frame
		# 	#cv2.imshow("Frame", img)
		# 	#key = cv2.waitKey(1) & 0xFF
		# 	# clear the stream in preparation for the next frame
		# 	#rawCapture.truncate(0)
		# 	# if the `q` key was pressed, break from the loop
		# 	# if count == 5:
		# 	# 	count = 0
		# 	# 	GPIO.output(Led_white, GPIO.LOW)
		# 	# 	break
		# 	# count += 1
		# 		#time.sleep(0.5)
		# 	#cv2.destroyAllWindows()
		# 	#break
		# else:
		# 	GPIO.output(Led_white, GPIO.LOW)
		# 	# GPIO.output(net_control, GPIO.HIGH)
		# 	#time.sleep(5)
		# 	print("start upload to drive")
		# 	subprocess.call(['sh','/home/pi/Desktop/raspberry/image_upload_drive/copy.sh'])
		# 	print("upload to teamdrive completed")
		# 	subprocess.call(['sh','/home/pi/Desktop/raspberry/image_upload_drive/move.sh'])
		# 	print("update to my drive ")
		# 	count = 1
		# 	flag = 0
		# 	#print("net down")
		# 	#shut_down()
		# 	break
		
	
