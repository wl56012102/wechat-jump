import os

def jump(time):
    os.system("adb shell input touchscreen swipe 100 100 100 100 %s"%time)

if __name__ == '__main__':
    while(1):
        time1 = input("time:")
        jump(int(time1)*105)