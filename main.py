import cv2 as cv
capture = cv.VideoCapture(0)

capture.set(3, 640)
capture.set(4, 480)

background = cv.imread("resources//background//background.jpg")
cv.imshow("background", background)
while True:
    isTrue, frame = capture.read()
    
    cv.imshow("Face attdendance", frame)
    cv.imshow("webcam", background)
    cv.waitKey(1)

