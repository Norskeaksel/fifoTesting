file = open('MultimeterData.txt', 'r')
while True:
    line = file.readline()
    if line:
        print(line, end='')
