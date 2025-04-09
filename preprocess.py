import csv

def open_points(file):
    data_list = []
    with open(file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)  
        
        for row in csv_reader:
            data_list.append(row)  

    return data_list