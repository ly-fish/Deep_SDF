import csv

with open('/home/liangyue/project/yly/DeepSDF/examples/chairs/Evaluation/1000/chamfer.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    
    for row in csv_reader:
        print(row)