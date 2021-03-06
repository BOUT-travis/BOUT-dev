from __future__ import division
from past.utils import old_div


def blob_velocity(n,**kwargs):
	import numpy as np

	from boututils import calculus as Calc
	# Calculate blob velocity in normalized time and normalized grid spacing
	# 
	# Input: Blob density as a 3D vector in the form  n[t,x,z] where t is time and x,z are the perpendicular spatial coordinates
	# 
	# Keywords: 
	#	    
	# 	    type='peak' -> Calculate velocity of the peak density
	#           type='COM' -> Calculate centre of mass velocity
	# 	    Index=True -> return indices used to create velocity
	#
	# Default: Peak velocity with no index returning

	size = n.shape
	
	try:
		v_type = kwargs['type']
	except:
		v_type = 'peak'		#Default to peak velocity calculation
	try: 		
		return_index = kwargs['Index']
	except:
		return_index = False	#Default to no index returning

	
	if v_type == 'peak':
		x = np.zeros(size[0])
		z = np.zeros(size[0])
		for i in np.arange(size[0]):
			nmax,nmin = np.amax((n[i,:,:])),np.amin((n[i,:,:]))
			xpos,zpos = np.where(n[i,:,:]==nmax)		
			x[i] = xpos[0]
			z[i] = zpos[0]	
		
	if v_type == 'COM':
		x = np.zeros(size[0])
		z = np.zeros(size[0])
		for i in np.arange(size[0]):            	
			data = n[i,:,:] - n[0,0,0]   #use corner cell rather than nmin
			ntot = np.sum(data[:,:])
		
			z[i] = old_div(np.sum(np.sum(data[:,:],axis=0)*(np.arange(size[2]))),ntot)
			x[i] = old_div(np.sum(np.sum(data[:,:],axis=1)*(np.arange(size[1]))),ntot)
				
	vx = Calc.deriv(x)
	vz = Calc.deriv(z)

	if return_index:
		return vx,vz,x,z
	else:
		return vx,vz
	


import numpy as np
from boutdata import *
from boututils import *
import pickle
import matplotlib.pyplot as plt

n = collect('n')


vx,vy,xx,yy = blob_velocity(n[:,:,0,:],type='COM',Index=True)

f = open('Velocity.dat','w')
pickle.dump(vx,f)
f.close()

f = open('Position.dat','w')
pickle.dump(xx,f)
f.close()


f = open('Velocity.dat','r')
vx = pickle.load(f)
f.close()

plt.plot(vx)
plt.show()






