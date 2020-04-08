#!/usr/bin/env python3
import sys

args = len(sys.argv)
if args >= 3:
	str = " ".join(sys.argv[i] for i in range(1, args))
elif args == 2:
	str = sys.argv[1]
else:
	exit(1)
aux = ''
for i in str:
	if i.isupper():	aux += i.lower()
	else:			aux += i.upper()
print (aux[::-1])
exit(0)
