import smtplib

my_email="bravojivesh@gmail.com"
my_password="yadjazzbmlmtuhha"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email,password=my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="hamal.jivesh@gmail.com",
                        msg="Subject:YOOO\n\nHola Jose! Wats popping dawg?")