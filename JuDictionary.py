import csv
data_list = []
with open("data_candidates_coordinates.csv") as csv_file:
    data = csv.reader(csv_file, delimiter=' ’)
    header = list(next(data))
    n = len(header)
    for row in data:
        object_dictionary = {}
        for i in range(n):
            object_dictionary[header[i]] = row[i]
        data_list.append(object_dictionary)
print(data_list[0])