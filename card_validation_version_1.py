
#card  = [4,6,1,9,3,3,0,1,1,0,4,4,4,4,9,0]
card = [4,4,1,7,1,2,3,4,5,6,7,8,9,1,1,3]
print(card)

i=0
j=1
c=[]
for x in card:
    a=card[i]*2
    b=card[j]
    if a > 9:
        a1=int(a / 10)
        c.append(a1)
        a2 = a % 10
        c.append(a2)
        a=0

    c.append(a)
    c.append(b)
    i=i+2
    j=j+2

    if i>=16:
        break
    if j>=16:
        break
print("Step 1")
print(c)
print("Step 2")
print(sum(c))
sum_c = sum(c)
if sum_c%10 == 0:
    print("\nCREDIT CARD")
else:
    print("\nNot a CREDIT CARD")
#credit card check over
print("\n********************************\n")
print(card)
i=0
j=1
c=[]
for x in card:
    a=card[i]
    b=card[j]*2

    c.append(a)
    c.append(b)
    i=i+2
    j=j+2

    if i>=16:
        break
    if j>=16:
        break
print("Step 1")
print(c)
print("Step 2")
print(sum(c))
sum_c = sum(c)
if sum_c % 5 == 0:
    print("\nDEBIT CARD")
else:
    print("\nNot a DEBIT CARD")

#debit card check over

if card[0] == 4:
    print("\nVISA CARD")
elif card[0] == 5:
    print("\nMASTER CARD")
elif card[0] == 6:
    print("\nRUPAY/DISCOVER CARD")