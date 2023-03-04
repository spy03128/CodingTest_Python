import sys
def pow(p,n):
    if n==1:
        return p
    tmp = pow(p,n//2)
    if n%2==0:
        return tmp*tmp%1000000007
    else:
        return tmp*tmp*p%1000000007

k,p,n=map(int,sys.stdin.readline().split())
x = pow(p,10*n)
print(k*x%1000000007)