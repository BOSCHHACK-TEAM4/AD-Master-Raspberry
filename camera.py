import picamera
import cv2
import httplib, urllib, base64
import json
import time

camera = picamera.PiCamera()
camera.resolution = (360, 240)

headers = {
    # Request headers
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': '1689b66293c84ff3bd421dd89c8cd701',
}

params = urllib.urlencode({
    # Request parameters
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender',
})


try:
    conn = httplib.HTTPSConnection('api.cognitive.azure.cn')
except Exception as e:
    print("Cannot connected!")
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
    exit(1)

while (True):
    # frame = list()
    camera.capture('test.jpg')
    # camera.capture(frame)
    # frame = cv2.imread('test.jpg')
    with open("test.jpg", "rb") as f:
        frame = f.read()
        # print frame
        f.close()
    # cv2.imshow('test', frame)
    try:
        conn.request("POST", "/face/v1.0/detect?%s" % params, frame, headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
        exit(1)
    if cv2.waitKey(1000) & 0xFF == ord('q'):
        conn.close()
        break
