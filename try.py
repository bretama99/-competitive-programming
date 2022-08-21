s = "12:45:54PM"
first = s[0:2]
second = s[8:10]
time = 0
output = ""
f = ":"
if second == 'PM':
    if s[0:2] == '12':
        time = int(first)
    else:
        time = int(first) + 12
    output = str(time) + s[2:8]
elif second == 'AM':
    if s[0:2] == '12':
        output = "00" + s[2:8]
    else:
        output = s[:8]
print(output)