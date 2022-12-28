import requests
import json

url = "http://api.languagetool.org/v2/check"
data = {
  "text": "Tis is my first tri",
  "language": "auto"
}
response = requests.post(url, data)
result = json.loads(response.text)
print(result)