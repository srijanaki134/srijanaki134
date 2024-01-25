#!C:\Python312\python.exe

import cgi
import mysql.connector

print("Content-Type:text/html\r\n\r\n")
print("<html>")
print("<body>")

form=cgi.FieldStorage()
fName=form.getvalue("Name")
fNumber=form.getvalue("Number")
fPickup=form.getvalue("Pickup")
fCname=form.getvalue("Cname")
fDestination=form.getvalue("Destination")
print("<br><center><h2>Thank you for Booking<a href='/cabBooking'><br>Back to Home</h2></center>")
print("<h1>",fName,fNumber,fPickup,fCname,fDestination,"</h1>")

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="booking"
    )
mycursor=mydb.cursor()
sql="INSERT INTO user(Name,Number,Pickup,Cname,Destination)VALUES(%s,%s,%s,%s,%s)"
val=(fName,fNumber,fPickup,fCname,fDestination)
mycursor.execute(sql,val)
mydb.commit()
print("</body>")
print("</html>")



