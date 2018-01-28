import scipy.misc
import numpy as np
import requests


# Image size
width = 128
height = 128
channels = 3


# Create an empty image
img = np.zeros((height, width, channels), dtype=np.uint8)

# Draw something
#xx, yy = np.mgrid[:height, :width]

# Set the RGB values

r = []
for n in range(1,5):
    a = (requests.get('https://www.random.org/integers/?num=10000&min=0&max=255&col=1&base=10&format=plain&rnd=new')).text
    
    a = a.encode("utf8")
    a = a.strip()
    #print "a",a
    p = a.split('\n')
    for c in p:
        r.append(int(c))


a = (requests.get('https://www.random.org/integers/?num=9152&min=0&max=255&col=1&base=10&format=plain&rnd=new')).text
a = a.encode("utf8")
a = a.strip()
#print "a",a
p = a.split('\n')
for c in p:
    r.append(int(c))
    


#print "r", r

#r = [1,5,3,7,8,10,42,66,126,59,98,255,12,21,45,12,65,78,6,246,126]

res = [r[i:i+3] for i in range(0,len(r),3)]
    
#print "res",res

for y in range(0,128):
    
    for x in range(0,128):
        for u in res:
            #print x
       
            r, g, b = u

            img[y][x][0] = r
            img[y][x][1] = g
            img[y][x][2] = b
            
            
print "Done"


# Save the image
scipy.misc.imsave("image.bmp", img)

