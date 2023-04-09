import sys
import datetime
now=datetime.datetime.now()
time=now.strftime("%d/%m/%y %H:%M:%S")

#For Creating Account
def creatingAccount():
    print("Welcome! For creating the Account we need some details.")
    name=input("Enter your Full Name here for the details:")
    age=int(input("Enter your Age for the details:"))
    mobile=int(input("Enter your Mobile Number for the details:"))
    account=input("Enter your Account Number:")
    login=input("Enter your Login Password:")
    password=input("Enter you Transaction Password:")
    print("Your Account Number is {}.".format(account))
    try:
        file1=open("accountFile","a") # append is the mode which is overcome the problem of the overwrite
    except IOError:
        print("File is not created.");sys.exit()
    lines1=name+ "," + str(age)+ "," + str(mobile)+ "," + str(account)+"," + login + "," + password + "," + "\n"
    file1.writelines(lines1)
    file1.close()
    #the first deposit
    money=input("Please credit opening amount for the account:")
    file2=open(account,"a")
    lines2=time+ "," + "Open" +","+ "Credit"+","+str(money)+","+ str(money)+","+"\n"
    file2.writelines(lines2)
    file2.close()
    
#For Printing Passbook
def passBook():
    print("For Printing Passbook we need some information.")
    list=[]
    list1=[]
    try:
        account=input("Enter your Account Number:")
        login=input("Enter your Login Password:")
        file1=open(account,"r")
        file2=open("accountFile","r")
    except IOError:
        print("File is not open.");sys.exit()
    lines=file1.readline()
    lines2=file2.readline()
    date="Date-Time"
    operation="Operation"
    typing="Type"
    amount="Amount"
    balance="Balance"
    print(date.center(20)+operation.center(30)+typing.center(40)+amount.center(50)+balance.center(60))
    while lines2!="":
        list1=lines2.split(",")
        if list1[-4]==account and list1[-3]==login:
            while lines!="":
                list=lines.split(",")
                for i in range(0,1):
                    try:
                        print(list[i].center(20)+list[i+1].center(30)+list[i+2].center(40)+list[i+3].center(50)+list[i+4].center(60))
                    except IndexError:
                        print("The list is out of Index.");sys.exit()
                lines=file1.readline()
            file1.close()
            break
        else:
            lines2=file2.readline()
    file2.close()

#For Transaction
def transaction(choice):
    if choice==2:
        list=[]
        list1=[]
        print("Welcome! For deposit the amount we need some details.")
        account=input("Please enter your account number:")
        password=input("Please enter your Transaction password:")
        try:
            file1=open("accountFile","r")
            file2=open(account,"r")
        except IOError:
            print("File is not open or not present.");sys.exit()
        line1=file1.readline()
        line2=file2.readline()
        while line1!="":
            list=line1.split(",")
            if list[-4]==account and list[-2]==password:
                amount=int(input("Enter amount which you want to deposit:"))
                while line2!="":
                    list1=line2.split(",")
                    line2=file2.readline()
                file2.close()
                file3=open(account,"a")
                finalAmount=amount+int(list1[-2])
                line3=time+","+"Self"+","+"Credit"+","+str(amount)+","+str(finalAmount)+","+"\n"
                file3.writelines(line3)
                file3.close()
                print("Transaction is successfully completed. Final balance of your account is Rs.{}.".format(finalAmount))
                break
            else:
                line1=file1.readline()
        file1.close()
    elif choice==3:
        list=[]
        list1=[]
        print("Welcome! For withdrawl the amount we need some details.")
        account=input("Please enter your account number:")
        password=input("Please enter your Transaction password:")
        try:
            file1=open("accountFile","r")
            file2=open(account,"r")
        except IOError:
            print("File is not open or not present.");sys.exit()
        line1=file1.readline()
        line2=file2.readline()
        while line1!="":
            list=line1.split(",")
            if list[-4]==account and list[-2]==password:
                amount=int(input("Please enter amount which you want to withdrawl:"))
                while line2!="":
                    list1=line2.split(",")
                    line2=file2.readline()
                file2.close()
                if amount>int(list1[-2]):
                    print("Sorry! You have insufficient funds. Please Try Again!")
                    break
                else:
                    file3=open(account,"a")
                    finalAmount=int(list1[-2])-amount
                    line3=time+","+"Self"+"Debit"+str(amount)+","+str(finalAmount)+","+"\n"
                    file3.writelines(line3)
                    file3.close()
                    print("Transaction is successfully completed. Final balance of your account is Rs.{}.".format(finalAmount))
                    break
            else:
                line1=file1.readline()
        file1.close()
    elif choice==4:
        list=[]
        list1=[]
        list2=[]
        print("Welcome! For transfer the amount we need some details.")
        sender=input("Enter your account number:")
        password=input("Enter your transaction password:")
        reciever=input("Enter account number in which you want to transfer the amount:")
        try:
            file1=open("accountFile","r")
            file2=open(sender,"r")
            file3=open(reciever,"r")
        except IOError:
            print("File is not find or not open.");sys.exit()
        line1=file1.readline()
        line2=file2.readline()
        line3=file3.readline()
        while line1!="":
            list=line1.split(",")
            if list[-4]==sender and list[-2]==password:
                amount=int(input("Enter the amount which you want to transfer:"))
                while line2!="":
                    list1=line2.split(",")
                    line2=file2.readline()
                file2.close()
                while line3!="":
                    list2=line3.split(",")
                    line3=file3.readline()
                file3.close()
                if amount>int(list1[-2]):
                    print("Sorry! You have insufficient Funds. Please Try Again!")
                    break
                else:
                    file4=open(sender,"a")
                    file5=open(reciever,"a")
                    finalAmountSender=int(list1[-2])-amount
                    finalAmountReciever=int(list2[-2])+amount
                    debit=time+","+"Transfer"+","+"Debit"+","+str(amount)+","+str(finalAmountSender)+","+"\n"
                    credit=time+","+"Recived"+","+"Credit"+","+str(amount)+","+str(finalAmountReciever)+","+"\n"
                    file4.writelines(debit)
                    file5.writelines(credit)
                    print("Transaction is successfully completed. Final balance of your account is Rs.{}.".format(finalAmountSender))
                    file4.close()
                    file5.close()
                    break
            else:
                line1=file1.readline()
        file1.close()
                    
#Main function
def main():
    print("For Opening the New Account in the Bank. Please enter=1.")
    print("For deposit the balance in account. Please enter=2.")
    print("For withdrawl amount form the account. Please enter=3.")
    print("For transfer the amount to other. Please enter=4.")
    print("For Printing the Passbook. Please enter=5.")
    choose="Y"
    while choose.upper()!="N":
        choice=int(input("Please enter. What do you want?:"))
        if choice==1:
            creatingAccount()
        elif 2<=choice<=4:
            transaction(choice)
        elif choice==5:
            passBook()
        else:
            print("You choose the Invalid option. Please choose a valid option.")
        choose=input("If you want to exit enter N and if you want to continue press Y:")


if __name__=="__main__":
    main()
