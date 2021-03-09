import array as arr
a = int(input("Range of number: \n"))
if a <= 0:
    exit()
n = arr.array('i' ,[])
for i in range(a):
    n.append(int(input('%d: ' % (i+1))))
print(n)
for i in range(len(n)):
    if n[i] == 2:
        print(n[i], "is even prime")
    elif n[i]% 2 == 0:
        print(n[i], "is even number")
    else:
        print(n[i], "is not even prime")

    