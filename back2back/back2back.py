from textwrap import wrap

s = "##########S6#6###6#######6##########4444%U6666%%%%%%%%%%%%&%%%%%%&###&###################&###&44#####&66%%%%%%%%%%&4######&4#&%&6&4##&%%%%%&####&6&6################&%%%%%%%%%%%%%%%%&44###&%%%%%&66############################&%%%%%%%%&%%%%%%%%%%%%%%%&##########&########&4&4##&%&6&4##&%%%%%&####&6&6%%%%%%%%%%%%%&44%&66%%%%%%%%%%&#############&"

current = s[0]
result = "1"
for c in s:
    if c == current:
        result+="0"
    else:
        result += "1"
        current = c

print result
