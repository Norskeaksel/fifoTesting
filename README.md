# fifoTesting

This repo contains code for pipeing data via a linux fifo file: https://man7.org/linux/man-pages/man7/fifo.7.html, from a Python file to a javascript or python file. To get started, clone the repository and create the fifo file by running the command `mkfifo multimeterData.fifo` in the terminal. The fifofile can them be used by the Python scipts when running `python fifoWriter.py` and `python fifoReader.py`. To pipe to fifoReader.js, first install nodejs with `sudo apt install nodejs`. Then run the file with node fifoReader.js. 
