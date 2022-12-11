def onescompliment(a):
    b = list()
    for i in range(len(a)):
        if(a[i]=="0"):
            b.append("1")
        else:
            b.append("0")
    return b

def binadd(a,b):
    while(len(a)<len(b)):
        a.insert(0,"0")
    while(len(b)<len(a)):
        b.insert(0,"0")
     
    carry=0
    a = a[::-1]
    b = b[::-1]
    ans=list()
    
    for i in range(len(a)):
        if((a[i]=="0" and b[i]=="1") or (a[i]=="1" and b[i]=="0")):
            if carry==0:
                ans.append("1")
                carry=0
            elif carry==1:
                ans.append("0")
                carry=1
        elif(a[i]=="0" and b[i]=="0"):
            if carry==0:
                ans.append("0")
                carry=0
            elif carry==1:
                ans.append("1")
                carry=0
        elif(a[i]=="1" and b[i]=="1"):
            if carry==0:
                ans.append("0")
                carry=1
            elif carry==1:
                ans.append("1")
                carry=1
    ans = ans[::-1]
    return ans

def shift(c):
    ans = list()
    ans.append(c[0])
    for i in range(1,len(c)):
        ans.append(c[i-1])
    return ans

print("Enter the multiplicant: ")
m = list(map(str, input().split()))
print("Enter the multiplier: ")
q = list(map(str, input().split()))
n = max(len(m),len(q))
one = ["1"]
if(q[0]=="1"):
    temp = list()
    for i in range(1,n):
        temp.append(q[i])
    temp = binadd(onescompliment(temp),one)
    temp.insert(0,"1")
    q=temp

a = ["0"]*n
minus_m = binadd(onescompliment(m),one)
q1 = "0"
combined = a+q
combined.append(q1)
# print(shift(combined,n))
count = n

while(count!=0):
    if(q[-1]=="1" and q1 == "0"):
        a = binadd(a,minus_m)
        combined = a+q
        combined.append(q1)
        ans = shift(combined)
        temp1=list()
        temp2=list()
        for i in range(0,n):
            temp1.append(ans[i])
        for i in range(n,2*n):
            temp2.append(ans[i])
        a = temp1
        q = temp2
        q1= ans[-1]
        count-=1
    elif(q[-1]=="0" and q1 == "1"):
        a = binadd(a,m)
        combined = a+q
        combined.append(q1)
        ans = shift(combined)
        temp1=list()
        temp2=list()
        for i in range(0,n):
            temp1.append(ans[i])
        for i in range(n,2*n):
            temp2.append(ans[i])
        a = temp1
        q = temp2
        q1= ans[-1]
        count-=1
    else:
        combined = a+q
        combined.append(q1)
        ans = shift(combined)
        temp1=list()
        temp2=list()
        for i in range(0,n):
            temp1.append(ans[i])
        for i in range(n,2*n):
            temp2.append(ans[i])
        a = temp1
        q = temp2
        q1= ans[-1]
        count-=1

res = a+q
if(res[0]=="1"):
    res = binadd(onescompliment(res),one)
    print("Product: negative ",*res)
else:
    print("Product: ",*res)