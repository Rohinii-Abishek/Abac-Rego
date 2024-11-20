import requests

# data = {
#     "user" :"alice"
# }

def query_opa(data):
 response = requests.post("http://localhost:8181/v1/data/authenticate/allow?pretty=true&explain=full",json={"input": data})

 print(f"response", response.json())