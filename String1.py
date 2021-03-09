name = str(input("Type your name here: \n"))
w_array = name.split()
print (" ".join(sorted(list(set(w_array)))))