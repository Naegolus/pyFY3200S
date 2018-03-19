#!/usr/bin/env python3

import funcgen.fy3200s as fg;
import time;
import sys;

###############################################################################

if (len(sys.argv) != 3):
	print("usage: python3 setFrequency.py <channel> <waveform>")
	print("  channel:   0, 1")
	print("  waveform:")
	print("    sine = 0")
	print("    square = 1")
	print("    triangle = 2")
	print("    arb1 = 3")
	print("    arb2 = 4")
	print("    arb3 = 5")
	print("    arb4 = 6")
	print("    lorentz_pulse = 7")
	print("    multi_tone = 8")
	print("    random_noise = 9")
	print("    ecg = 10")
	print("    trapezoidal_pulse = 11")
	print("    sinc_pulse = 12")
	print("    narrow_pulse = 13")
	print("    white_noise = 14")
	print("    am = 15")
	print("    fm = 16")
	sys.exit(1)

funcGen = fg.FY3200S()

channel = int(sys.argv[1])
waveform = int(sys.argv[2])

funcGen[channel].set_waveform(waveform)

funcGen.close()
