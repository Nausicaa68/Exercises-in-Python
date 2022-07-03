x = int(input("Entrez le dividande : "))
y = int(input("Entrez le diviseur : "))
quotient = 0
xtotal = x

while x >= y:
    x= x - y
    quotient += 1

reste = xtotal - (quotient*y)

print("Q =", quotient)
print("R =",reste)
