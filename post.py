import json

headers = {
    # Request headers
    'Content-Type': 'application/json',
}

url = ''

try:
    conn = httplib.HTTPSConnection(url)
except Exception as e:
    print("Cannot connected!")
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
    exit(1)
    
try:
        conn.request("POST", data, headers)

