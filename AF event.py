import random
l=['Tarun','Hari Om ','Naveen Rathore','Sushant','Jathin','Akash Batchu','Meher','Kunal','Arjun','Abhimanyu','Shruti ','Aastha','Ayesha','Shashidhar ','Shishir','Kajal','Pranav']
l2=len(l)
print("\nCalling People\n")
while l!=[] :
    if len(l)=l2-3:
        print("\nMinor Event\n")
    elif len(l)=l2-9:
        print("\nMajor Event\n")
    a=l[random.randint(0,len(l)-1)]
    l.remove(a)
    print(a)
input()
