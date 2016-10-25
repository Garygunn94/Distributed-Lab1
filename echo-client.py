import urllib

x = "hello"
while x != "xxxxxx":
    
    data = urllib.urlencode({"message":x})

 
    u = urllib.urlopen("https://www.scss.tcd.ie:80/echo.php?%s" % data)
    
    print u.read()
    x = raw_input("Enter a message to send to echo server. Enter 'xxxxxx' to exit\n")
    
