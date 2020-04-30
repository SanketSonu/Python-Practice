with open('ex_file.txt', 'w') as f:                                    #Writing to a file.
    f.write("I'm writing this line using Python Program.")

with open('ex_file.txt', 'r') as f:
    f_contents = f.read()                     #This will read the content of the file.
    print(f_contents)

with open('ex_file.txt', 'r') as f:
    f_contents_list = f.readlines()                     #This will read the content and display in list.
    print(f_contents_list)
