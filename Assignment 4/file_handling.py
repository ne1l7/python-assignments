def file_task():
    # writing
    f = open("sample.txt", "w")
    f.write("Hello this is line 1\n")
    f.write("Hello this is line 2\n")
    f.close()
    print("File created")

    # reading
    f = open("sample.txt", "r")
    data = f.read()
    print("\nFile content:")
    print(data)
    f.close()

    # appending
    f = open("sample.txt", "a")
    f.write("This is new added line\n")
    f.close()
    print("\nData added")

    # reading again
    f = open("sample.txt", "r")
    print("\nUpdated content:")
    print(f.read())
    f.close()


file_task()
