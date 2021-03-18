import cv2 
import time 
import pygame

W = 1920//2
H = 1080//2

cv2.namedWindow('image', cv2.WINDOW_NORMAL)

def process_frame(img): 
    img = cv2.resize(img, (W,H))
    cv2.imshow('image', img)
    cv2.waitKey() 
    print(img.shape)
    
if __name__ == '__main__':
    cap = cv2.VideoCapture('./videos/test_ohio.mp4')
    
    while cap.isOpened():
        ret, frame = cap.read() 
        if ret == True:
            process_frame(frame)
        else:
            break 

    
