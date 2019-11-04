#!/usr/bin/env python3
# coding: utf-8
#

import time
import subprocess
import queue
import threading

import cv2
from hyperlpr import *


def read_from_camera():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if frame is None:
            continue
        yield frame


def say_lp(q):
    while True:
        lp = q.get()
        subprocess.run(['say', lp])
    

if __name__ == "__main__":
    cars = {}
    say_que = queue.Queue(10)

    for im in read_from_camera():
        #frame = cv2.imread("car410.jpg")
        result = HyperLPR_PlateRecogntion(im)
        print(time.ctime(), result)
        if not result:
            continue

        print(time.ctime(), result)

        if len(result) == 1:
            license_plate = result[0][0]
            cv2.imwrite("cars/"+license_plate+".jpg", frame)
            que.put(license_plate)
