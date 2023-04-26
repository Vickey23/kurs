zdanie = input("Podaj zdanie: ")
s = zdanie.split()[::-1]
l = []
for i in s:
    l.append(i)
print(" ".join(l))