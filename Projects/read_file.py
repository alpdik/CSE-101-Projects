with open("testing.txt", 'r') as file:
    filedata=file.read()
    file.close()

print(filedata)