#!/usr/bin/python3
for n in range(0, 10):
    for d in range(n + 1, 10):
        if n < d:
print("{:d}{:d}".format(n, d), end='\n' if n == 8 and d == 9 else ", ")
