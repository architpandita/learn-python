import numpy as np

#np.arange( start, stop, step)

np.arange(1,11)

#numpy.linspace(start, stop, num, endpoint)

#numpy.logspace(start, stop, num, endpoint)
m=np.arange(10).reshape(3,3)
print(m)

print(m.shape)

print(m.ndim)

print(m.dtype.name)


np.zeros( (3,4) )
np.ones( (3,3,4),dtype=np.int16 )

np.empty( (2,2) )

np.random.rand(3,2) #matrix of 3 by 2
np.random.randn(3,2) #matrix of 3 by 2
from skimage import io
im=io.read(".png")
type(im.shape)

import matplotlib.plot

#reverse
plt.imshow(im[::-1])

#reverse column
plt.imshow(im[:,::-1])

#crop
plt.imshow(im[50:50,150,150])

#half size of image
plt.imshow(im[::2,::2])

#sin image
sin_im=np.sin(im)
plt.imshow(sin_im)

#give index of min
np.argmin(im)

ar=np.array([1,2,3,4])
#filter
ar[a>2]

#normalize
ar=np.where(ar>2, 0,1)
print(ar)
ar1=np.array([1,2,4,6])

ar2=np.array([2,3,4,5])
#dot product
print(ar2 @ ar1)

#numpy.sort(a, axis=-1, kind='quicksort', order=None)
np.sort(ar1,kind="")



