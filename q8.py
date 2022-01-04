import json
a={ 
     "emp1":{ "name":"Anjali",
       "Designation":"programmer",
       "Age":"34",
       "salary":"24000",
         },

    "emp2":
      { "name":"Ankita",
        "Designation":"Trainee",
        "Age":"24",
        "salary":"20000" ,
        },

 
    "emp3":
       { "name":"Rupa",
         "Designation":"HR",
         "Age":"25",
         "salary":"40000",
         },


    "emp4":
       { "name":"Divya",
         "Designation":"Manager",
         "Age":"29",
       }
 }
with open("data2.txt","w") as write_file:  
    json.dump( a, write_file , indent=4)  
with open("data2.txt", "r") as read_file:  
    c =  read_file.read() 
print(c)
