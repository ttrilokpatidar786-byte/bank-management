from pathlib import Path
import json
import random
import string
class bank: 
    database='database.json'
    data=[]

    try: 
        if Path(database).exists():
            with open(database) as fs:
                data= json.loads(fs.read())

        else :
            print("sorry we are facing an issue")

    except Exception as err:
        print(f"an error occured as {err}")         

    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(cls.data)) 

    @staticmethod
    def __accountno():
         alpha = random.choices(string.ascii_letters , k=5) 
         digits = random.choices(string.digits , k=4)    
         id= alpha + digits 
         random.shuffle(id)
         return "".join(id)  
            
                      
    def createaccount(self):
        d={
        
           "name":input("please tell your name= "),
           
            "email": input("tell your email"),

            "phone no.": int(input("enter your phone number")),
            "pin": int(input("please tell your pin  ")),
            "account no." : bank.__accountno(),
            "balance":0
        }
        print(f"please note dawn your account no.{d['account no.']}")
        
        
        if len(str(d['pin'])) !=4:
            print("please review your pin")

        elif len(str(d["phone no."])) != 10 :
            print("check your input no.")   

        else :
            bank.data.append(d)
            bank.__update()

    def deposite_money(self):
        accNO=input("enetr your acc no")
        pin=int(input("enter your pin"))
        user_data=[i for i in bank.data if i['account no.']==accNO and i['pin']==pin  ]
        if not user_data:
            print(("user not found"))
        else :
            amount=int(input("enter amount to be credited")) 
            if amount <=0:
                print("invalid amount")
            elif amount>10000:
                print("grater then 10000") 
            else :
                user_data[0]['balance']+=amount
                bank.__update()
                print("amount credited")          






    def withdraw_money(self):
        accNO=input("enetr your acc no")
        pin=int(input("enter your pin"))
        user_data=[i for i in bank.data if i['account no.']==accNO and i['pin']==pin  ]
        if not user_data:
            print(("user not found"))
        else :
            amount=int(input("enter amount to be withdraw")) 
            if amount <=0:
                print("invalid amount")
            elif amount>10000:
                print("grater then 10000") 
            else :
                if user_data[0]['balance']<amount:
                    print("insufficient balance")
                else :

                    user_data[0]['balance']-=amount
                    bank.__update()
                    print("amount debited")    

    def details(self):
        accNO=input("enetr your acc no")
        pin=int(input("enter your pin"))
        user_data=[i for i in bank.data if i['account no.']==accNO and i['pin']==pin  ]
        if not user_data:
            print("user not found")
        else :
            for i in user_data[0]:
                print(i,user_data[0][i])  


    def update_details(self):
        accNO=input("enetr your acc no")
        pin=input("enter your pin")
        user_data=[i for i in bank.data if i['account no.']==accNO and i['pin']==pin  ]
        if not user_data:
            print("user not found")
        else :
            print(" you cannot change acc no. ")    
            print("naw update your details and skip it if you don't want to update ")
            # name,email,phone,pin
            new_data={
        
            'name':input("enter your new name:"),
            'email':input("enter your new email:"),
            'phone NO.':input("enter your new no.:"),
            'pin':input("enter new pin:")
            }
            # we have to handle skiped value
            for i in new_data:
                if new_data[i]=="":
                    new_data[i]=user_data[0][i]# yaha [0]likhna hi kyu h jab user_data me ek hi user h becaUSE user data ek list h
                continue 

            new_data['accNO'] = user_data[0]['accNO']
            new_data['balance']=user_data[0]['balance']
            # we have to update new data to database

            for i in user_data:
                if   user_data[0][i]==new_data[i]:
                    continue
                else: # same chij nahi ho gai ye ??
                    if new_data[i].isnumeric():
                        user_data[0][i]=new_data[i]
                    else:
                        user_data[0][i]=new_data[i]
            bank.__update()     
            print("update successfully")   

    def delete_user(self):
        accNO=input("enetr your acc no")
        pin=input("enter your pin")
        user_data=[i for i in bank.data if i['account no.']==accNO and i['pin']==pin  ]
        if not user_data:
            print("user not found")
        else :
            for i in bank.data:
                if i["account no."] =='accNo' and i['pin']=='pin':
                    bank.data.remove(i)     
                bank.__update() 
                print("deleted")   
                       
            
                


    
user = bank()
print("press 1 for creating account")
print("press 2 for deposit money")
print("press 3 to withdrow money")
print("press 4  for details")
print("press 5 for updating details")
print("press 6 for deleting account")

check= int(input("enter your choice= "))

if check==1:
    user.createaccount()
elif check==2:
    user.deposite_money()
elif check==3:
    user.withdraw_money()  
elif check==4:
    user.details()
elif check==5:
    user.update_details() 
elif check==6:
    user.delete_user()       





    # 5
    # 6
    # dillat h 