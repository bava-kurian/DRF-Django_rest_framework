import requests
endpoint="https://httpbin.org/anything"

get_response=requests.get(endpoint,json={"query":"HelloWorld"})

print(get_response.json())