f = open('index.html','w')

message = """<html>
<head></head>
<body><p>Hello World!</p>
<p>New Text</p>
<p>@5 wala commit</p>
<p>@5.10 wala commit</p>
</body>
</html>"""

f.write(message)
f.close()
