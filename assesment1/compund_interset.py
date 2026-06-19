p = int(input("P = ")) 
r = float(input("r ="))
t = int(input("t = "))

ci = p*((1+(r/100))**t)

print(f"Amount = ₹{p+ci}")
print(f"Compound Intrest = ₹{ci}")
