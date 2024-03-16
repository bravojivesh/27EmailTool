import pandas

data=pandas.read_csv("birthdays.csv")

dict={row["name"]:row.email for index1,row in data.iterrows()}
print (dict)