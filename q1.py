import json

data='{"name":"dimple","age":24,"course":"maths"}'
n=json.loads(data)
print(type(n))
print(type(data))