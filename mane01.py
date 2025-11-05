import urllib.parse

string = [
    "Как стать backend разработчиком", 
    "Привет!"
]

print(urllib.parse.quote(string[1]))
print(urllib.parse.unquote(string[1]))