#!/usr/bin/env python
#
# grabserial - program to read a serial port and send the data to stdout

# Copyright 2006 Sony Corporation
#
# This program is provided under the Gnu General Public License (GPL)
# version 2 ONLY.
#
# 2006-09-07 by Tim Bird <tim.bird@am.sony.com>
# 2011-09-24 Constantine Shulyupin <const@makelinux.com> better time output and time delta
# 2011-12-19 Kent Borg <kentborg@borg.org> added instantpat and launchtime
#
# To do:
#  * buffer output chars??
#

MAJOR_VERSION=1
MINOR_VERSION=0
REVISION=2

import os, sys
import getopt
import serial
import time
import re

cmd = os.path.basename(sys.argv[0])
verbose = 0

def vprint(message):
	if verbose:
		print message

def usage(rcode):
	print """%s : Serial line reader
	Usage: %s [options] <config_file>
options:
    -h, --help             Print this message
    -d, --device=<devpath> Set the device to read (default '/dev/ttyS0')
    -b, --baudrate=<val>   Set the baudrate (default 115200)
    -w, --width=<val>      Set the data bit width (default 8)
    -p, --parity=<val>     Set the parity (default N)
    -s, --stopbits=<val>   Set the stopbits (default 1)
    -x, --xonxoff          Enable software flow control (default off)
    -r, --rtscts           Enable RTC/CTS flow control (default off)
    -e, --endtime=<secs>   End the program after the specified seconds have
                           elapsed.
    -t, --time             Print time for each line received.  The time is
                           when the first character of each line is
                           received by %s
    -m, --match=<pat>      Specify a regular expression pattern to match to
                           set a base time.  Time values for lines after the
                           line matching the pattern will be relative to
                           this base time.
    -i, --instantpat=<pat> Specify a regular expression pattern to have its time
                           reported at end of run.  Works mid-line.
    -l, --launchtime       Set base time from launch of program.
    -v, --verbose          Show verbose runtime messages
    -V, --version          Show version number and exit

Ex: %s -e 30 -t -m "^Linux version.*"
This will grab serial input for 30 seconds, displaying the time for
each line, and re-setting the base time when the line starting with
"Linux version" is seen.
""" % (cmd, cmd, cmd, cmd)
	sys.exit(rcode)

def main():
	global verbose

	# parse the command line options
	try:
		opts, args = getopt.getopt(sys.argv[1:],
			 "hli:d:b:w:p:s:xrtm:e:vV", [
				"help",
				"launchtime",
				"instantpat=",
				"device=",
				"baudrate=",
				"width=",
				"parity=",
				"stopbits=",
				"xonxoff",
				"rtscts",
				"time",
				"match=",
				"endtime=",
				"verbose",
				"version"])
	except:
		# print help info and exit
		print "Error parsing command line options"
		usage(2)

	device="/dev/ttyS0"
	baudrate=115200
	width=8
	parity='N'
	stopbits=1
	xon=0
	rtc=0
	show_time = 0
	basepat = ""
	instantpat = ''
	basetime = 0
	instanttime = None
	endtime = 0

	# get a dummy instance for error checking
	sd = serial.Serial()

	for opt, arg in opts:
		if opt in ["-h", "--help"]:
			usage(0)
		if opt in ["-d", "--device"]:
			device = arg
			if not os.path.exists(device) and device.lower() != "stdin":
				print "Error: serial device '%s' does not exist" % device
				usage(2)
		if opt in ["-b", "--baudrate"]:
			baudrate = int(arg)
			if baudrate not in sd.BAUDRATES:
				print "Error: invalid baud rate '%d' specified" % baudrate
				print "Valid baud rates are: %s" % str(sd.BAUDRATES)
				sys.exit(3)
		if opt in ["-p", "--parity"]:
			parity = arg.upper()
			if parity not in sd.PARITIES:
				print "Error: invalid parity '%s' specified" % parity
				print "Valid parities are: %s" % str(sd.PARITIES)
				sys.exit(3)
		if opt in ["-w", "--width"]:
			width = int(arg)
			if width not in sd.BYTESIZES:
				print "Error: invalid data bit width '%d' specified" % width
				print "Valid data bit widths are: %s" % str(sd.BYTESIZES)
				sys.exit(3)
		if opt in ["-s", "--stopbits"]:
			stopbits = int(arg)
			if stopbits not in sd.STOPBITS:
				print "Error: invalid stopbits '%d' specified" % stopbits
				print "Valid stopbits are: %s" % str(sd.STOPBITS)
				sys.exit(3)
		if opt in ["-x", "--xonxoff"]:
			xon = 1
		if opt in ["-r", "--rtcdtc"]:
			rtc = 1
		if opt in ["-t", "--time"]:
			show_time=1
		if opt in ["-m", "--match"]:
			basepat=arg
		if opt in ["-i", "--instantpat"]:
			instantpat=arg
		if opt in ["-l", "--launchtime"]:
			print('setting basetime to launch')
			basetime = time.time()
		if opt in ["-e", "--endtime"]:
			endstr=arg
			try:
				endtime = time.time()+float(endstr)
			except:
				print "Error: invalid endtime %s specified" % arg
				sys.exit(3)
		if opt in ["-v", "--verbose"]:
			verbose=1
		if opt in ["-V", "--version"]:
			print "grabserial version %d.%d.%d" % (MAJOR_VERSION, MINOR_VERSION, REVISION)
			sys.exit(0)

	if device.lower() != "stdin":
	# if verbose, show what our settings are
	    vprint("Opening serial port %s" % device)
	    vprint("%d:%d%s%s:xonxoff=%d:rtcdtc=%d" % (baudrate, width,
		     parity, stopbits, xon, rtc))
	if endtime:
		vprint("Program will end in %s seconds" % endstr)
	if show_time:
		vprint("Printing timing information for each line")
	if basepat:
		vprint("Matching pattern '%s' to set base time" % basepat)
	if instantpat:
		vprint("Instant pattern '%s' to set base time" % instantpat)

	if device.lower() == "stdin":
		import select
		s = sys.stdin
	else: 
	    # now actually open and configure the requested serial port
	    # specify a read timeout of 1 second
		s = serial.Serial(device, baudrate, width, parity, stopbits, 1,
				  xon, rtc)
	# read from the serial port until something stops the program
	prev1 = 0
	linetime = 0
	newline = 1
	curline = ""
	vprint("Use Control-C to stop...")
	try:
                while(1):
                        x = ""
		    # read for up to 1 second
			if device.lower() == "stdin":
				r, w, e = select.select([ s ], [], [], 1)       # wait up to 1 second
				if s in r:
					x = os.read(s.fileno(), 1)      # read 1 character
			else:
				x = s.read()

			# see if we're supposed to stop yet
			if endtime and time.time()>endtime:
				break

			# if we didn't read anything, loop
			if len(x)==0:
				continue

			# ignore carriage returns
			if x=="\r":
				continue

			# set basetime, by default, to when first char
			# is received
			if not basetime:
				#print('setting basetime')
				basetime = time.time()

			if show_time and newline:
				linetime = time.time()
				elapsed = linetime-basetime
				if instanttime:
					instanttime_str = '%4.2f' % (instanttime-basetime)
					print('The output: "' + instantpat + '", was matched at ' + instanttime_str)
					instanttime = None
				if not prev1:
					prev1 = elapsed
				sys.stdout.write("%4.2f\t" % elapsed)
				#if (elapsed-prev1)>0.0005:
				sys.stdout.write("%4d\t" % ((elapsed-prev1)*100))
				#else:
				#	sys.stdout.write("    0\t" )
				prev1 = elapsed
				newline = 0

			# FIXTHIS - should I buffer the output here??
			sys.stdout.write(x)
			curline += x
			
			if (instantpat
			    and not instanttime
			    and instantpat in curline # re.match(instantpat, curline)
			    ):
				# print('matched instantpat')
				instanttime = time.time()

			if x=="\n":
				newline = 1
				if basepat and re.match(basepat, curline):
					basetime = linetime
				curline = ""
			sys.stdout.flush()
	finally:
                s.close()
                if instanttime:
                        instanttime_str = '%4.2f' % (instanttime-basetime)
                        print('\nThe instantpat: "' + instantpat + '", was matched at ' + instanttime_str)

main()
