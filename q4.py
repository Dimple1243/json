import json
x={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
y=json.dumps(x, indent=1, sort_keys=True) 
print(y)
print(type(y))
