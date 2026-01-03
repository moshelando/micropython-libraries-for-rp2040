
# Outputs

## Display

### WS2812 Strip Light; "NeoPixels":

	Neopixels are individual led's connected serially.
	Each led can be separately programmed.
	https://cdn-shop.adafruit.com/datasheets/WS2812.pdf
	
	The neopixel library was first made by Damien P. George (micropython founders).
	It's packaged with most micropython distributions.
	https://docs.micropython.org/en/latest/library/neopixel.html
	
	Adafruit has extensively expanded on the original library.
	The Adafruit libraries seem optimized for Arduino and circuitpython.
	https://adafruit.github.io/Adafruit_NeoPixel/html/class_adafruit___neo_pixel.html
	https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel/tree/6.3.8
	
	Numerous other micropython and python libraries have been made.
	
### 8 x 8 LED Matrix

	The 8 x 8 LED matrix is controlled by the MAX7219 chip.
	This chip can control numerous types of LED displays.
	It takes SPI input.
	https://cdn-shop.adafruit.com/datasheets/MAX7219.pdf

	mcauser wrote a micropython library for the MAX7219 based on deshipu's library.
	https://github.com/mcauser/micropython-max7219/blob/master/max7219.py
	https://github.com/mcauser/deshipu-micropython-max7219/blob/master/max7219.py
	
### TM1637 7 Segment Display:

	The "TM1637" is a control circuit for 7-segment displays; generally, 4-digit displays.
	https://datasheetspdf.com/pdf-file/788613/TitanMicro/TM1637/1
	
	It takes serial input.
	
	It seems like the first library made for it was an Arduino library by "Avishorp".
	https://github.com/avishorp/TM1637
	
	A micropython library was made by Mike Causer ("mcauser").
	https://github.com/mcauser/micropython-tm1637
	I'm not sure if it was based on Avishorp's Arduino library.
	
	There have been several Python ports based on mcauser's micropython library.

### LCD 1602 2-Line Character Display:

	The "1602 Display Module" is a display with 2 lines, 16 characters per line.
	It is controlled by the HD44780 driver.
	https://cdn-shop.adafruit.com/datasheets/TC1602A-01T.pdf
	https://cdn-shop.adafruit.com/datasheets/HD44780.pdf

	To transmit data to the HD44780, the HD44780 requires many data pins in parallel transmission.
	However, using the i2C protocol with serial transmission, only two lines (SDA and SCL) are required.
	Additionally, serial transmission allows several devices to be connected to the same bus.

	To interpret the serial data for the HD44780, a separate chip is required.
	The "8574" chip family is designed for this purpose, transmitting i2C data to the HD44780.
	The specific name of the chip varies depending on the manufacturer.
	For example, Analog Tek's version is named AT8574 and NXP's is called PCA8574.

	DFROBOT produced the first library for communicating with the 8574.
	https://www.dfrobot.com/product-135.html

	Based on that library, FDEBRABANDER compiled an Arduino library.
	https://github.com/fdebrabander/Arduino-LiquidCrystal-I2C-library

	Finally, BRAINELECTRONICS compiled a Micropython library based on FDEBRABANDER's library
	https://github.com/brainelectronics/micropython-i2c-lcd
	
	Aside from the 8574-related code, all I2C transmission requires an I2C library.
	MicroPython comes with one.
	https://docs.micropython.org/en/latest/library/machine.I2C.html#machine-i2c
	
### SSD1306 Oled Display

	The SSD1306 is a driver for 128 x 64 OLED displays.
	It is made by Solomon Systech.
	https://cdn-shop.adafruit.com/datasheets/SSD1306.pdf
	
	It can take SPI or I2C input.
	
	MicroPython has a SSD1306 driver.
	https://github.com/micropython/micropython/blob/4d9e657f0ee881f4a41093ab89ec91d03613744d/drivers/display/ssd1306.py
	
## Motors

### 28BYJ-48 Step motor:

	The 28BYJ-48 is a step motor.
	https://datasheetspdf.com/pdf/1006817/Kiatronics/28BYJ-48/1
	
	For proper voltage regulation, it is controlled by the ULN2003; a board made by Texas Instruments.
	https://microcontrollerslab.com/wp-content/uploads/2019/11/IC-ULN2003-Datasheet.pdf
	
	Programming the ULN2003 is relatively simple and does not require a dedicated library.
	
### SG90 Servo

	The SG90 is a servo, originally made by Tower Pro.
	https://datasheetspdf.com/pdf-file/791970/TowerPro/SG90/1
	
	MicroPython has a built in class for using servos with pyboards, however, not for the rp2040.
	Here's one by redoxcode:
	https://github.com/redoxcode/micropython-servo
	
# Inputs

## Sensors

### Sound, Light (LDR), Vibration, Tilt (SW520-D) Sensor

### Raindrop Sensor

	The raindrop sensor senses whether or not water is falling on the sensor.
	It has a digital output, as well as an analog output dependant on the intensity of the water.

### PIR (Passive Infrared) Sensor

	The PIR sensor is driven by a BISS0001 chip.
	https://cdn-learn.adafruit.com/assets/assets/000/010/133/original/BISS0001.pdf

### BMP280 Pressure Sensor

	The BMP280 is a pressure sensor by Bosch.
	https://cdn-shop.adafruit.com/datasheets/BST-BMP280-DS001-11.pdf
	
	It uses both SPI and I2C iterface.
	
	The current BMP280 library is by David Stenwall.
	https://github.com/dafvid/micropython-bmp280
	(See readme.md for inspirations.)	
	
### UltraSonic Sensor

	The HC-sr04 is an ultrasonic sensor.
	It has two data pins; a "trigger pulse" input, and an "echo pulse" output.
	https://datasheetspdf.com/pdf-file/1380136/ETC/HC-SR04/1
	
	'Roberto Sánchez' made a micropython library for it.
	https://github.com/rsc1975/micropython-hcsr04/blob/master/hcsr04.py
	
### DS18B20 Temerature Sensor

	The DS18B20 is a temperature sensor made by Dallas Semiconductor.
	https://cdn-shop.adafruit.com/datasheets/DS18B20.pdf
	
	It has a "One-Wire" interface, which requires a special library to communicate with it.
	There's a default mocropython onewire library.
	https://github.com/micropython/micropython-lib/blob/master/micropython/drivers/bus/onewire/onewire.py
	There's also a specific DS18x20 library. (The Ds18b20 is part of the DS18x20 family.)
	https://github.com/micropython/micropython-lib/blob/master/micropython/drivers/sensor/ds18x20/ds18x20.py
	
### DHT11 Digital Temperature and Humidity Sensor

	The DHT11 is part of a family of DHT (Digital Humidity and Temperature) sensors made by Aosong Electronics.
	https://components101.com/sites/default/files/component_datasheet/DHT11-Temperature-Sensor.pdf
	
	There is a default micropython library for the DHT11, however, it does not appear to be for the rp2040.
	Here's one that works for the pico, by geekpi:
	https://github.com/geeekpi/picokitadv/blob/main/libs/dht.py	

### MPU6050 Gyroscope and Accelerometer

	The MPU6050 is a device that tracks rotation and acceleration, each in all 3 axis.
	It has an on-board ADC.
	It is connected through I2C.
	Aside from the power, ground, and two i2C pins, it has an additional four:
	xda and xcl, for attaching other sensors directly to it;
	add for toggling a second i2c address,
	and int for triggering hardware interupts.
	https://invensense.tdk.com/wp-content/uploads/2015/02/MPU-6000-Datasheet1.pdf
	https://invensense.tdk.com/wp-content/uploads/2015/02/MPU-6000-Register-Map1.pdf
	
	There is no official library for using the 6050 with the RP2040.
	Here are two:
	https://github.com/OneMadGypsy/upy-motion
	https://github.com/adamjezek98/MPU6050-ESP8266-MicroPython/blob/master/mpu6050.py
	
## Control

### Relay Module

	The relay module is an electonically controlled switch.
	It has a power and gnd input, as well as a control input.
	It has three pins it controls: the COM for inputting the circuit that's being switched;
	NC (Normal Closed) is default on; NO (Normal Open) is default off.
	When the control input is pulled high, the NC circuit opens, and the NO circuit closes.
	https://datasheetspdf.com/pdf-file/720556/Songle/SRD-05VDC-SL-C/1
	
### Potentiomater

	A potentiometer outputs an analog signal dependant on the knob's rotation.
	To convert the signal to digital, Micropython's ADC (analog to digital conversion) library is used.
	
### Joystick

	The joystick has 3 outputs:
	x analog
	y analog
	press digital

### Rotary Encoder

	The rotary encoder has 3 outputs:
	CLK and DT contain infortamion about the rotation.
	SW contains information about whether or not the shaft is pressed.
	
	Proper rotary decoding is a contreversial topic.
	We currently use Mike Teachman's library
	https://github.com/miketeachman/micropython-rotary/blob/master/rotary_irq_rp2.py
	It's based on Ben Buxton's arduino library.
	https://github.com/buxtronix/arduino/tree/master/libraries/Rotary
	It's also inspired by SpotlightKid's micropython.
	https://github.com/SpotlightKid/micropython-stm-lib/tree/master/encoder
