log_file = open("um-server-01.txt")
#opening file "um-server-01.txt"

def sales_reports(log_file):
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Mon":
            print(line)

#creating a for loop, if statement, & removing elements

sales_reports(log_file)

#displaying the results
