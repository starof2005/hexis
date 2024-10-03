# hexis
code to fnd a number is prime or not

l=int(input("enter a number"))
y=0
if l==0 or l == 1:
    y=1

elif l>1:
    for i in range(2,l):
        if l%i == 0:
            y=1
            break
else:
    y=0


if y ==0:
     print("prime")
else:
    print("prime factors are : ")

    h =[ ]
    for j in range (2,l+1):
        while l%j==0:
         h.append(j)
         l=l/j
    print(h)

