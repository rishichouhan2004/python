amount=int(input("enter the amount="))
hundred=amount//100
fifty=(amount%100)//50
tens=(amount%50)//10
print(f"{hundred} {fifty} {tens}")
