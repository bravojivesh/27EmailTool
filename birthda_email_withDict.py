import random
import smtplib
import datetime as dt
import csv

my_email="bravojivesh@gmail.com"
my_password="<not putting it here due to security issues>" #need to use gmail settings to get this
dict1={}

todays_date=dt.datetime.now()

current_month=todays_date.month
current_date=todays_date.day


with open ("birthdays.csv", "r") as birthdays:
    data=csv.reader(birthdays)
    next(data) #to skip header row

    for row in data:
        # print (row)
        if int(row[3])==current_month and int(row[4])==current_date:
            message = ""
            to_address=row[1]
            to_name=row[0]

            # print ("the to address is:", to_address, "and the name is:",to_name)

            rand1=random.randint(1,3)
            file_to_open="letter_"+str(rand1)+".txt"
            # print("Random file template is: ",file_to_open)

            with open(file_to_open,"r") as input_file:
                lines=input_file.readlines()
                for line in lines:
                    line=line.replace('[NAME]', to_name)
                    #string is immutable, so you have to store in a variable. Simply using replace will
                    #not work

                    message+=line
                    dict1[to_name] = (to_address,message)
                    # a dictionary with a tuple as a value. The first item in the tuple is the
                    #address. The second is the message sent to the person.
                    #I wanted to create this way so that we can access all the details when needed.

            # print (dict1[to_name][0])


            with smtplib.SMTP("smtp.gmail.com") as connection:
                print ("i am inside email logic here") #debgging
                connection.starttls()
                connection.login(user=my_email,password=my_password)
                connection.sendmail(from_addr=my_email,
                                            to_addrs=dict1[to_name][0],
                                            msg=f"Subject:YOOO\n\n {dict1[to_name][1]}")
                #note: I am using the dictionary indexing for address and message above, which is
                #different from the otheer style (birthday_email.py)
            # using f strings for the message

print(dict1)









