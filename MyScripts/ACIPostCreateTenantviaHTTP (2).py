import requests

url = "http://192.168.10.1/api/node/mo/uni/tn-testtenant.json"

payload = "{\r\n  \"fvTenant\": {\r\n    \"attributes\": {\r\n      \"dn\": \"uni/tn-testtenant\",\r\n      \"name\": \"testtenant\",\r\n      \"rn\": \"tn-testtenant\",\r\n      \"status\": \"created\"\r\n    },\r\n    \"children\": []\r\n  }\r\n}"
cookie = {"APIC-cookie": "yJ1j1HxDZIUQIMQ65Xj0ldW59URDo6Sc81l0GNfc7/H08tUduenN+oFKVIAoTqm4LrDRUOsJw8RxkeluYOpiq1SC1xzbWHFYaZDLmO5wD5tpkF7V8eGlwhFippQSOAd0wvjbNCufaJai8qZpvj3n/t43HsHiqCaWbajNeSUp7Xk="}
response = requests.request("POST", url, data=payload, cookies=cookie)

print(response.text)