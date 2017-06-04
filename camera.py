import picamera
import serial
import cv2
import httplib, urllib, base64
import urllib2
import json
import time
import traceback

camera = picamera.PiCamera()
camera.resolution = (360, 240)
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

headers = {
    # Request headers
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': '1689b66293c84ff3bd421dd89c8cd701',
}

params = urllib.urlencode({
    # Request parameters
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,facialHair,hair,makeup',
})

server_url = "http://172.31.11.38/sensors/"
server_ip = "172.31.11.38:8000"

server_headers = {
     'Content-Type': 'application/json',
}

try:
    conn = httplib.HTTPSConnection('api.cognitive.azure.cn')
except Exception as e:
    print("Cannot connect to Azure API!")
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
    exit(1)

try:
    server_conn = httplib.HTTPConnection(server_ip)
except Exception as e:
    print("Cannot connect to Server!")
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
    exit(1)

while (True):
    camera.capture('test.jpg')
    with open("test.jpg", "rb") as f:
        frame = f.read()
        # print frame
        f.close()
    try:
        conn.request("POST", "/face/v1.0/detect?%s" % params, frame, headers)
        response = conn.getresponse()
        face_data = response.read()
        print("face: " + face_data)
	air_data = ser.readline()
        air_data = air_data.strip()
        print len(air_data)
        if (air_data == ""):
            air_data = 'NONE'
	print("air: " + air_data)
	server_data = {
            'face': face_data,
            'air': air_data,
        }
        # server_req = urllib2.Request(server_url)
        # server_req.add_header('Content-Type', 'application/json')
        # server_response = urllib2.urlopen(server_req, json.dumps(server_data))
        # print("server: " + server_response)

        server_conn.request("POST", "/sensors/", json.dumps(server_data), server_headers)
        server_resp = server_conn.getresponse()
        print("server: %d %s" % (server_resp.status, server_resp.reason))

    except Exception as e:
        print e
        traceback.print_exc()
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
        exit(1)
    if cv2.waitKey(3000) & 0xFF == ord('q'):
        conn.close()
        break
