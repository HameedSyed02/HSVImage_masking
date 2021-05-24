import cv2
import numpy as np
import matplotlib.pyplot as plt

def empty(a):
    pass


# track bars
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,260)
cv2.createTrackbar("Hue min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue max", "TrackBars", 34, 179, empty)
cv2.createTrackbar("sat min", "TrackBars", 23, 255, empty)
cv2.createTrackbar("sat max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("val min", "TrackBars", 68, 255, empty)
cv2.createTrackbar("val max", "TrackBars", 255, 255, empty)

img = cv2.imread("car.jpg")
img = cv2.resize(img, (340, 280))
imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

while True:
    # values of track bar
    h_min = cv2.getTrackbarPos("Hue min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue max", "TrackBars")
    s_min = cv2.getTrackbarPos("sat min", "TrackBars")
    s_max = cv2.getTrackbarPos("sat max", "TrackBars")
    v_min = cv2.getTrackbarPos("val min", "TrackBars")
    v_max = cv2.getTrackbarPos("val max", "TrackBars")

    print(h_min, h_max, s_min, s_max, v_min, v_max)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imghsv, lower, upper)
    imgresult = cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow("orginal image", img)
    cv2.imshow("HSV image", imghsv)
    cv2.imshow("mask", mask)
    cv2.imshow("result", imgresult)
    cv2.waitKey(1)