'''
Ball and stick with Na and K channels
'''
from brian import *
from brian.experimental.morphology import *

defaultclock.dt=0.025*ms

# Morphology
morpho=Soma(30*um)
morpho.axon=Cylinder(diameter=1*um,length=300*um,n=100)

# Channels
gL=1e-4*siemens/cm**2
EL=-70*mV
ENa = 50*mV
ka = 6*mV
ki=6*mV
va = -30*mV
vi = -50*mV
EK=-90*mV
vk = -20*mV
kk = 8*mV
eqs='''
Im=gL*(EL-v)+I+gNa*m*h*(ENa-v)+gK*n*(EK-v) : amp/cm**2
dm/dt=(minf-m)/(0.3*ms) : 1 # simplified Na channel
dh/dt=(hinf-h)/(3*ms) : 1 # inactivation
dn/dt=(ninf-n)/(5*ms) : 1 # K+
minf=1/(1+exp((va-v)/ka)) : 1
hinf=1/(1+exp((v-vi)/ki)) : 1
ninf=1/(1+exp((vk-v)/kk)) : 1
I : amp/cm**2
gNa : siemens/cm**2
gK : siemens/cm**2
'''

neuron = SpatialNeuron(morphology=morpho, model=eqs, Cm=1 * uF / cm ** 2, Ri=100 * ohm * cm)
neuron.v=-65*mV
neuron.I=0*amp/cm**2
neuron.axon.gNa[10:20]=700*gL
neuron.axon.gK[10:20]=700*gL

# Monitors
mon=StateMonitor(neuron,'v',record=True)

run(1*ms)
neuron.I[0]=0.15*nA/neuron.area[0]
run(50*ms)
neuron.I=0*amp
run(95*ms,report='text')

plot(mon.times/ms,mon[0]/mV,'r')
plot(mon.times/ms,mon[20]/mV,'g')
plot(mon.times/ms,mon[40]/mV,'b')
plot(mon.times/ms,mon[60]/mV,'k')
plot(mon.times/ms,mon[80]/mV,'y')
show()
