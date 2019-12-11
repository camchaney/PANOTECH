<h1 align="center">

<img src="LOGO.png" alt="Panotech Logo" width="200px"/>

PANOTECH

</h1><h4 align="center">

A critique of public survalence & Final project for Fall 2019
Critical Practices.

- Zeke, Alyssa, Cameron, and Serena.

</h4>

Install.
--------

Panotech requires a fairly involved hardware setup and as such this
installation guide is slightly incomplete as it only details the
software configuration. Time allowing, we'll work on a hardware setup
guide as well. At the moment though, this mostly serves as a guide for
our group.

This project is designed to be run on a Raspberry Pi with an Arduino
attached. The Pi subsequentally communicates with the Arduino via its
serial port. Make sure you have the included Arduino code loaded onto
the Arduino before attempting to do anything.

In order to run this code you'll need to have a couple things
installed:

	- openCV
	- electron
	- pyserial
	
Pyserial can be installed with `pip install pyserial`. Electron has a
bug for our pi, so in order to install electron, you'll need to
specify the archetecture. Run `npm install --arch=armv7l electron`.

Finally, installing openCV is a bit of a process and is outside the
scope of this installation manual. Googling how to do it is probably
your best bet.

Run.
----

This part is pretty simple, run the following two commands in
different terminal sessions:

	```
	$ python3 main.py
	$ npm start
	```
	
Boom. Assuming install worked, you should be up and running.
