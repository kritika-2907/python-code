lst=[]
def c_to_f(temp):
   fahrenheit=(temp*1.8)+32
   return fahrenheit    
def f_to_c(temp):        
    celsius=(temp-32)/1.8
    return celsius
while(True):
    ch=int(input("MENU: \n1.C to F \n2.F to C \n3.history \n4.Exit \nEnter your choice: "))

    if ch==1:
        temp=int(input("Enter the value of the temperature in celsius: \n"))
        print("The temperature in Fahrenheit is: ",c_to_f(temp))
        lst.append((str(temp)+" C ",str(c_to_f(temp))+" F"))
    elif ch==2:
        temp=int(input("Enter the value of the temperature in Fahrenheit: \n"))
        print("The temperature in Fahrenheit is: ",f_to_c(temp))
        lst.append((str(temp)+" F",str(f_to_c(temp))+" C"))
    elif ch==3:
        print(tuple(lst))
    else:
        break

