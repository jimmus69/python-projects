#! /usr/bin/python

import struct

a = 3.141593
b = 33.13555
c = 124556

fbw = open( "binary.bin", "wb");

data = struct.pack('f', a)
fbw.write(data)
data = struct.pack('f', b)
fbw.write(data)
data = struct.pack('f', c)
fbw.write(data)

fbw.close()

fbr = open("binary.bin", "rb")

floatsize = struct.calcsize('f')
data = fbr.read(floatsize)
ar = struct.unpack('f', data)
print "a = ", a, " ar = ", ar

floatsize = struct.calcsize('f')
data = fbr.read(floatsize)
br = struct.unpack('f', data)
print "b = ", b, " br = ", br

floatsize = struct.calcsize('f')
data = fbr.read(floatsize)
cr = struct.unpack('f', data)
print "c = ", c, " cr = ", cr


