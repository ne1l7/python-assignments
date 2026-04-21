import csv

def count_rows(file):
    count = 0
    try:
        f = open(file, "r")
        reader = csv.reader(f)

        for line in reader:
            count += 1

        f.close()
        return count

    except:
        print("Error opening file")
        return 0


# main program
name = input("Enter file name: ")
rows = count_rows(name)

if rows != 0:
    print("Total rows are:", rows)
