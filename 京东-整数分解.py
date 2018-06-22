


def fenjie(s):
    t="No"
    for i in range(2,s+1):
        if i%2==0:
            if s%i==0:
                t=s/i
                if t%2==1:
                    break
            else:
                return t
    return t



t=int(raw_input())
list=[]
for i in range(0,t):
    s=int(raw_input())
    list.append(s)


for item in list:
    if fenjie(item)=="No":
        print "No"
    else:
        print (str(fenjie(item))+" "+str(item/fenjie(item)))
