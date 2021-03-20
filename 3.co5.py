import csv
with open('movie1.csv','w',newline='')as file:
    writer=csv.writer(file)
    writer.writerow(["SN","Movie","Rating"])
    writer.writerow([1,"BTS",5])
    writer.writerow([2,"NIGHT",6])
with open('movie1.csv')as csvfile:
    data=csv.reader(csvfile)
    for row in data:
        print(','.join(row))
