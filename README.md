<h2 align="center">Raspberry Pi Airsoft Turret</h2>
</p>

> Using a [Raspberry Pi 3B+](https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/) to remotely control and shoot dual mounted AR15 airsoft rifles.

_Parts List:_
 - Raspberry Pi 3B+
 - [Adafruit Stepper Motor HAT](https://www.adafruit.com/product/2348)
 - [12V 1A Power Supply](https://www.adafruit.com/product/798)
 - [Female DC Power Adapter - 2.1mm Jack to Screw Terminal Block](https://www.adafruit.com/product/798)
 - (2x) [Nema 17 Stepper Motors](https://www.adafruit.com/product/324)
 - [Nema 17 Stepper Motor Mounting Brackets](https://www.amazon.com/gp/product/B071NWWB7Z/ref=ppx_yo_dt_b_asin_title_o00__o00_s01?ie=UTF8&psc=1)
 - (2x) [Aluminum GT2 Timing Pulley - 6mm Belt - 36 Tooth - 5mm bore](https://www.adafruit.com/product/1253)
 - Any 5V Relay Module --> [The one I used](https://www.amazon.com/SunFounder-Channel-Optocoupler-Expansion-Raspberry/dp/B00E0NTPP4)
 - [GT2 6mm Timing Belt](https://www.amazon.com/gp/product/B01FNT093A/ref=ppx_yo_dt_b_asin_title_o00__o00_s01?ie=UTF8&psc=1). I chose to use a 200mm length belt. You could use a 400mm belt instead.
 - (2x) Airsoft guns --> [The ones I used](https://www.amazon.com/Jing-Gong-RIS-System-Airsoft/dp/B000YKK7TU). Any airsoft guns will work for this project as long as they are electric.
 - Simple OLED Display --> [The one I used](https://learn.adafruit.com/ssd1306-oled-displays-with-raspberry-pi-and-beaglebone-black/overview). The purpose of this screen is to show the Raspberry Pi's ip address on boot since development from a desktop with a full IDE is much easier.
 - USB Type-A Joystick or another gaming controller. I chose to use the Raider Advanced FX joystick since I already had it. Choosing another joystick or controller might mean changing parts of the code to make it compatible.
 - [Raspberry Pi Camera Module V2-8 Megapixel](https://www.amazon.com/Raspberry-Pi-Camera-Module-Megapixel/dp/B01ER2SKFS)
 - Other missing miscellaneous parts and links to be added ...
----------

Development Environment
-------------
1. (Optional) Set up OLED screen --> [walkthrough](https://learn.adafruit.com/monochrome-oled-breakouts/arduino-library-and-examples)
2. Set up Stepper Motor HAT --> [walkthrough](https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi)
3. Rewire the airsoft guns to bypass the trigger switch. We will be inserting our relay module directly between the battery of the airsoft gun and the motor that fires the gun. Wiring diagram soon to come ... 
4. Remap out controls on chosen joystick/controller and modify the code as needed.
5. 3D print coming ...
6. Adding motion detection using [OpenCV](https://opencv.org/) or [Motion](https://github.com/Motion-Project/motion)
