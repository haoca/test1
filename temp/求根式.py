from decimal import Decimal
c =input('请输入:')
c =Decimal(c)
a = c/2
n=0
print(a)
while abs(a*a-c)>0.01:
    b = a
    n = n+1
    if n == 20:
        break
    if a*a > c:
        # b = a
        a = a/2
        # b = a
    if a*a < c:
        a = (b+a)/2
    # a = a/2
    # a = Decimal(c)
    # b = Decimal('60.0')
    # a + b
    # Decimal('6.3')
    print(a)
# 6.3
# (a + b) == Decimal('6.3')
# True