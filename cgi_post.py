#!C:\Users\Arun Kannan\AppData\Local\Programs\Python\Python37\python.exe
# Importing the 'cgi' module
import cgi

print("Content-type: text/html\r\n\r\n")
# Using the inbuilt methods
form = cgi.FieldStorage()
if form.getvalue("name"):
    name = form.getvalue("name")
    print("<h1>Hello " +name+"! Thanks for sharing!</h1><br />")
    
if form.getvalue("happy"):
    print("<p> Yayy! I'm happy too! Keep smiling always  :) </p>")
if form.getvalue("sad"):
    print("<p> Oh no! Why are you sad? Go play for a while. All work and no play makes Jack a dull boy :P</p>")
if form.getvalue("tired"):
    print("<p> Get some rest you've had a long day and you did well today</p>")
if form.getvalue("lazy"):
    print("<p> Get yourself up and get to work. You have miles to go and goals to achieve</p>")
if form.getvalue("angry"):
    print("<p> Control your anger. Don't let your anger control you</p>")
if form.getvalue("afraid"):
    print("<p>Overcome your fear and take charge of your life and your world</p>")
