
std={1:["akash",75,85,77],2:["akshay",78,90,75],4:["richa",87,84,90],3:["akansha",88,85,89]}
inp="n"
'''while(inp!="y"):
   inp=input("enter y to exit the insert mode")
   if inp is not "y":
      a=input("enter rollno.")
      b=input("enter english")
      c=input("enter maths.")
      d=input("enter sci. marks ")
      std.update({a:[b,c,d]})

f=open("std.csv","w")
for keys in std.keys():
   f.write((str(keys)+","+std[keys][0]+","+str(std[keys][1])+","+str(std[keys][2])+","+str(std[keys][3])+"\n"))
f.close()   
  '''    
with open("std.csv","r") as f:
   std=f.read()
std=std.split("\n")
std.pop()   
std_di={}

for rw in std:
   rw=rw.split(",")
   per=(int(rw[2])+int(rw[3])+int(rw[4]))/3
   
   print(per)
   std_di.update({rw[0]:[rw[1],rw[2],rw[3],rw[4],per   ]})
print(std_di)

import json
'''with open("std.json","w") as f:
   json.dump(std_di,f)
'''

with open("std.json","r") as f:
   std_di=json.load(f)

print(std_di)
## store data in db







