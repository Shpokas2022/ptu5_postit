import requests

reqUrl = "http://127.0.0.1:8000/posts"

headersList = {
 "Accept": "*/*",
 "User-Agent": "CodeAcademy API Tests App" 
}

payload = ""

response = requests.request("GET", reqUrl, data=payload,  headers=headersList)

print(response.text)