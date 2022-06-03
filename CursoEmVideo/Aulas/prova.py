x = 5
y = 12
z = (x + y) // x;
if z==1:
 x = x*5
elif z == 2:
 y = y*5
elif z ==3:
 z = z*5   
else:
 x = x*5
 y = y*5
 z = z*5
print ('{}, {} e {}'.format(x,y,z))