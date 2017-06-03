import httplib, urllib, base64
import json
import time


headers = {
    # Request headers
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': 'd7fe70f094ca40289d88e38db1724880',
}

params = urllib.urlencode({
    # Request parameters
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender',
})


try:
    conn = httplib.HTTPSConnection('api.cognitive.azure.cn')
    with open("test.jpg", "rb") as f:
        frame = f.read()
        # print frame
        f.close()
    conn.request("POST", "/face/v1.0/detect?%s" % params, frame, headers)
    
    response = conn.getresponse()
    data = response.read()
    conn.close()
    print(data)
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
    exit(1)

