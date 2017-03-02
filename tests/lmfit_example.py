import numpy as np
#import emcee
import matplotlib.pyplot as plt

vals = np.loadtxt('waspdata.csv',delimiter=',')
x = vals[:,0]
y = vals[:,1]
err = vals[:,2]

# m_true =[-0.3,0.1]


#define a prior, returns -inf when reachs the limit, set to zero if constraining###
def lnprior(p):
	m,b = p
	# if -1.0 < m < 0.0 and 0.0 < b < 0.5:
	# 	return 0.0
	return 0.0
#
def lnlike(p,x,y,err): #assume a gaussian distribution##
	m,b = p
	model = m*x + b #telling the likelihood what the model is##
	chi2 = -0.5*(np.sum(((y - model)/err)**2)) ##using a gaussian to minimize##

	# model = m*x + b
	# chisq = (((y - model)/err)**2 + np.log((2*np.pi*err**2)))
	# chi2 =  -0.5 * np.sum(chisq)
	return chi2

def lnprob(p,x,y,err): #now we create the probability function###
	lp = lnprior(p)
	if not np.isfinite(lp):
		return -np.inf
	return lp + lnlike(p,x,y,err)
#
ndim,nwalkers = 2,100 #initiate numvber of dimensions and walkers##
'''trying scipy optimize minimize for initial positions'''
# import scipy.optimize as op
# nll = lambda *args: -lnlike(*args)
# result = op.minimize(nll, m_true, args=(x, y, err))
# fit = result["x"]

'''trying polyfit to find initial positions'''
# fit = np.polyfit(x,y,deg=1,w=err)
#
'''trying lmfit to find initial positions'''
def residual(params,x,y,err):
	m = params['slope'].value
	b = params['intercept'].value

	model = m*x + b

	chi2 = (model-y)/err
	return chi2

from lmfit import minimize,Parameters,report_fit

params = Parameters()
params.add('slope',min=-0.5,max=0.0)
params.add('intercept',min=0.0,max=1.0)

out = minimize(residual,params,args=(x,y,err))
report_fit(out.params)

fit = [out.params['slope'].value,out.params['intercept'].value]

print(fit)
