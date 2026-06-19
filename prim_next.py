'''

10.Zero Count Prime Scanner

A banking system checks account numbers.

Write a program to:

- Count zero digits
- Find sum of digits
- Add zero count and sum
- Multiply by smallest digit
- Check whether final result is Prime or Not

Input:
908406
Output:
Zero Count = 2
Sum = 27
Smallest Digit = 0
Final Result = 0
Not Prime'''


n = int(input("enter no. "))
zc=0
sum =0
min = 9 
for i in str(n):
    if int(i)==0:
        zc +=1
    sum = sum+int(i)
    if min >= int(i):
        min = int(i)   
    
print(min)
print(zc)
print(sum)
add = zc + sum
diff = add*min
print(diff)
for i in range(2,diff//2+1):
    if diff%2==0:
        print("not prime ")
else:
    print("prime")        







