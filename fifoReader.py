fifo_name = "multimeterData.fifo"

for line in open(fifo_name,'r'):
    print(line[:-1]) # Fifo writer generates an extra newline, which we want to exclude here with the :-1
