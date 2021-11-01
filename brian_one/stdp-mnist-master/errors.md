# errors

## 2021-10-31

### b.run() error, g++ command error
```
time needed to load test set: 4.91647481918
brian.stateupdater: WARNING  Using codegen CStateUpdater
brian.stateupdater: WARNING  Using codegen CStateUpdater
create neuron group A
create recurrent connections
(400, 3) ./weights/../random/AeAi.npy
(160000, 3) ./weights/../random/AiAe.npy
create monitors for A
create connections between X and A
(313600, 3) ./weights/XeAe.npy
/home/ubuntu/.local/lib/python2.7/site-packages/matplotlib/backend_bases.py:2437: MatplotlibDeprecationWarning: Using default event loop until function specific to this GUI is implemented
  warnings.warn(str, mplDeprecation)
creating /tmp/weave-ubuntu-4j0bU_/python27_intermediate/compiler_42af0de1ac3c9a329eed61392ee41a0d
x86_64-linux-gnu-g++: error: unrecognized command line option ‘-ffast-math -march=native’; did you mean ‘-fsso-struct=native’?
x86_64-linux-gnu-g++: error: unrecognized command line option ‘-ffast-math -march=native’; did you mean ‘-fsso-struct=native’?
brian.experimental.codegen.stateupdaters: WARNING  C compilation failed, falling back on Python.
x86_64-linux-gnu-g++: error: unrecognized command line option ‘-ffast-math -march=native’; did you mean ‘-fsso-struct=native’?
brian.experimental.codegen.stateupdaters: WARNING  C compilation failed, falling back on Python.
x86_64-linux-gnu-g++: error: unrecognized command line option ‘-ffast-math -march=native’; did you mean ‘-fsso-struct=native’?
x86_64-linux-gnu-g++: error: unrecognized command line option ‘-ffast-math -march=native’; did you mean ‘-fsso-struct=native’?
Traceback (most recent call last):
  File "Diehl&Cook_spiking_MNIST.py", line 455, in <module>
    b.run(single_example_time, report='text')
  File "/home/ubuntu/.local/lib/python2.7/site-packages/brian/network.py", line 938, in run
    report=report, report_period=report_period)
  File "/home/ubuntu/.local/lib/python2.7/site-packages/brian/network.py", line 574, in run
    self.update()
  File "/home/ubuntu/.local/lib/python2.7/site-packages/brian/network.py", line 518, in update
    f()
  File "/home/ubuntu/.local/lib/python2.7/site-packages/brian/neurongroup.py", line 501, in update
    spikes = self._threshold(self) # get spikes
  File "/home/ubuntu/.local/lib/python2.7/site-packages/brian/threshold.py", line 186, in __call__
    extra_compile_args=self._extra_compile_args)
  File "/home/ubuntu/.local/lib/python2.7/site-packages/weave/inline_tools.py", line 370, in inline
    **kw)
  File "/home/ubuntu/.local/lib/python2.7/site-packages/weave/inline_tools.py", line 500, in compile_function
    verbose=verbose, **kw)
  File "/home/ubuntu/.local/lib/python2.7/site-packages/weave/ext_tools.py", line 373, in compile
    verbose=verbose, **kw)
  File "/home/ubuntu/.local/lib/python2.7/site-packages/weave/build_tools.py", line 279, in build_extension
    setup(name=module_name, ext_modules=[ext],verbose=verb)
  File "/home/ubuntu/.local/lib/python2.7/site-packages/numpy/distutils/core.py", line 171, in setup
    return old_setup(**new_attr)
  File "/usr/lib/python2.7/distutils/core.py", line 166, in setup
    raise SystemExit, "error: " + str(msg)
weave.build_tools.CompileError: error: Command "x86_64-linux-gnu-g++ -pthread -fno-strict-aliasing -Wdate-time -D_FORTIFY_SOURCE=2 -g -fdebug-prefix-map=/build/python2.7-gnDdqE/python2.7-2.7.17=. -fstack-protector-strong -Wformat -Werror=format-security -fPIC -I/home/ubuntu/.local/lib/python2.7/site-packages/weave -I/home/ubuntu/.local/lib/python2.7/site-packages/weave/scxx -I/home/ubuntu/.local/lib/python2.7/site-packages/weave/blitz -I/home/ubuntu/.local/lib/python2.7/site-packages/numpy/core/include -I/usr/include/python2.7 -c /home/ubuntu/.cache/weave/python27_compiled/sc_d99244cd82bb18764cebf838c5d78a220.cpp -o /tmp/weave-ubuntu-4j0bU_/python27_intermediate/compiler_42af0de1ac3c9a329eed61392ee41a0d/home/ubuntu/.cache/weave/python27_compiled/sc_d99244cd82bb18764cebf838c5d78a220.o -MMD -MF /tmp/weave-ubuntu-4j0bU_/python27_intermediate/compiler_42af0de1ac3c9a329eed61392ee41a0d/home/ubuntu/.cache/weave/python27_compiled/sc_d99244cd82bb18764cebf838c5d78a220.o.d -O3 -ffast-math -march=native" failed with exit status 1
x86_64-linux-gnu-g++: error: unrecognized command line option ‘-ffast-math python Diehl\&Cook_spiking_MNIST.py 
/home/ubuntu/.local/lib/python2.7/site-packages/brian_no_units.py:4: UserWarning: Turning off units
  warnings.warn("Turning off units")
time needed to load training set: 3.46042108536
time needed to load test set: 0.57140994072
brian.stateupdater: WARNING  Using codegen CStateUpdater
brian.stateupdater: WARNING  Using codegen CStateUpdater
create neuron group A
create recurrent connections
(400, 3) ./weights/../random/AeAi.npy
(160000, 3) ./weights/../random/AiAe.npy
create monitors for A
create connections between X and A
(313600, 3) ./weights/XeAe.npy
/home/ubuntu/.local/lib/python2.7/site-packages/matplotlib/backend_bases.py:2437: MatplotlibDeprecationWarning: Using default event loop until function specific to this GUI is implemented
  warnings.warn(str, mplDeprecation)
x86_64-linux-gnu-g++: error: unrecognized command line option ‘-ffast-math -march=native’; did you mean ‘-fsso-struct=native’?
brian.experimental.codegen.stateupdaters: WARNING  C compilation failed, falling back on Python.
x86_64-linux-gnu-g++: error: unrecognized command line option ‘-ffast-math -march=native’; did you mean ‘-fsso-struct=native’?
x86_64-linux-gnu-g++: error: unrecognized command line option ‘-ffast-math -march=native’; did you mean ‘-fsso-struct=native’?
brian.experimental.codegen.stateupdaters: WARNING  C compilation failed, falling back on Python.
x86_64-linux-gnu-g++: error: unrecognized command line option ‘-ffast-math -march=native’; did you mean ‘-fsso-struct=native’?
x86_64-linux-gnu-g++: error: unrecognized command line option ‘-ffast-math -march=native’; did you mean ‘-fsso-struct=native’?
Traceback (most recent call last):
  File "Diehl&Cook_spiking_MNIST.py", line 455, in <module>
    b.run(single_example_time, report='text')
  File "/home/ubuntu/.local/lib/python2.7/site-packages/brian/network.py", line 938, in run
    report=report, report_period=report_period)
  File "/home/ubuntu/.local/lib/python2.7/site-packages/brian/network.py", line 574, in run
    self.update()
  File "/home/ubuntu/.local/lib/python2.7/site-packages/brian/network.py", line 518, in update
    f()
  File "/home/ubuntu/.local/lib/python2.7/site-packages/brian/neurongroup.py", line 501, in update
    spikes = self._threshold(self) # get spikes
  File "/home/ubuntu/.local/lib/python2.7/site-packages/brian/threshold.py", line 186, in __call__
    extra_compile_args=self._extra_compile_args)
  File "/home/ubuntu/.local/lib/python2.7/site-packages/weave/inline_tools.py", line 370, in inline
    **kw)
  File "/home/ubuntu/.local/lib/python2.7/site-packages/weave/inline_tools.py", line 500, in compile_function
    verbose=verbose, **kw)
  File "/home/ubuntu/.local/lib/python2.7/site-packages/weave/ext_tools.py", line 373, in compile
    verbose=verbose, **kw)
  File "/home/ubuntu/.local/lib/python2.7/site-packages/weave/build_tools.py", line 279, in build_extension
    setup(name=module_name, ext_modules=[ext],verbose=verb)
  File "/home/ubuntu/.local/lib/python2.7/site-packages/numpy/distutils/core.py", line 171, in setup
    return old_setup(**new_attr)
  File "/usr/lib/python2.7/distutils/core.py", line 166, in setup
    raise SystemExit, "error: " + str(msg)
weave.build_tools.CompileError: error: Command "x86_64-linux-gnu-g++ -pthread -fno-strict-aliasing -Wdate-time -D_FORTIFY_SOURCE=2 -g -fdebug-prefix-map=/build/python2.7-gnDdqE/python2.7-2.7.17=. -fstack-protector-strong -Wformat -Werror=format-security -fPIC -I/home/ubuntu/.local/lib/python2.7/site-packages/weave -I/home/ubuntu/.local/lib/python2.7/site-packages/weave/scxx -I/home/ubuntu/.local/lib/python2.7/site-packages/weave/blitz -I/home/ubuntu/.local/lib/python2.7/site-packages/numpy/core/include -I/usr/include/python2.7 -c /home/ubuntu/.cache/weave/python27_compiled/sc_d99244cd82bb18764cebf838c5d78a221.cpp -o /tmp/weave-ubuntu-4j0bU_/python27_intermediate/compiler_42af0de1ac3c9a329eed61392ee41a0d/home/ubuntu/.cache/weave/python27_compiled/sc_d99244cd82bb18764cebf838c5d78a221.o -MMD -MF /tmp/weave-ubuntu-4j0bU_/python27_intermediate/compiler_42af0de1ac3c9a329eed61392ee41a0d/home/ubuntu/.cache/weave/python27_compiled/sc_d99244cd82bb18764cebf838c5d78a221.o.d -O3 -ffast-math -march=native" failed with exit status 1
x86_64-linux-gnu-g++: error: unrecognized command line option ‘-ffast-math -march=native’; did you mean ‘-fsso-struct=native’?

```


### random connection result

```
ubuntu@ubuntu-virtual-machine:~/Desktop/brian/brian_one/stdp-mnist-master$ python Diehl\&Cook_MNIST_random_conn_generator.py 
create random connection matrices
create connection matrices from E->I which are purely random
save connection matrix XeAi
create connection matrices from E->I which are purely random
save connection matrix AeAi
create connection matrices from I->E which are purely random
save connection matrix AiAe

```


### b.run() error, g++ command error

```
time needed to load test set: 4.91405200958
brian.stateupdater: WARNING  Using codegen CStateUpdater
brian.stateupdater: WARNING  Using codegen CStateUpdater
create neuron group A
create recurrent connections
(400, 3) ./weights/../random/AeAi.npy
(160000, 3) ./weights/../random/AiAe.npy
create monitors for A
create connections between X and A
(313600, 3) ./weights/XeAe.npy
x86_64-linux-gnu-g++: error: unrecognized command line option ‘-ffast-math -march=native’; did you mean ‘-fsso-struct=native’?
brian.experimental.codegen.stateupdaters: WARNING  C compilation failed, falling back on Python.
x86_64-linux-gnu-g++: error: unrecognized command line option ‘-ffast-math -march=native’; did you mean ‘-fsso-struct=native’?
x86_64-linux-gnu-g++: error: unrecognized command line option ‘-ffast-math -march=native’; did you mean ‘-fsso-struct=native’?
brian.experimental.codegen.stateupdaters: WARNING  C compilation failed, falling back on Python.
x86_64-linux-gnu-g++: error: unrecognized command line option ‘-ffast-math -march=native’; did you mean ‘-fsso-struct=native’?
x86_64-linux-gnu-g++: error: unrecognized command line option ‘-ffast-math -march=native’; did you mean ‘-fsso-struct=native’?
Traceback (most recent call last):
  File "Diehl&Cook_spiking_MNIST.py", line 455, in <module>
    b.run(single_example_time, report='text')
  File "/home/ubuntu/.local/lib/python2.7/site-packages/brian/network.py", line 938, in run
    report=report, report_period=report_period)
  File "/home/ubuntu/.local/lib/python2.7/site-packages/brian/network.py", line 574, in run
    self.update()
  File "/home/ubuntu/.local/lib/python2.7/site-packages/brian/network.py", line 518, in update
    f()
  File "/home/ubuntu/.local/lib/python2.7/site-packages/brian/neurongroup.py", line 501, in update
    spikes = self._threshold(self) # get spikes
  File "/home/ubuntu/.local/lib/python2.7/site-packages/brian/threshold.py", line 186, in __call__
    extra_compile_args=self._extra_compile_args)
  File "/home/ubuntu/.local/lib/python2.7/site-packages/weave/inline_tools.py", line 370, in inline
    **kw)
  File "/home/ubuntu/.local/lib/python2.7/site-packages/weave/inline_tools.py", line 500, in compile_function
    verbose=verbose, **kw)
  File "/home/ubuntu/.local/lib/python2.7/site-packages/weave/ext_tools.py", line 373, in compile
    verbose=verbose, **kw)
  File "/home/ubuntu/.local/lib/python2.7/site-packages/weave/build_tools.py", line 279, in build_extension
    setup(name=module_name, ext_modules=[ext],verbose=verb)
  File "/home/ubuntu/.local/lib/python2.7/site-packages/numpy/distutils/core.py", line 171, in setup
    return old_setup(**new_attr)
  File "/usr/lib/python2.7/distutils/core.py", line 166, in setup
    raise SystemExit, "error: " + str(msg)
weave.build_tools.CompileError: error: Command "x86_64-linux-gnu-g++ -pthread -fno-strict-aliasing -Wdate-time -D_FORTIFY_SOURCE=2 -g -fdebug-prefix-map=/build/python2.7-gnDdqE/python2.7-2.7.17=. -fstack-protector-strong -Wformat -Werror=format-security -fPIC -I/home/ubuntu/.local/lib/python2.7/site-packages/weave -I/home/ubuntu/.local/lib/python2.7/site-packages/weave/scxx -I/home/ubuntu/.local/lib/python2.7/site-packages/weave/blitz -I/home/ubuntu/.local/lib/python2.7/site-packages/numpy/core/include -I/usr/include/python2.7 -c /home/ubuntu/.local/lib/python2.7/site-packages/weave/scxx/weave_imp.cpp -o /tmp/weave-ubuntu-4j0bU_/python27_intermediate/compiler_42af0de1ac3c9a329eed61392ee41a0d/home/ubuntu/.local/lib/python2.7/site-packages/weave/scxx/weave_imp.o -MMD -MF /tmp/weave-ubuntu-4j0bU_/python27_intermediate/compiler_42af0de1ac3c9a329eed61392ee41a0d/home/ubuntu/.local/lib/python2.7/site-packages/weave/scxx/weave_imp.o.d -O3 -ffast-math -march=native" failed with exit status 1
x86_64-linux-gnu-g++: error: unrecognized command line option ‘-ffast-math -march=native’; did you mean ‘-fsso-struct=native’?

```



### when gcc, g++ doesn't exist

```
brian.experimental.codegen.stateupdaters: WARNING  C compilation failed, falling back on Python.
brian.experimental.codegen.stateupdaters: WARNING  C compilation failed, falling back on Python.
Traceback (most recent call last):
  File "Diehl&Cook_spiking_MNIST.py", line 455, in <module>
    b.run(single_example_time, report='text')
  File "/home/ubuntu/.local/lib/python2.7/site-packages/brian/network.py", line 938, in run
    report=report, report_period=report_period)
  File "/home/ubuntu/.local/lib/python2.7/site-packages/brian/network.py", line 574, in run
    self.update()
  File "/home/ubuntu/.local/lib/python2.7/site-packages/brian/network.py", line 518, in update
    f()
  File "/home/ubuntu/.local/lib/python2.7/site-packages/brian/neurongroup.py", line 501, in update
    spikes = self._threshold(self) # get spikes
  File "/home/ubuntu/.local/lib/python2.7/site-packages/brian/threshold.py", line 186, in __call__
    extra_compile_args=self._extra_compile_args)
  File "/home/ubuntu/.local/lib/python2.7/site-packages/weave/inline_tools.py", line 370, in inline
    **kw)
  File "/home/ubuntu/.local/lib/python2.7/site-packages/weave/inline_tools.py", line 500, in compile_function
    verbose=verbose, **kw)
  File "/home/ubuntu/.local/lib/python2.7/site-packages/weave/ext_tools.py", line 373, in compile
    verbose=verbose, **kw)
  File "/home/ubuntu/.local/lib/python2.7/site-packages/weave/build_tools.py", line 279, in build_extension
    setup(name=module_name, ext_modules=[ext],verbose=verb)
  File "/home/ubuntu/.local/lib/python2.7/site-packages/numpy/distutils/core.py", line 171, in setup
    return old_setup(**new_attr)
  File "/usr/lib/python2.7/distutils/core.py", line 166, in setup
    raise SystemExit, "error: " + str(msg)
weave.build_tools.CompileError: error: Command "x86_64-linux-gnu-g++ -pthread -fno-strict-aliasing -Wdate-time -D_FORTIFY_SOURCE=2 -g -fdebug-prefix-map=/build/python2.7-gnDdqE/python2.7-2.7.17=. -fstack-protector-strong -Wformat -Werror=format-security -fPIC -I/home/ubuntu/.local/lib/python2.7/site-packages/weave -I/home/ubuntu/.local/lib/python2.7/site-packages/weave/scxx -I/home/ubuntu/.local/lib/python2.7/site-packages/weave/blitz -I/home/ubuntu/.local/lib/python2.7/site-packages/numpy/core/include -I/usr/include/python2.7 -c /home/ubuntu/.cache/weave/python27_compiled/sc_d99244cd82bb18764cebf838c5d78a2212.cpp -o /tmp/weave-ubuntu-4j0bU_/python27_intermediate/compiler_42af0de1ac3c9a329eed61392ee41a0d/home/ubuntu/.cache/weave/python27_compiled/sc_d99244cd82bb18764cebf838c5d78a2212.o -MMD -MF /tmp/weave-ubuntu-4j0bU_/python27_intermediate/compiler_42af0de1ac3c9a329eed61392ee41a0d/home/ubuntu/.cache/weave/python27_compiled/sc_d99244cd82bb18764cebf838c5d78a2212.o.d -O3 -ffast-math -march=native" failed with exit status 127

```




### after installing gcc/g++ compiler 5

```
brian.experimental.codegen.stateupdaters: WARNING  C compilation failed, falling back on Python.
brian.experimental.codegen.stateupdaters: WARNING  C compilation failed, falling back on Python.
Traceback (most recent call last):
  File "Diehl&Cook_spiking_MNIST.py", line 455, in <module>
    b.run(single_example_time, report='text')
  File "/home/ubuntu/.local/lib/python2.7/site-packages/brian/network.py", line 938, in run
    report=report, report_period=report_period)
  File "/home/ubuntu/.local/lib/python2.7/site-packages/brian/network.py", line 574, in run
    self.update()
  File "/home/ubuntu/.local/lib/python2.7/site-packages/brian/network.py", line 518, in update
    f()
  File "/home/ubuntu/.local/lib/python2.7/site-packages/brian/neurongroup.py", line 501, in update
    spikes = self._threshold(self) # get spikes
  File "/home/ubuntu/.local/lib/python2.7/site-packages/brian/threshold.py", line 186, in __call__
    extra_compile_args=self._extra_compile_args)
  File "/home/ubuntu/.local/lib/python2.7/site-packages/weave/inline_tools.py", line 370, in inline
    **kw)
  File "/home/ubuntu/.local/lib/python2.7/site-packages/weave/inline_tools.py", line 500, in compile_function
    verbose=verbose, **kw)
  File "/home/ubuntu/.local/lib/python2.7/site-packages/weave/ext_tools.py", line 373, in compile
    verbose=verbose, **kw)
  File "/home/ubuntu/.local/lib/python2.7/site-packages/weave/build_tools.py", line 242, in build_extension
    compiler_dir = platform_info.get_compiler_dir(compiler_name)
  File "/home/ubuntu/.local/lib/python2.7/site-packages/weave/platform_info.py", line 125, in get_compiler_dir
    raise ValueError("The '%s' compiler was not found." % compiler_name)
ValueError: The 'gcc' compiler was not found.
```

