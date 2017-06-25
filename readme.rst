.. figure:: https://raw.githubusercontent.com/MomsFriendlyRobotCompany/MCP3208/master/docs/pics/chip.png
    :width: 300px

MCP3208
=============

.. image:: https://img.shields.io/pypi/l/mcp3208.svg
	:target: https://github.com/MomsFriendlyRobotCompany/mcp3208
.. image:: https://img.shields.io/pypi/pyversions/mcp3208.svg
	:target: https://github.com/MomsFriendlyRobotCompany/mcp3208
.. image:: https://img.shields.io/pypi/wheel/mcp3208.svg
	:target: https://github.com/MomsFriendlyRobotCompany/mcp3208
.. image:: https://img.shields.io/pypi/v/mcp3208.svg
	:target: https://github.com/MomsFriendlyRobotCompany/mcp3208

This is a python library designed to work with the MCP3208 ADC using SPI on a Raspberry Pi. The MCP3208 is capable of:

- 12-bit resolution
- ±1 LSB max DNL
- ±1 LSB max INL (MCP3204/3208-B)
- ±2 LSB max INL (MCP3204/3208-C)
- 4 (MCP3204) or 8 (MCP3208) input channels
- Analog inputs programmable as single-ended or pseudo-differential pairs
- On-chip sample and hold
- SPI serial interface (modes 0,0 and 1,1)
- Single supply operation: 2.7V-5.5V
- 100ksps max.sampling rate at VDD = 5V
- 50ksps max. sampling rate at VDD = 2.7V
- Low power CMOS technology
    - 500 nA typical standby current, 2 μA max.
    - 400 μA max. active current at 5V
- Industrial temp range: -40°C to +85°C

For more information, see the `datasheet <https://raw.githubusercontent.com/MomsFriendlyRobotCompany/MCP3208/master/docs/mcp3208.pdf>`_.

Install
--------

The preferred installation method is::

	pip install mcp3208

Usage
---------

.. code-block:: python

	from mcp3208 import MCP3208
	import time

	adc = MCP3208()

	while True:
		for i in range(8):
			print('ADC[{}]: {:.2f}'.format(i, adc.read(i)))
		time.sleep(0.5)

SPI Interface
----------------

This chip uses SPI to interface with the Raspberry Pi. Basically, the chip
returns 12 bits contained in 3 bytes. You are able to read the MCP3208
either LSB or MSB first.

.. figure:: https://raw.githubusercontent.com/MomsFriendlyRobotCompany/MCP3208/master/docs/pics/waveform.png

MIT License
--------------

**Copyright (c) 2017 Kevin J. Walchko**

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
