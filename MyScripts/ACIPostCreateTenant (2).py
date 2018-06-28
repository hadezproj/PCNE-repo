import requests

url = "https://192.168.10.1/api/node/mo/uni/tn-testtenant.json"

payload = "{\r\n  \"fvTenant\": {\r\n    \"attributes\": {\r\n      \"dn\": \"uni/tn-testtenant\",\r\n      \"name\": \"testtenant\",\r\n      \"rn\": \"tn-testtenant\",\r\n      \"status\": \"created\"\r\n    },\r\n    \"children\": []\r\n  }\r\n}"
headers = {'Authorization': 'Basic YWRtaW46Y2lzY28='}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)