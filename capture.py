#!/usr/bin/python
import picamera
import time

camera = picamera.PiCamera()
camera.resolution = (360, 240)
camera.capture('test.jpg')
