a=int(input())
b=int(input())
c=int(input())
if (a<b+c and b<a+c and c<a+b) and (a>0 and b>0 and c>0):
    print('true')
else :
    print("false")