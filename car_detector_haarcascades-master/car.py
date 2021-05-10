import cv2

car_cascade = cv2.CascadeClassifier('haarcascade_car.xml')
cap = cv2.VideoCapture("cars.mp4")

while cap.isOpened():
    success, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#将img 转化为灰度图像

    # 灰度图像 1.1表示决定两个不同大小的窗口扫描之间有多大的跳跃 6表明至少有6次重叠检测，我们才认为汽车存在。
    cars = car_cascade.detectMultiScale(gray, 1.1, 6)
    print(cars)
    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w+5,y+h+5),(0,0,255),3)#跟踪框的设置

    cv2.imshow('Car Detector',img)

    if cv2.waitKey(30) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()