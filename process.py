log_file = open("um-server-01.txt")
#opening file "um-server-01.txt"

def sales_reports(log_file):
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Tue":
            print(line)

#creating a for loop, if statement, & editing/deleting file data

sales_reports(log_file)

#displaying results 