from decimal import Decimal
while 1:
    c =input('请输入U，得到I\n')
    a = Decimal(c)
    b = Decimal('60.0')
    # a + b
    # Decimal('6.3')
    print(b/a)
# 6.3
# (a + b) == Decimal('6.3')
# True