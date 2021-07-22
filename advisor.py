#!C:\Users\Arun Kannan\AppData\Local\Programs\Python\Python37\python.exe

  
print("Content-type: text/html\r\n\r\n")
print("<html><body>")
print("<h1> Betterment advisor! </h1>")

  

  
# Using HTML input and forms method
print("<form method='post' action='cgi_post.py'>")
print("<p>Name: <input type='text' name='name' /></p>")
print("<input type='checkbox' name='happy' /> Happy")
print("<input type='checkbox' name='sad' /> Sad")
print("<input type='checkbox' name='tired' /> Tired")
print("<input type='checkbox' name='lazy' /> Lazy")
print("<input type='checkbox' name='angry' /> Angry")
print("<input type='checkbox' name='afraid' /> Afraid  <br>")
print("<br><input type='submit' value='Submit' />")
print("</form")
print("</body></html>")
