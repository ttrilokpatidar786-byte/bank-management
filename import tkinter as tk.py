import tkinter as tk
from tkinter import messagebox, simpledialog
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
                data= json.loads(fs.read_text())

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
        id_list = list(id)
        random.shuffle(id_list)
        return "".join(id_list)  

    def createaccount(self, name, email, phone, pin):
        d={
           "name": name,
           "email": email,
           "phone no.": int(phone),
           "pin": int(pin),
           "account no." : bank.__accountno(),
           "balance":0
        }
        print(f"please note dawn your account no.{d['account no.']}")
        # Validation
        if len(str(d['pin'])) !=4:
            return "Pin must be 4 digits."
        elif len(str(d["phone no."])) != 10:
            return "Phone number must be 10 digits."
        else:
            bank.data.append(d)
            bank.__update()
            return f"Account created successfully. Your account no: {d['account no.']}"

    def deposite_money(self, accNO, pin, amount):
        user_data=[i for i in bank.data if i['account no.']==accNO and i['pin']==pin  ]
        if not user_data:
            return "User not found."
        else:
            if amount <=0:
                return "Invalid amount."
            elif amount > 10000:
                return "Amount exceeds limit."
            else:
                user_data[0]['balance']+=amount
                bank.__update()
                return "Amount credited successfully."

    def withdraw_money(self, accNO, pin, amount):
        user_data=[i for i in bank.data if i['account no.']==accNO and i['pin']==pin  ]
        if not user_data:
            return "User not found."
        else:
            if amount <=0:
                return "Invalid amount."
            elif amount > 10000:
                return "Amount exceeds limit."
            elif user_data[0]['balance']<amount:
                return "Insufficient balance."
            else:
                user_data[0]['balance']-=amount
                bank.__update()
                return "Amount debited successfully."

    def details(self, accNO, pin):
        user_data=[i for i in bank.data if i['account no.']==accNO and i['pin']==pin  ]
        if not user_data:
            return "User not found."
        else:
            return user_data[0]

    def update_details(self, accNO, pin, name, email, phone, new_pin):
        user_data=[i for i in bank.data if i['account no.']==accNO and i['pin']==pin  ]
        if not user_data:
            return "User not found."
        else:
            # Update details
            if name != "":
                user_data[0]['name'] = name
            if email != "":
                user_data[0]['email'] = email
            if phone != "":
                user_data[0]['phone no.'] = int(phone)
            if new_pin != "":
                if len(new_pin) ==4 and new_pin.isdigit():
                    user_data[0]['pin'] = int(new_pin)
                else:
                    return "Invalid new pin."
            bank.__update()
            return "Details updated successfully."

    def delete_user(self, accNO, pin):
        user_data=[i for i in bank.data if i['account no.']==accNO and i['pin']==pin  ]
        if not user_data:
            return "User not found."
        else:
            bank.data.remove(user_data[0])
            bank.__update()
            return "User deleted successfully."

# GUI part
class BankGUI:
    def __init__(self, root):
        self.bank_obj = bank()
        self.root = root
        self.root.title("Banking System")
        self.create_widgets()

    def create_widgets(self):
        btn_create = tk.Button(self.root, text="Create Account", command=self.create_account)
        btn_deposit = tk.Button(self.root, text="Deposit Money", command=self.deposit_money)
        btn_withdraw = tk.Button(self.root, text="Withdraw Money", command=self.withdraw_money)
        btn_details = tk.Button(self.root, text="View Details", command=self.view_details)
        btn_update = tk.Button(self.root, text="Update Details", command=self.update_details)
        btn_delete = tk.Button(self.root, text="Delete Account", command=self.delete_account)

        btn_create.pack(pady=5)
        btn_deposit.pack(pady=5)
        btn_withdraw.pack(pady=5)
        btn_details.pack(pady=5)
        btn_update.pack(pady=5)
        btn_delete.pack(pady=5)

    def create_account(self):
        name = simpledialog.askstring("Name", "Enter your name:")
        email = simpledialog.askstring("Email", "Enter your email:")
        phone = simpledialog.askstring("Phone", "Enter your 10-digit phone number:")
        pin = simpledialog.askstring("Pin", "Enter a 4-digit pin:")

        if None in (name, email, phone, pin):
            messagebox.showinfo("Cancelled", "Operation cancelled.")
            return

        result = self.bank_obj.createaccount(name, email, phone, pin)
        messagebox.showinfo("Result", result)

    def deposit_money(self):
        accNO = simpledialog.askstring("Account No", "Enter your account number:")
        pin = simpledialog.askstring("Pin", "Enter your pin:")
        amount_str = simpledialog.askstring("Amount", "Enter amount to deposit:")
        if None in (accNO, pin, amount_str):
            messagebox.showinfo("Cancelled", "Operation cancelled.")
            return
        try:
            amount = int(amount_str)
        except:
            messagebox.showerror("Error", "Invalid amount.")
            return
        result = self.bank_obj.deposite_money(accNO, int(pin), amount)
        messagebox.showinfo("Result", result)

    def withdraw_money(self):
        accNO = simpledialog.askstring("Account No", "Enter your account number:")
        pin = simpledialog.askstring("Pin", "Enter your pin:")
        amount_str = simpledialog.askstring("Amount", "Enter amount to withdraw:")
        if None in (accNO, pin, amount_str):
            messagebox.showinfo("Cancelled", "Operation cancelled.")
            return
        try:
            amount = int(amount_str)
        except:
            messagebox.showerror("Error", "Invalid amount.")
            return
        result = self.bank_obj.withdraw_money(accNO, int(pin), amount)
        messagebox.showinfo("Result", result)

    def view_details(self):
        accNO = simpledialog.askstring("Account No", "Enter your account number:")
        pin = simpledialog.askstring("Pin", "Enter your pin:")
        if None in (accNO, pin):
            messagebox.showinfo("Cancelled", "Operation cancelled.")
            return
        result = self.bank_obj.details(accNO, int(pin))
        if isinstance(result, dict):
            details = "\n".join(f"{k}: {v}" for k, v in result.items())
            messagebox.showinfo("Account Details", details)
        else:
            messagebox.showerror("Error", result)

    def update_details(self):
        accNO = simpledialog.askstring("Account No", "Enter your account number:")
        pin = simpledialog.askstring("Pin", "Enter your pin:")
        if None in (accNO, pin):
            messagebox.showinfo("Cancelled", "Operation cancelled.")
            return
        name = simpledialog.askstring("Name", "Enter new name (leave blank to skip):")
        email = simpledialog.askstring("Email", "Enter new email (leave blank to skip):")
        phone = simpledialog.askstring("Phone", "Enter new phone (leave blank to skip):")
        new_pin = simpledialog.askstring("Pin", "Enter new pin (leave blank to skip):")
        result = self.bank_obj.update_details(accNO, int(pin), name or "", email or "", phone or "", new_pin or "")
        messagebox.showinfo("Result", result)

    def delete_account(self):
        accNO = simpledialog.askstring("Account No", "Enter your account number:")
        pin = simpledialog.askstring("Pin", "Enter your pin:")
        if None in (accNO, pin):
            messagebox.showinfo("Cancelled", "Operation cancelled.")
            return
        result = self.bank_obj.delete_user(accNO, int(pin))
        messagebox.showinfo("Result", result)

if __name__ == "__main__":
    root = tk.Tk()
    app = BankGUI(root)
    root.mainloop()