f = open('MultimeterData.txt', 'w+')
for i in range(5):
  f.write('0.0V\n')
  f.flush()
  time.sleep(1)
