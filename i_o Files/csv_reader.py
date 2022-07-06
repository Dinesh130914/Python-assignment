import csv

filename = "F:/apicall/bridgelab/CFP/pythonProject/data.csv"
new_file = "F:/apicall/bridgelab/CFP/pythonProject/new.csv"
fields = []

with open(filename, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    fields = next(csv_reader)  # get the Header Names

    with open(new_file, 'w') as new_csv_file:
        csv_writter = csv.writer(new_csv_file, delimiter="\t")

        for row in csv_reader:
            csv_writter.writerow(row)

        new_csv_file.close()
    csv_file.close()
    # Dict of csv reader
with open(filename, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open(new_file,'w') as new_csv:
        fieldnames = ['id', 'Employee Name', 'job tittle', 'Base Pay', 'Over Time ', 'Other pay', 'Total Pay', 'Total Pay benifits']
        csv_writter = csv.DictWriter(new_csv, filednames=fieldnames, delimiter=" /t")
        csv_writter.writeheader()
        for line in new_csv:
            csv_writter.writerow(line)
    new_csv.close()
csv_file.close()