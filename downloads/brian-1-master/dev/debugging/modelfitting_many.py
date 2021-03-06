'''
Model fitting example.
Fit an integrate-and-fire model to an in-vitro electrophysiological 
recording during one second.
'''
from brian import loadtxt, ms, Equations
from brian.library.modelfitting import *

if __name__ == '__main__':
    nvar = 100
    equations = '''
        dV/dt=(R*I-V)/tau : 1
        I : 1
        R : 1
        tau : second
    '''
    equations += '\n'.join(['var'+str(i)+':0' for i in range(nvar)])
    equations = Equations(equations)
    input = loadtxt('current.txt')
    spikes = loadtxt('spikes.txt')
    results = modelfitting( model = equations,
                            reset = 0,
                            threshold = 1,
                            data = spikes,
                            input = input,
                            dt = .1*ms,
                            popsize = 1000,
                            maxiter = 3,
                            delta = 4*ms,
                            gpu = 1,
                            R = [1.0e9, 9.0e9],
                            tau = [10*ms, 40*ms],
                            refractory = [0*ms, 10*ms])
    print_table(results)
