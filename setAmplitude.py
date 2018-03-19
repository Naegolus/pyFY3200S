#!/usr/bin/env python3

import funcgen.fy3200s as fg;
import time;
import sys;

###############################################################################

if (len(sys.argv) != 3):
	print("usage: python3 setFrequency.py <channel> <amplitude>")
	print("  channel:   0, 1")
	print("  amplitude: [V]")
	sys.exit(1)

funcGen = fg.FY3200S()

channel = int(sys.argv[1])
amplitude = float(sys.argv[2])

funcGen[channel].set_amplitude(amplitude)

funcGen.close()
