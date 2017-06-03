#!/bin/sh

curl --request POST -L --cookie ~/.cms --data-binary "@test.jpg" --header "Ocp-Apim-Subscription-Key: d7fe70f094ca40289d88e38db1724880" --header "Content-Type: application/octet-stream" https://api.cognitive.azure.cn/face/v1.0/detect?returnFaceAttributes=age,gender
