x = 'add(3, 5)'
print (x)

for i in range (10):
    if i == 3:
        break
    print(i)

    for j in range (10):
       if j == 7:
        continue
    print('God is still good')
    print(j)

    for k in range (10):
       if k %3 == 0:
          continue
       print(k)