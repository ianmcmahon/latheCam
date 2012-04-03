

from post import HNC

X = "X"
Z = "Z"

h = HNC()

h.rapidTo(X=1, Z=2)
h.rapidTo(A=1, C=2)
h.feed(10)
h.slope(Z=4)


# turn 1" to 0.675 from Z=0 to Z=-3 with 0.025" clearance at feed 10ipm surface speed of 100 and DOC=0.025"

mat_dia = 1.0
finish_dia = 0.678
startz = 0
endz = -3
clearance = 0.025
doc = 0.025

while mat_dia > finish_dia:
    h.rapidTo(X=mat_dia+clearance)
    h.rapidTo(Z=startz+clearance)
    mat_dia = (mat_dia - doc) if mat_dia > finish_dia + doc else finish_dia
    h.rapidTo(X=mat_dia)
    h.slope(Z=endz)



for line in h:
    print line


