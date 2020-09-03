import random
l=['Tarun','Hari Om ','Cyril ','Naveen Rathore','Sushant','Jathin','Akash Batchu','Meher','Kunal','Arjun','Abhimanyu','Shruti ','Aastha','Ayesha','Shashidhar ','Shishir','Kajal','Pranav']
print(len(l))
while l!=[] :
    a=l[random.randint(0,len(l)-1)]
    l.remove(a)
    print(a)
print(l)
input()
