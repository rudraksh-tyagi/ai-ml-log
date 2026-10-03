print("Hello, \"World!\"")
# \ -> escape character
print('Hello, "World!"')
s = "Hello, World!"
print(s[0] + s[1] + s[2] + s[3] + s[4] + s[5] + s[6] + s[7] + s[8] + s[9] + s[10] + s[11]  + " this is a string")  
print(s.lower())
print(s.upper())
print(s.replace("World", "Python"))
print(s.upper().isupper())
print(len(s))
print(s.index("W"))
print(s[0:5])  # slicing
print(s[7:12])  # slicing
print(s[0:12:2])  # slicing with step
# slicing ->[start:end:step]