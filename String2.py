string = str(input("Type your sentence here: \n"))
cnt = 0
check = 0
w_array = string.split()
for x in w_array:
    if (x.islower()):
        cnt = cnt + 1
    else:
        check = check + 1

print ("Right: " + str(check))
print ("Wrong: " + str(cnt))