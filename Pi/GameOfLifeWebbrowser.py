# -*- coding: utf-8 -*-
from time import sleep
import RPi.GPIO as GPIO
 
# Import the WS2801 module.
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI

from os import system, name
import random
import sys

import os
import copy
from flask import Flask, request
from flask_cors import CORS, cross_origin
from threading import Thread
import json

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
# Configure the count of pixels:
PIXEL_COUNT = 144
    
# Alternatively specify a hardware SPI connection on /dev/spidev0.0:
SPI_PORT   = 0
SPI_DEVICE = 0
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE), gpio=GPIO)

color = (0, 0, 255) # Blau

global thread
global led

class LED:
    global board
    global c
    global iteration
    global is_running

    def terminate(self):  
        global is_running
        is_running = False
        pixels.clear()
        pixels.show()
        sleep(1)


    def main():
        init_board()
        show_board()
        init_user_choice()
        start_simulation()

    def init_board(self):
        global board
        global iteration
        iteration = 0
        board = []
        count = 12
        for column in range(0, count):
            column = []
            for item in range(0, count):
                column.append("o")
            board.append(column)


    def show_board(self):
        pixels.clear()
        row_nr = 0
        for r in board:
            col_nr = 0
            for c in r:
                col = (0,0,0)
                if board[row_nr][col_nr] == "x":
                    col = self.wheel(((256 // pixels.count() + ((iteration*10) % 256))) % 256)
                else:
                    col = (0, 0, 0)
                pos = 0
                if row_nr % 2 == 0:
                    pos = (row_nr*12)+col_nr
                else:
                    pos = (row_nr*12)+11-col_nr
                pixels.set_pixel(pos, Adafruit_WS2801.RGB_to_color( col[0], col[1], col[2] ))
                col_nr += 1
            row_nr += 1
        pixels.show()


    def show_terminal_board(self):  
        row_nr = 0
        for r in board:
            col_nr = 0
            line = "|"
            for c in r:
                line = line + board[row_nr][col_nr] + "|"
                col_nr += 1
            row_nr += 1
            print(line)


    def start_simulation(self):
        global board
        global c
        global iteration
        global is_running
        is_running = True
        try:
            iteration = 0
            no_change = False
            while(c >= 0 and is_running is True):
                if iteration > 1:
                    no_change = True
                new_board = copy.deepcopy(board)
                iteration += 1
                print("Iterationen: "+ str(iteration))
                self.show_board()
                self.show_terminal_board()
                for col in range(len(board)):
                    for row in range(len(board)):
                        value = board[row][col]
                        count = self.count_neighbours(row, col)
                        if (count == 3) and (value == "o"):
                            new_board[row][col] = "x"
                            c += 1
                            no_change = False
                        elif ((count < 2) or (count > 3)) & (value == "x"):
                            new_board[row][col] = "o"
                            c -= 1
                            no_change = False
                board = copy.deepcopy(new_board)
                sleep(1)
                if(no_change == True):
                    pixels.clear()
                    pixels.show()
                    self.random_fill()
                    self.start_simulation()         
        except KeyboardInterrupt:
            pixels.clear()
            pixels.show()
            exit(0)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise


    def count_neighbours(self, row, col):
        n = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i != 0) or (j != 0):
                    r = row + i
                    c = col + j
                    if (r>=0) & (r<len(board)) & (c>=0) & (c<len(board)):
                        n += 1 if board[r][c] == "x" else 0
        return n


    def clear():
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')


    def wheel(self, pos):
        if pos < 85:
            return (pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return (255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return (0, pos * 3, 255 - pos * 3)


    def random_fill(self, probability = 0.2):
        global board
        global c
        c = 0
        for col in range(len(board)):
            for row in range(len(board)):
                if (random.random() < probability):
                    board[row][col] = "x"
                    c += 1
                else:
                    board[row][col] = "o"    

        self.show_terminal_board()

    def start_sim_with_random(self):
        self.init_board()
        self.random_fill()
        self.start_simulation()
    
    def start_sim_with_data(self):
        self.start_simulation()


@cross_origin()
@app.route('/board/random', methods = ['GET', 'POST'])
def start_sim_with_random():
    global thread
    global led
    global is_running
    if is_running:
        led.terminate()
    pixels.clear()
    pixels.show()
    thread = Thread(target=led.start_sim_with_random)
    thread.start()
    return 'Done!'


@cross_origin()
@app.route('/board/terminate', methods = ['GET', 'POST'])
def terminate():
    global thread
    global led
    led.terminate()
    return 'Terminated!'


@cross_origin()
@app.route('/board/new', methods = ['POST'])
def get_data_from_ui():
    global led
    global thread
    global is_running
    global board
    data = request.get_json()
    if is_running:
        led.terminate()
    pixels.clear()
    pixels.show()
    board = data
    count_living(data)
    thread = Thread(target=led.start_sim_with_data)
    thread.start()
    return "Got Data"


def count_living(data):
    global c
    c = 0
    for row in range(len(data)):
        for col in range(len(data)):
            if data[col][row] == 'x':
                c += 1


if __name__ == "__main__":
    global led
    global is_running
    is_running = False
    led = LED()
    app.run(debug=True, host='0.0.0.0', port=5000)