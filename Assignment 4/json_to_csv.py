import csv

def convert(json_list, filename):
    f = open(filename, "w", newline="")

    keys = json_list[0].keys()
    writer = csv.DictWriter(f, fieldnames=keys)

    writer.writeheader()

    for item in json_list:
        writer.writerow(item)

    f.close()
    print("File saved successfully")


# main
data = [
    {"name": "Amit", "age": 20, "city": "Pune"},
    {"name": "Riya", "age": 19, "city": "Mumbai"},
    {"name": "Karan", "age": 21, "city": "Delhi"}
]

convert(data, "data.csv")
