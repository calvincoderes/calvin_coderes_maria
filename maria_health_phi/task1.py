x = 15
num1 = 1
num2 = 0
if x % 3 and x % 5 and c > 0:
    print('0')
    for i in range(0, x):
        nxt = num1 + num2
        num1 = num2
        num2 = nxt
        print(nxt)
elif x % 3 == 0 and x % 5 == 0:
    print('Maria Health')
else:
    if x % 3 == 0:
      print('Maria')

    if x % 5 == 0:
      print('Health')
