toatal_seconds=int(input("enter the time in second="))
hours=(toatal_seconds//3600)
rem = toatal_seconds%3600
min=rem//60
seconds=rem%60
print(hours)
print(min)
print(round(seconds))