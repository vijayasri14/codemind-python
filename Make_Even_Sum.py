n=int(input())
lst=map(int,input().split())
s=0
for i in lst:
    s=s+i
if s%2==0:
    print("1")
else:
    print("0")