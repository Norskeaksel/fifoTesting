import time

# Before running the script for the first time, run `mkfifo multimeterData.fifo` in this directory to create the fifo file. 
fifo_name = "multimeterData.fifo"
f = open(fifo_name,'w')
for i in range(5):
  f.write('Hello world!\n')
  f.flush()
  time.sleep(1)
