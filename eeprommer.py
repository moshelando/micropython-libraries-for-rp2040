# custom eeprom programmer

from machine import Pin
from time import sleep_us, sleep_ms
from eeprommer import Eeprommer

func_pins = {
    "shift_clk": Pin(0),
    "shift_latch": Pin(1),
    "shift_data": Pin(2),
    "output_enable": Pin(17),
    "write_enable": Pin(16),
    }

data_pins = [
    Pin(6),
    Pin(7),
    Pin(8),
    Pin(9),
    Pin(10),
    Pin(11),
    Pin(12),
    Pin(13),
    ]

rpico = Eeprommer(func_pins, data_pins)

# digit_list = [126, 48, 109, 121, 51, 91, 95, 112, 127, 123]
# 
# print("Programming ones place...")
# for n in range(0, 256):
#     ones = n % 10
#     rpico.write_addr(n, digit_list[ones])
#   
# print("Programming tens place...")
# for n in range(0, 256):
#     tens = (n // 10) % 10
#     rpico.write_addr(n+256, digit_list[tens])
# 
# print("Programming hundreds place...")
# for n in range(0, 256):
#     hundreds = (n // 100) % 10
#     rpico.write_addr(n+512, digit_list[hundreds])
#     
# print("Programming sign...")
# for n in range(0, 256):
#     rpico.write_addr(n+768, 0)
# 
# print("Reading...")
# rpico.read_range(0, 1023)

rpico.write_mode()
rpico.write_addr(0, 126)
rpico.read_mode()
rpico.read_range(0, 10)

from machine import Pin
import time

class Eeprommer():

  def __init__(self, func_pins, data_pins):
    # "funct_pins" expects dict
    # "data_pins" expects list
    for key, value in func_pins.items():
        setattr(self, key, value)
    self.shift_clk.init(self.shift_clk.OUT, self.shift_clk.PULL_DOWN)
    self.shift_latch.init(self.shift_latch.OUT, self.shift_latch.PULL_DOWN)
    self.shift_data.init(self.shift_data.OUT, self.shift_data.PULL_DOWN)
    self.output_enable.init(self.output_enable.OUT, self.output_enable.PULL_UP)
    self.write_enable.init(self.write_enable.OUT, self.write_enable.PULL_UP)
    self.data_pins = data_pins
    self.write_enable.high()
    
  def shift(self, data):
    # shifts MSB first
    data_bin = "{:b}".format(data)
    for n in data_bin:
      self.shift_data.value(int(n))     
      self.shift_clk.high()
      self.shift_clk.low()
    self.shift_data.low()
    self.shift_latch.high()
    self.shift_latch.low()

  def shift_addr(self, addr):
      # sets addr at 11 bits
      # if addr is longer than 11 bits, uses LSB
      addr_str = "{:011b}".format(addr)[-11:]
      for n in addr_str:
        self.shift_data.value(int(n))     
        self.shift_clk.high()
        self.shift_clk.low()
      self.shift_data.low()
      self.shift_latch.high()
      self.shift_latch.low()
  
  def write_mode(self):
    self.output_enable.high()
    for n in self.data_pins:
      n.init(n.OUT, n.PULL_DOWN)
    
  def read_mode(self):
    self.output_enable.low()
    for n in self.data_pins:
      n.init(n.IN, pull=None)

  def read_pins(self):
    self.read_mode()
    data = 0
    for pin in reversed(self.data_pins):
      data <<= 1
      val = pin.value()
      data |= val
    return data
  
  def read_addr(self, addr):
    self.read_mode()
    self.shift_addr(addr)
    data = self.read_pins()
    
  def read_range(self, start_addr, end_addr):
    self.read_mode()
    for n in range(start_addr, end_addr, 16):
      line_list = []
      line_addr = n
      formatted_line_addr = "{:03x}".format(line_addr) + ":"
      line_list.append(formatted_line_addr)
      for nn in range(n, n+16):
        data_addr = nn
        if data_addr >= end_addr:
          break
        self.shift_addr(data_addr)
        data = self.read_pins()
        formatted_data = "{:02x}".format(data)
        line_list.append(formatted_data)
      print(" ".join(line_list))

  def write_pins(self, data):
    # sets data at 8 bits
    # if data is longer than 8 bits, uses LSB
    self.write_mode()
    data_str = "{:08b}".format(data)
    for n in range(8):
      bit = data_str[-(n+1)]
      bit_int = int(bit)
      pin = self.data_pins[n]
      pin.value(bit_int)
  
  def write_addr(self, addr, data):
    self.write_mode()
    self.shift_addr(addr)
    self.write_pins(data)
    self.write_enable.low()
    time.sleep_us(1)
    self.write_enable.high()
    time.sleep_us(1)
    


      


