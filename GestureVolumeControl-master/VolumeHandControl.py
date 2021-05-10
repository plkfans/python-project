import cv2
import time
import numpy as np
import HandTrackingMoudle as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

########################
wCam, hCam = 640, 480
########################

# 输入的视频，“0”为打开摄像头
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
detector = htm.handDetector(detectionCon=0.7)  # 创建对象

#音量控制
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange()  # 获取音量范围 -74 -- 0


minVol = volRange[0]#-74
maxVol = volRange[1]#0
vol = 0
volBar=400#img上的进度条
volPer=0 #电脑上的音量条


while True:

    success, img = cap.read()
    # 检测手
    img = detector.findHands(img)
    # 检测手的标志，并返回标志点坐标
    lmList = detector.findPosition(img, personDraw=False)

    if len(lmList) != 0:
        #print(lmList[4], lmList[8])#[4, 295, 184] [8, 310, 146]

        # 计算食指和大拇指指尖坐标，并绘制点、连线
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)#将img图像上的 (x1, y1)点 配置为 半径为15 颜色为紫色 填充
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)#在将img图像上的  线段(x1, y1), (x2, y2) 颜色为紫色 宽度为3

        cLength = math.hypot(x2 - x1, y2 - y1)
        # print(cLength)


        # Hand range 10-450（根据实际情况自己修改）
        vol = np.interp(cLength, [20, 300], [minVol, maxVol])  # interp()是进行线性内插，返回一个与length同形状的数
        volBar = np.interp(cLength, [20, 300], [400, 150])
        volPer = np.interp(cLength, [20, 300], [0, 100])
        volume.SetMasterVolumeLevel(int(vol), None)  # 设置音量值

        if int(cLength) <= 20:
            cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)



    # 绘制音量图
    cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)  # 外框 起始位置 结束位置 颜色 宽度
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
    cv2.putText(img, str(int(volPer)) + "%", (40, 430), cv2.FONT_HERSHEY_COMPLEX,
                    1, (255, 0, 0), 2)


    cTime = time.time()  #当前时间 设置为 时间点时间
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, "FPS:" + str(int(fps)), (20, 30), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 0, 0), 2) #“FPS”+以字符串形式显示+坐标+字体+字体大小+颜色+字体粗细

    cv2.imshow("Image", img) #显示图像
    cv2.waitKey(5) #延时为5毫秒
