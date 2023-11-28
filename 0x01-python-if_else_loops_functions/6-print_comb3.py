#!/usr/bin/python3
for nm in range(0, 10):
    for dg in range(nm + 1, 10):
        if nm < dg:
print("{:d}{:d}".format(nm, dg), end='\n' if nm == 8 and dg == 9 else ", ")
