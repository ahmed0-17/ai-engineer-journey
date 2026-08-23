age=int(input("Enter your age : "))

if age>=18:
    print("adult")

else :
    print("minor")   





number=int(input("Enter a number : "))

if number%2==0:
    print (f"{number} is even")

else:
    print(f"{number} is odd")    




marks=int(input("Enter marks :"))

if marks >=80:
    print("A")
elif marks>=70:
    print("B")
elif marks>=60:
    print("C")    
elif marks>=50:
    print("D")
else:
    print("Fail")        





username=input("Enter your username : ")   
password=int(input("Enter your pssword : "))

if username=="admin" and password==1234 :
    print("Login Successful")


else:
    print("Invalid username or password")



daily_study_hours=int(input("Enter study hours : "))

if daily_study_hours>=4:
    print("Excellent Consistency")

elif daily_study_hours>=2:
    print("Good but improve")

elif daily_study_hours>=1:
    print("need more practice")
else:
    print("No study today")