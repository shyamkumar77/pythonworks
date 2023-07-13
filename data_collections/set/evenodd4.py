# given set create even and odd set

s={1,2,3,4,56,7,8,9,5,488,78}
even=set()
odd=set()

for i in s:
    if(i%2==0):
        even.add(i)
    else:
        odd.add(i)

print("even set",even)
print("odd set",odd)