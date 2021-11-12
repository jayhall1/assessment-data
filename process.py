log_file = open("um-server-01.txt")  


def sales_reports(log_file):
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "mon":
            print(line)


sales_reports(log_file)
# the log file opens and connects to the um server then runs a for loop which runs through each day and the rstrip removes any white spaces at the end of a string
# the day = line [0:3] is just looking through the indexes from 0 to 3 at the end of the string if the day is monday then print the data for monday 