f = open("log.txt")

for l in f:
  if (int(l[0] == 0)):
    print l 
  if int(l[3]) % 2 != 0:
    print l
  if (int(l[1]) + int(l[2]) + int(l[3])) % 3 != 0:
    print l 

print "Done."