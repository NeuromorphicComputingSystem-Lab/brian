'''
Very short example program.
'''
#import brian_no_units
from brian import *
from time import time

N = 10000        # number of neurons
Ne = int(N * 0.8) # excitatory neurons 
Ni = N - Ne       # inhibitory neurons
p = 80. / N
duration = 1000 * ms

eqs = '''
dv/dt = (ge+gi-(v+49*mV))/(20*ms) : volt
dge/dt = -ge/(5*ms) : volt
dgi/dt = -gi/(10*ms) : volt
'''

P = NeuronGroup(N, model=eqs, threshold= -50 * mV, reset= -60 * mV)
P.v = -60 * mV + 10 * mV * rand(len(P))
Pe = P.subgroup(Ne)
Pi = P.subgroup(Ni)

Ce = Connection(Pe, P, 'ge', weight=1.62 * mV, sparseness=p)
Ci = Connection(Pi, P, 'gi', weight= -9 * mV, sparseness=p)

M = SpikeMonitor(P)
trace = StateMonitor(P, 'v', record=0)

t1 = time()
run(1 * second)
t2 = time()
print "Simulated in", t2 - t1, "s"
print len(M.spikes), "spikes"

subplot(211)
raster_plot(M)
subplot(212)
plot(trace.times / ms, trace[0] / mV)
show()
