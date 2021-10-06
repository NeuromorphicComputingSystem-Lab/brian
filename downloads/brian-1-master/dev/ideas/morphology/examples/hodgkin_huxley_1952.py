'''
Hodgkin-Huxley equations (1952)

Conduction velocity is about 12.5 m/s (is it right?)
'''
from brian import *
from brian.experimental.morphology import *

defaultclock.dt=0.1*ms

morpho=Cylinder(length=10*cm, diameter=2*238*um, n=1000, type='axon')

El = 10.613* mV
ENa = 115*mV
EK = -12 * mV
gl = 0.3 * msiemens / cm ** 2
gNa = 120 * msiemens / cm ** 2
gK = 36 * msiemens / cm ** 2

# Typical equations
eqs=''' # The same equations for the whole neuron, but possibly different parameter values
Im=gl*(El-v)+gNa*m**3*h*(ENa-v)+gK*n**4*(EK-v)+I : amp/cm**2 # distributed transmembrane current
I:amp/cm**2 # applied current
dm/dt=alpham*(1-m)-betam*m : 1
dn/dt=alphan*(1-n)-betan*n : 1
dh/dt=alphah*(1-h)-betah*h : 1
alpham=(0.1/mV)*(-v+25*mV)/(exp((-v+25*mV)/(10*mV))-1)/ms : Hz
betam=4.*exp(-v/(18*mV))/ms : Hz
alphah=0.07*exp(-v/(20*mV))/ms : Hz
betah=1./(exp((-v+30*mV)/(10*mV))+1)/ms : Hz
alphan=(0.01/mV)*(-v+10*mV)/(exp((-v+10*mV)/(10*mV))-1)/ms : Hz
betan=0.125*exp(-v/(80*mV))/ms : Hz
'''

neuron = SpatialNeuron(morphology=morpho, model=eqs, Cm=1 * uF / cm ** 2, Ri=35.4 * ohm * cm)
neuron.v=0*mV
neuron.h=1
neuron.m=0
neuron.n=.5
neuron.I=0*amp/cm**2
M=StateMonitor(neuron,'v',record=True)

run(50*ms)
neuron.I[0]=1 * uA/neuron.area[0] # current injection at one end
run(3*ms)
neuron.I=0*amp/cm**2
run(50*ms)

for i in range(10):
    plot(M.times/ms,M[i*10]/mV)
show()
