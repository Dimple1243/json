import json
x={
    "Name": "Divya",
    "Designation": "CEO of  Khurana Industries",
    "Gender":"Female",
    "Age": "29"
    }
with open("data.txt","w") as write_file:  
    json.dump( x, write_file , indent=4)  
with open("data.txt", "r") as read_file:  
    c =  read_file.read() 
print(c)

