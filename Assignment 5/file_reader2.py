try:
    f = open("test.txt","r")
    print(f.read())
    f.close()
except:
    print("Error opening file")
