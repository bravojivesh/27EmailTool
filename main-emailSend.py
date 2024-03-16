import random
import smtplib
import datetime as dt

my_email="bravojivesh@gmail.com"
my_password="stlbzsdseboaggvi" #need to use gmail settings to get this


todays_date=dt.datetime.now()
todays_day=todays_date.weekday() #monday is 0

# print (todays_day,todays_date, type(todays_day))

if todays_day==5:
    with open("quotes.txt","r") as quotes:
        line=quotes.readlines() #creates a list with each line as an element.
        message=random.choice(line)

    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            print ("i am here") #debgging
            connection.starttls()
            connection.login(user=my_email,password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="hamal.jivesh@gmail.com",
                                msg=f"Subject:YOOO\n\n {message}")
            #using f strings for the message

    except:
        print ("Something is wrong")
    else:
        print ("Email sent brow")



