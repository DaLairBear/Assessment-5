#opens um-server-01.txt and sets it equal to the value log_file to be used.
log_file = open("um-server-01.txt")

#declaration of a functions passing in log_file
def sales_reports(log_file):
    #for loop for looping through each line of data in um-server-01.txt
    for line in log_file:
        #strips any whitespace characters from the end of the strings
        line = line.rstrip()
        #sets day equal to the first 3 indexes of the string
        day = line[0:3]
        #checking if the beginning of the string is equal Tue originally, modifided to reflect Mon
        if day == "Mon":
            #if the condition is met printing that line of data in um-server-01.txt
            print(line)

#telling the function to run
#sales_reports(log_file)

def orders_over_ten(log_file):
    for line in log_file:
        value = line.split(' ')
        if int(value[2]) > 10:
            print(line)

orders_over_ten(log_file)
