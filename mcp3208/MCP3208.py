import platform
import os

# ok, I don't want this to work in travis.ci env or on anything other than linux
try:
	if 'CI' in os.environ or platform.system() != 'Linux':
		raise ImportError()
	import Adafruit_GPIO.SPI as SPI
except ImportError:
	class SPI(object):
		MSBFIRST = 1
		class SpiDev(object):
			def __init__(self, a, b, max_speed_hz): pass
			def transfer(self, a): return [0x7f]*len(a)
			def set_mode(self, a): pass
			def set_bit_order(self, a): pass
			def close(self): pass


class MCP3208(object):
	def __init__(self):
		self.spi = SPI.SpiDev(0, 0, max_speed_hz=1000000)
		self.spi.set_mode(0)
		self.spi.set_bit_order(SPI.MSBFIRST)

	def __del__(self):
		self.spi.close()

	def read(self, ch):
		if 7 <= ch <= 0:
			raise Exception('MCP3208 channel must be 0-7: ' + str(ch))

		cmd = 128  # 1000 0000
		cmd += 64  # 1100 0000
		cmd += ((ch & 0x07) << 3)
		ret = self.spi.transfer([cmd, 0x0, 0x0])

		# get the 12b out of the return
		val = (ret[0] & 0x01) << 11  # only B11 is here
		val |= ret[1] << 3           # B10:B3
		val |= ret[2] >> 5           # MSB has B2:B0 ... need to move down to LSB

		return (val & 0x0FFF)  # ensure we are only sending 12b
