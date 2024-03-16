import random
import smtplib
import datetime as dt
import csv

my_email="bravojivesh@gmail.com"
my_password="<not putting here due to security reasons>" #need to use gmail settings to get this
message=""

todays_date=dt.datetime.now()
todays_day=todays_date.weekday() #monday is 0
current_month=todays_date.month
current_date=todays_date.day
# print(current_month,current_date)
# print (todays_day,todays_date, type(todays_day))

with open ("birthdays.csv", "r") as birthdays:
    data=csv.reader(birthdays)
    next(data) #to skip header row

    for row in data:
        # print (row)
        if int(row[3])==current_month and int(row[4])==current_date:
            # print ("match")
            to_address=row[1]
            to_name=row[0]
            print ("the to address is:", to_address, "and the name is:",to_name)

            rand1=random.randint(1,3)
            file_to_open="letter_"+str(rand1)+".txt"
            # print("Random file template is: ",file_to_open)

            with (open(file_to_open,"r") as input_file):
                lines=input_file.readlines()
                for line in lines:
                    line=line.replace('[NAME]', 'Jose')
                    message+=line

            with smtplib.SMTP("smtp.gmail.com") as connection:
                print ("i am inside email logic here") #debgging
                connection.starttls()
                connection.login(user=my_email,password=my_password)
                connection.sendmail(from_addr=my_email,
                                            to_addrs=to_address,
                                            msg=f"Subject:YOOO\n\n {message}")
            # using f strings for the message











