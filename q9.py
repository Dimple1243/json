import json
A = {"shopping_list":
        { 
            "choco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
 }
J = input("enter a item :")
S = int(input("enter the quantity :"))
for i in A :
    for j in A[i]:
        if J in A[i] :
            if j == J and int(A[i][j])>=S:
                print(A[i][j])
                b = int(A[i][j]) - S
                A[i][j] = str(b)
                break
        elif j != J:
          print("Not available")
          break
            
with open("data1.json","w") as write_file:  
    json.dump( A, write_file , indent=4)  
with open("data1.json", "r") as read_file:  
    c =  read_file.read() 
print(c)
print(type(c))
