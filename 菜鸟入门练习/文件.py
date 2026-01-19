with open("test.txt", "w") as file:
    file.write("Hello World!\n第二行内容\n")
with open("test.txt", "r") as file:
    print(file.read())