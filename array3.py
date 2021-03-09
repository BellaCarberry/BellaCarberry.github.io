import array as arr
a = int(input("Range of number: \n"))
if a <= 0:
    exit()
n = arr.array('i' ,[])
for i in range(a):
    n.append(int(input('%d: ' % (i+1))))
print("Array after arranging: ", sorted(n))