# GameOfLife
You can use this code to set up your local LED Strip Matrix! This was written using Adafruit LED package to control the stripe and flask as an server to get requests from Javascript.
## Requirements
- WS2801 RGB LED Stripe
- Power supply for the stripe
- Raspberry Pi (with Python 2.7)


## Set Up
Wire the LED stripe (f.e. written [here](https://tutorials-raspberrypi.de/raspberry-pi-ws2801-rgb-led-streifen-anschliessen-steuern/)) and install the requirements from the requirements.txt file.
`pip install -r requirements.txt`

Execute the code, or modify the host and port by changing the last line in the python file (see flask documentation). By default, it will listen on port 5000 for API calls. If you modify this, please also modify the url and port in the Javascript file to reach your Pi.

Using the code you find in the parent directory, you can now send requests by simply using the html file. Hosting will be up to you.
