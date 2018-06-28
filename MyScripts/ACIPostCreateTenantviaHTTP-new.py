import requests
import json

url = "http://192.168.10.1/api/aaaLogin.json"

payload = "{\n\t\"aaaUser\": {\n\t\t\"attributes\": {\n\t\t\t\"name\": \"admin\",\n\t\t\t\"pwd\": \"ciscoapic\"\n\t\t}\n\t}\n}"
headers = {'Authorization': 'Basic YWRtaW46Y2lzY28='}

response = requests.request("POST", url, data=payload, headers=headers)

json_response = json.loads(response.text)

print('Successfully logged in to APIC.\n')
#print(response.text)
#print(json_response)['imdata'][0]['aaaLogin']['attributes']['token']

tokenfromlogin = (json_response['imdata'][0]['aaaLogin']['attributes']['token'])

# Next API Request (Create Tenant)
url = "http://192.168.10.1/api/node/mo/uni/tn-testtenant.json"

payload = "{\r\n  \"fvTenant\": {\r\n    \"attributes\": {\r\n      \"dn\": \"uni/tn-testtenant\",\r\n      \"name\": \"testtenant\",\r\n      \"rn\": \"tn-testtenant\",\r\n      \"status\": \"created\"\r\n    },\r\n    \"children\": []\r\n  }\r\n}"
cookie = {"APIC-cookie": tokenfromlogin}
response = requests.request("POST", url, data=payload, cookies=cookie)

print(response.text)
print('Tenant has been successfully created.\n')

