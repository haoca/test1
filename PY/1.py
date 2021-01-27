#int m
# hello how are you?
while True:
  ten=None
  
  # ten=int(input("x:"))
  ten=(input("x:"))
  if type(ten)==int:
    print('it is a digit')
  #m=int(input())
  else:
    print('it is not a digit')
  a=(type(ten)==int)
  print(type(ten),a)
  
