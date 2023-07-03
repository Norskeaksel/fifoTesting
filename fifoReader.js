const fs = require('fs');
const path = require('path');

const fifoPath = path.resolve('', 'multimeterData.fifo')

const fifo = fs.createReadStream(fifoPath);
fifo.setEncoding('utf8')
fifo.on('data', data => {
  console.log(data.slice(0, -1)) ;
});
