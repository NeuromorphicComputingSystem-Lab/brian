'''
A pseudo MSO neuron, with two dendrites and one axon (fake geometry).
'''
from brian import *
from brian.experimental.morphology import *

defaultclock.dt=0.1*ms

# Morphology
morpho=Soma(30*um)
morpho.axon=Cylinder(diameter=1*um,length=300*um,n=100)
morpho.L=Cylinder(diameter=1*um,length=100*um,n=50)
morpho.R=Cylinder(diameter=1*um,length=150*um,n=50)

# Passive channels
gL=1e-4*siemens/cm**2
EL=-70*mV
eqs='''
Im=gL*(EL-v)+I : amp/cm**2
I : amp/cm**2
'''

neuron = SpatialNeuron(morphology=morpho, model=eqs, Cm=1 * uF / cm ** 2, Ri=100 * ohm * cm)
neuron.v=EL
neuron.I=0*amp/cm**2

# Monitors
mon_soma=StateMonitor(neuron,'v',record=[0])
mon_L=StateMonitor(neuron.L,'v',record=True)
mon_R=StateMonitor(neuron.R,'v',record=25)

run(1*ms)
neuron.L.I[25]=0.2*nA/neuron.L.area[25] # injecting in the left dendrite
run(5*ms)
neuron.I=0*amp
run(50*ms,report='text')

subplot(211)
plot(mon_L.times/ms,mon_soma[0]/mV,'k')
plot(mon_L.times/ms,mon_L[25]/mV,'r')
plot(mon_L.times/ms,mon_R[25]/mV,'b')
subplot(212)
for i in [0,5,10,15,20,25,30,35,40,45]:
    plot(mon_L.times/ms,mon_L[i]/mV)
show()
