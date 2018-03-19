#!/usr/bin/env python3

import funcgen.fy3200s as fg;
import time;
import sys;

###############################################################################

if (len(sys.argv) != 3):
	print("usage: python3 setFrequency.py <channel> <offset>")
	print("  channel:   0, 1")
	print("  offset:   [V]")
	sys.exit(1)

funcGen = fg.FY3200S()

channel = int(sys.argv[1])
offset = float(sys.argv[2])

funcGen[channel].set_offset(offset)

funcGen.close()
