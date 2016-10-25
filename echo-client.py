import urllib

data = urllib.urlencode({"message":"hello world"})
 
u = urllib.urlopen("http://localhost:8000/echo-server.php/?%s" % data)

print u.read()