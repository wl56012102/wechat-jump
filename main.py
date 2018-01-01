import os
import cv2
import time

def jump(time):
    os.system("adb shell input touchscreen swipe 100 100 100 100 %s"%time)

def get_png():
    os.system("adb shell screencap -p /sdcard/screen.png")
    os.system("adb pull /sdcard/screen.png")
    os.system("adb shell rm /sdcard/screen.png")

def draw_circle(event, x, y, flags, param):
    global start_x,start_y,end_x,end_y
    if event == cv2.EVENT_LBUTTONDOWN:
        start_x,start_y=x,y
    if event == cv2.EVENT_LBUTTONUP:
        end_x,end_y=x,y

if __name__ == '__main__':
    start_x, start_y, end_x, end_y=0,0,0,0
    cv2.namedWindow('img')
    cv2.setMouseCallback('img',draw_circle)
    get_png()
    while(1):
        img = cv2.imread('screen.png')
        img = cv2.resize(img,(288,510))
        cv2.imshow('img',img)
        k =cv2.waitKey(5) & 0xFF
        if  k== ord('p'):
            break
        if k ==ord('1'):
            get_png()
        if end_x!=0:
            dis=(abs(end_x-start_x)**2+abs(end_y-start_y)**2)**0.5
            time1 = int(dis*5)
            jump(time1)
            time.sleep(1)
            get_png()
            start_x, start_y, end_x, end_y = 0, 0, 0, 0
    cv2.destroyAllWindows()
