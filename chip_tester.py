# library to test ic chips

from machine import Pin
from time import sleep

# pass a list of the rpico's pins, ordered by the chip's pinout
rpico_pins = [
    Pin(16),
    Pin(17),
    Pin(18),
    Pin(19),
    Pin(20),
    Pin(21),
    Pin(22),
    Pin(9),
    Pin(10),
    Pin(11),
    Pin(12),
    Pin(13),
    Pin(14),
    Pin(15),
    ]

class LS163():    
    
    def __init__(self, rpico_pins):
    
        # assigns each of the chip's pins the relevant rpico pin
        self.clear = rpico_pins[0]
        self.clock = rpico_pins[1]
        self.d0 = rpico_pins[2]
        self.d1 = rpico_pins[3]
        self.d2 = rpico_pins[4]
        self.d3 = rpico_pins[5]
        self.p = rpico_pins[6]
        self.load = rpico_pins[7]
        self.t = rpico_pins[8]
        self.q3 = rpico_pins[9]
        self.q2 = rpico_pins[10]
        self.q1 = rpico_pins[11]
        self.q0 = rpico_pins[12]
        self.carry = rpico_pins[13]
        
        # sets the respective rpico pins in and out
        pico_out_pins = [
            self.clear,
            self.clock,
            self.d0,
            self.d1,
            self.d2,
            self.d3,
            self.p,
            self.load,
            self.t,
            ]
        pico_in_pins = [
            self.q3,
            self.q2,
            self.q1,
            self.q0,
            self.carry,
            ]
        for n in pico_out_pins:
            n.init(n.OUT, n.PULL_DOWN)
        for n in pico_in_pins:
            n.init(n.IN, n.PULL_DOWN)
            
    def return_pins(self):
            
        # reads the chip's output pins
        data = 0
        for pin in [self.q3, self.q2, self.q1, self.q0]:
            data <<= 1
            val = pin.value()
            data |= val
        data = "{:04b}".format(data)
        return data
    
    def print_pins(self):
            
        # prints the chip's output pins
        print(self.return_pins())
    
    def pulse_clock(self):
        
        # pulses clock
        self.clock.high()
        self.clock.low()
    
    def reset(self):
    
        # resets counter
        self.clear.low()
        self.pulse_clock()
        self.clear.high()
    
    def inc_count(self):
        
        # sets pins and increments clock
        self.p.high()
        self.t.high()
        self.clear.high()
        self.load.high()
        self.pulse_clock()
    
    def load_val(self, val):
        val = "{:04b}".format(val)
        for n in range(4):
            [self.d3, self.d2, self.d1, self.d0][n].value(int(val[n]))
        self.load.low()
        self.pulse_clock()
        self.load.high()

    def run_test(self):

        # tests initial clear
        self.reset()
        if self.return_pins() != "0000":
            print("00 failed clear")
        
        # tests counter and carry
        self.inc_count()
        if self.return_pins() != "0001":
            print("01 failed counter")
        
        self.pulse_clock()
        if self.return_pins() != "0010":
            print("02 failed counter")
        
        self.pulse_clock()
        if self.return_pins() != "0011":
            print("03 failed counter")
        
        self.pulse_clock()
        if self.return_pins() != "0100":
            print("04 failed counter")
        
        self.pulse_clock()
        self.pulse_clock()
        self.pulse_clock()
        if self.return_pins() != "0111":
            print("05 failed counter")
            
        for n in range(9):
            self.pulse_clock()
        if self.return_pins() != "0000":
            print("06 failed counter")
        
        # tests enable pins
        self.reset()
        self.t.low()
        self.pulse_clock()
        if self.return_pins() != "0000":
            print("07 failed enable")
            
        self.p.low()
        self.t.high()
        self.pulse_clock()
        if self.return_pins() != "0000":
            print("08 failed enable")
            
        self.t.low()
        self.pulse_clock()
        if self.return_pins() != "0000":
            print("09 failed enable")

        # tests load
        self.load_val(5)
        if self.return_pins() != "0101":
            print("10 failed load")
            
        self.load_val(10)
        if self.return_pins() != "1010":
            print("11 failed load")

        print("done test")
        
counter = LS163(rpico_pins)

counter.run_test()
