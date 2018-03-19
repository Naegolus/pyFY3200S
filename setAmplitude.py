#!/usr/bin/env python3

import funcgen.fy3200s as fg;
import time;
import sys;

###############################################################################

if (len(sys.argv) != 3):
	print("usage: python3 setFrequency.py <channel> <frequency>")
	print("  channel:   0, 1")
	print("  frequency: [Hz]")
	sys.exit(1)

funcGen = fg.FY3200S()

channel = int(sys.argv[1])
frequency = int(sys.argv[2])

funcGen[channel].set_frequency(frequency)

funcGen.close()
