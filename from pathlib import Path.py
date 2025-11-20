from pathlib import Path
import json 
import string
import random
class bank:
    database ='database.json'
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
    def acc_no():
        alpha=random.choices(string.ascii_letters,k=6)
        digit=random.choices(string.digits,k=4)
        id=alpha + digit
        random.shuffle(id)
        return "".join(id)
    
    def create_acc(self):
        d={
            'name':input("enter your name"),
            'email':input("email"),
            "phone no.": int(input("enter your phone number")),
            "pin": int(input("please tell your pin  ")),
            "account no." : bank.acc_no(),
            "balance":0
        }
        print(f"your acc no is {d[ 'account no.']}")
        if len(str(d['phone no.']))!=10:
            print("invalid phone no")
        elif len(str(d['pin']))!=4:
            print("review your pin")

        else :
            bank.data.append(d)
            bank.__update()

    def deposite_money(self)     :
        account_no =  int(input("enter your account no"))
        pin = int(input("enter your pin "))
        user_data = [ i for i in bank.data if account_no!=i['account_no'] and pin!=i['pin']  ]
        if not  user_data :
            print('user not found')
        else :
            amount=int(input("enter amount to be deposite")  )  
            if amount<0 and amount>10000:
                print("invalid")
            else :
                user_data[0]['balance'] +=amount 
                bank.__update()


           



user=bank()

check=int(input(("enter your choice")))
if check==1:
    user.create_acc()  
if check==2:
    user.deposite_money()               