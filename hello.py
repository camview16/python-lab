f = open('index.html','w')

message = """<html>
<head></head>
<body><p>Hello World!</p>
<p>New Text</p>
</body>
</html>"""

f.write(message)
f.close()
