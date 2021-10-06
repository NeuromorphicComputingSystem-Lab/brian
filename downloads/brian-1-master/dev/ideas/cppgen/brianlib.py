# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.33
#
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _brianlib
import new
new_instancemethod = new.instancemethod
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method: return method(self, value)
    if (not static) or hasattr(self, name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)

def _swig_getattr(self, class_type, name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method: return method(self)
    raise AttributeError, name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


class PySwigIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PySwigIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PySwigIterator, name)
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _brianlib.delete_PySwigIterator
    __del__ = lambda self : None;
    def value(*args): return _brianlib.PySwigIterator_value(*args)
    def incr(*args): return _brianlib.PySwigIterator_incr(*args)
    def decr(*args): return _brianlib.PySwigIterator_decr(*args)
    def distance(*args): return _brianlib.PySwigIterator_distance(*args)
    def equal(*args): return _brianlib.PySwigIterator_equal(*args)
    def copy(*args): return _brianlib.PySwigIterator_copy(*args)
    def next(*args): return _brianlib.PySwigIterator_next(*args)
    def previous(*args): return _brianlib.PySwigIterator_previous(*args)
    def advance(*args): return _brianlib.PySwigIterator_advance(*args)
    def __eq__(*args): return _brianlib.PySwigIterator___eq__(*args)
    def __ne__(*args): return _brianlib.PySwigIterator___ne__(*args)
    def __iadd__(*args): return _brianlib.PySwigIterator___iadd__(*args)
    def __isub__(*args): return _brianlib.PySwigIterator___isub__(*args)
    def __add__(*args): return _brianlib.PySwigIterator___add__(*args)
    def __sub__(*args): return _brianlib.PySwigIterator___sub__(*args)
    def __iter__(self): return self
PySwigIterator_swigregister = _brianlib.PySwigIterator_swigregister
PySwigIterator_swigregister(PySwigIterator)

class SpikeList(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SpikeList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SpikeList, name)
    __repr__ = _swig_repr
    def iterator(*args): return _brianlib.SpikeList_iterator(*args)
    def __iter__(self): return self.iterator()
    def __nonzero__(*args): return _brianlib.SpikeList___nonzero__(*args)
    def __len__(*args): return _brianlib.SpikeList___len__(*args)
    def pop(*args): return _brianlib.SpikeList_pop(*args)
    def __getslice__(*args): return _brianlib.SpikeList___getslice__(*args)
    def __setslice__(*args): return _brianlib.SpikeList___setslice__(*args)
    def __delslice__(*args): return _brianlib.SpikeList___delslice__(*args)
    def __delitem__(*args): return _brianlib.SpikeList___delitem__(*args)
    def __getitem__(*args): return _brianlib.SpikeList___getitem__(*args)
    def __setitem__(*args): return _brianlib.SpikeList___setitem__(*args)
    def append(*args): return _brianlib.SpikeList_append(*args)
    def empty(*args): return _brianlib.SpikeList_empty(*args)
    def size(*args): return _brianlib.SpikeList_size(*args)
    def clear(*args): return _brianlib.SpikeList_clear(*args)
    def swap(*args): return _brianlib.SpikeList_swap(*args)
    def get_allocator(*args): return _brianlib.SpikeList_get_allocator(*args)
    def begin(*args): return _brianlib.SpikeList_begin(*args)
    def end(*args): return _brianlib.SpikeList_end(*args)
    def rbegin(*args): return _brianlib.SpikeList_rbegin(*args)
    def rend(*args): return _brianlib.SpikeList_rend(*args)
    def pop_back(*args): return _brianlib.SpikeList_pop_back(*args)
    def erase(*args): return _brianlib.SpikeList_erase(*args)
    def __init__(self, *args):
        this = _brianlib.new_SpikeList(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(*args): return _brianlib.SpikeList_push_back(*args)
    def front(*args): return _brianlib.SpikeList_front(*args)
    def back(*args): return _brianlib.SpikeList_back(*args)
    def assign(*args): return _brianlib.SpikeList_assign(*args)
    def resize(*args): return _brianlib.SpikeList_resize(*args)
    def insert(*args): return _brianlib.SpikeList_insert(*args)
    def pop_front(*args): return _brianlib.SpikeList_pop_front(*args)
    def push_front(*args): return _brianlib.SpikeList_push_front(*args)
    def reverse(*args): return _brianlib.SpikeList_reverse(*args)
    __swig_destroy__ = _brianlib.delete_SpikeList
    __del__ = lambda self : None;
SpikeList_swigregister = _brianlib.SpikeList_swigregister
SpikeList_swigregister(SpikeList)

class VectorDouble(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VectorDouble, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VectorDouble, name)
    __repr__ = _swig_repr
    def iterator(*args): return _brianlib.VectorDouble_iterator(*args)
    def __iter__(self): return self.iterator()
    def __nonzero__(*args): return _brianlib.VectorDouble___nonzero__(*args)
    def __len__(*args): return _brianlib.VectorDouble___len__(*args)
    def pop(*args): return _brianlib.VectorDouble_pop(*args)
    def __getslice__(*args): return _brianlib.VectorDouble___getslice__(*args)
    def __setslice__(*args): return _brianlib.VectorDouble___setslice__(*args)
    def __delslice__(*args): return _brianlib.VectorDouble___delslice__(*args)
    def __delitem__(*args): return _brianlib.VectorDouble___delitem__(*args)
    def __getitem__(*args): return _brianlib.VectorDouble___getitem__(*args)
    def __setitem__(*args): return _brianlib.VectorDouble___setitem__(*args)
    def append(*args): return _brianlib.VectorDouble_append(*args)
    def empty(*args): return _brianlib.VectorDouble_empty(*args)
    def size(*args): return _brianlib.VectorDouble_size(*args)
    def clear(*args): return _brianlib.VectorDouble_clear(*args)
    def swap(*args): return _brianlib.VectorDouble_swap(*args)
    def get_allocator(*args): return _brianlib.VectorDouble_get_allocator(*args)
    def begin(*args): return _brianlib.VectorDouble_begin(*args)
    def end(*args): return _brianlib.VectorDouble_end(*args)
    def rbegin(*args): return _brianlib.VectorDouble_rbegin(*args)
    def rend(*args): return _brianlib.VectorDouble_rend(*args)
    def pop_back(*args): return _brianlib.VectorDouble_pop_back(*args)
    def erase(*args): return _brianlib.VectorDouble_erase(*args)
    def __init__(self, *args):
        this = _brianlib.new_VectorDouble(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(*args): return _brianlib.VectorDouble_push_back(*args)
    def front(*args): return _brianlib.VectorDouble_front(*args)
    def back(*args): return _brianlib.VectorDouble_back(*args)
    def assign(*args): return _brianlib.VectorDouble_assign(*args)
    def resize(*args): return _brianlib.VectorDouble_resize(*args)
    def insert(*args): return _brianlib.VectorDouble_insert(*args)
    def reserve(*args): return _brianlib.VectorDouble_reserve(*args)
    def capacity(*args): return _brianlib.VectorDouble_capacity(*args)
    __swig_destroy__ = _brianlib.delete_VectorDouble
    __del__ = lambda self : None;
VectorDouble_swigregister = _brianlib.VectorDouble_swigregister
VectorDouble_swigregister(VectorDouble)

class NeuronGroup(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, NeuronGroup, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, NeuronGroup, name)
    __repr__ = _swig_repr
    __swig_setmethods__["S"] = _brianlib.NeuronGroup_S_set
    __swig_getmethods__["S"] = _brianlib.NeuronGroup_S_get
    if _newclass:S = _swig_property(_brianlib.NeuronGroup_S_get, _brianlib.NeuronGroup_S_set)
    __swig_setmethods__["num_vars"] = _brianlib.NeuronGroup_num_vars_set
    __swig_getmethods__["num_vars"] = _brianlib.NeuronGroup_num_vars_get
    if _newclass:num_vars = _swig_property(_brianlib.NeuronGroup_num_vars_get, _brianlib.NeuronGroup_num_vars_set)
    __swig_setmethods__["num_neurons"] = _brianlib.NeuronGroup_num_neurons_set
    __swig_getmethods__["num_neurons"] = _brianlib.NeuronGroup_num_neurons_get
    if _newclass:num_neurons = _swig_property(_brianlib.NeuronGroup_num_neurons_get, _brianlib.NeuronGroup_num_neurons_set)
    __swig_setmethods__["S_m"] = _brianlib.NeuronGroup_S_m_set
    __swig_getmethods__["S_m"] = _brianlib.NeuronGroup_S_m_get
    if _newclass:S_m = _swig_property(_brianlib.NeuronGroup_S_m_get, _brianlib.NeuronGroup_S_m_set)
    __swig_setmethods__["su"] = _brianlib.NeuronGroup_su_set
    __swig_getmethods__["su"] = _brianlib.NeuronGroup_su_get
    if _newclass:su = _swig_property(_brianlib.NeuronGroup_su_get, _brianlib.NeuronGroup_su_set)
    __swig_setmethods__["thr"] = _brianlib.NeuronGroup_thr_set
    __swig_getmethods__["thr"] = _brianlib.NeuronGroup_thr_get
    if _newclass:thr = _swig_property(_brianlib.NeuronGroup_thr_get, _brianlib.NeuronGroup_thr_set)
    __swig_setmethods__["resetobj"] = _brianlib.NeuronGroup_resetobj_set
    __swig_getmethods__["resetobj"] = _brianlib.NeuronGroup_resetobj_get
    if _newclass:resetobj = _swig_property(_brianlib.NeuronGroup_resetobj_get, _brianlib.NeuronGroup_resetobj_set)
    __swig_setmethods__["LS"] = _brianlib.NeuronGroup_LS_set
    __swig_getmethods__["LS"] = _brianlib.NeuronGroup_LS_get
    if _newclass:LS = _swig_property(_brianlib.NeuronGroup_LS_get, _brianlib.NeuronGroup_LS_set)
    __swig_setmethods__["spikesarray"] = _brianlib.NeuronGroup_spikesarray_set
    __swig_getmethods__["spikesarray"] = _brianlib.NeuronGroup_spikesarray_get
    if _newclass:spikesarray = _swig_property(_brianlib.NeuronGroup_spikesarray_get, _brianlib.NeuronGroup_spikesarray_set)
    __swig_setmethods__["owner"] = _brianlib.NeuronGroup_owner_set
    __swig_getmethods__["owner"] = _brianlib.NeuronGroup_owner_get
    if _newclass:owner = _swig_property(_brianlib.NeuronGroup_owner_get, _brianlib.NeuronGroup_owner_set)
    __swig_setmethods__["origin"] = _brianlib.NeuronGroup_origin_set
    __swig_getmethods__["origin"] = _brianlib.NeuronGroup_origin_get
    if _newclass:origin = _swig_property(_brianlib.NeuronGroup_origin_get, _brianlib.NeuronGroup_origin_set)
    def __init__(self, *args):
        this = _brianlib.new_NeuronGroup(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _brianlib.delete_NeuronGroup
    __del__ = lambda self : None;
    def get_spikes(*args): return _brianlib.NeuronGroup_get_spikes(*args)
    def update(*args): return _brianlib.NeuronGroup_update(*args)
    def reset(*args): return _brianlib.NeuronGroup_reset(*args)
NeuronGroup_swigregister = _brianlib.NeuronGroup_swigregister
NeuronGroup_swigregister(NeuronGroup)

class StateUpdater(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, StateUpdater, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, StateUpdater, name)
    __repr__ = _swig_repr
    def __call__(*args): return _brianlib.StateUpdater___call__(*args)
    def __init__(self, *args):
        this = _brianlib.new_StateUpdater(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _brianlib.delete_StateUpdater
    __del__ = lambda self : None;
StateUpdater_swigregister = _brianlib.StateUpdater_swigregister
StateUpdater_swigregister(StateUpdater)

class LinearStateUpdater(StateUpdater):
    __swig_setmethods__ = {}
    for _s in [StateUpdater]: __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, LinearStateUpdater, name, value)
    __swig_getmethods__ = {}
    for _s in [StateUpdater]: __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, LinearStateUpdater, name)
    __swig_setmethods__["M"] = _brianlib.LinearStateUpdater_M_set
    __swig_getmethods__["M"] = _brianlib.LinearStateUpdater_M_get
    if _newclass:M = _swig_property(_brianlib.LinearStateUpdater_M_get, _brianlib.LinearStateUpdater_M_set)
    __swig_setmethods__["M_n"] = _brianlib.LinearStateUpdater_M_n_set
    __swig_getmethods__["M_n"] = _brianlib.LinearStateUpdater_M_n_get
    if _newclass:M_n = _swig_property(_brianlib.LinearStateUpdater_M_n_get, _brianlib.LinearStateUpdater_M_n_set)
    __swig_setmethods__["M_m"] = _brianlib.LinearStateUpdater_M_m_set
    __swig_getmethods__["M_m"] = _brianlib.LinearStateUpdater_M_m_get
    if _newclass:M_m = _swig_property(_brianlib.LinearStateUpdater_M_m_get, _brianlib.LinearStateUpdater_M_m_set)
    __swig_setmethods__["b"] = _brianlib.LinearStateUpdater_b_set
    __swig_getmethods__["b"] = _brianlib.LinearStateUpdater_b_get
    if _newclass:b = _swig_property(_brianlib.LinearStateUpdater_b_get, _brianlib.LinearStateUpdater_b_set)
    __swig_setmethods__["b_n"] = _brianlib.LinearStateUpdater_b_n_set
    __swig_getmethods__["b_n"] = _brianlib.LinearStateUpdater_b_n_get
    if _newclass:b_n = _swig_property(_brianlib.LinearStateUpdater_b_n_get, _brianlib.LinearStateUpdater_b_n_set)
    def __init__(self, *args):
        this = _brianlib.new_LinearStateUpdater(*args)
        try: self.this.append(this)
        except: self.this = this
    def __call__(*args): return _brianlib.LinearStateUpdater___call__(*args)
    def __repr__(*args): return _brianlib.LinearStateUpdater___repr__(*args)
    __swig_destroy__ = _brianlib.delete_LinearStateUpdater
    __del__ = lambda self : None;
LinearStateUpdater_swigregister = _brianlib.LinearStateUpdater_swigregister
LinearStateUpdater_swigregister(LinearStateUpdater)

class Threshold(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Threshold, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Threshold, name)
    __repr__ = _swig_repr
    __swig_setmethods__["value"] = _brianlib.Threshold_value_set
    __swig_getmethods__["value"] = _brianlib.Threshold_value_get
    if _newclass:value = _swig_property(_brianlib.Threshold_value_get, _brianlib.Threshold_value_set)
    __swig_setmethods__["state"] = _brianlib.Threshold_state_set
    __swig_getmethods__["state"] = _brianlib.Threshold_state_get
    if _newclass:state = _swig_property(_brianlib.Threshold_state_get, _brianlib.Threshold_state_set)
    def __init__(self, *args):
        this = _brianlib.new_Threshold(*args)
        try: self.this.append(this)
        except: self.this = this
    def __call__(*args): return _brianlib.Threshold___call__(*args)
    __swig_destroy__ = _brianlib.delete_Threshold
    __del__ = lambda self : None;
Threshold_swigregister = _brianlib.Threshold_swigregister
Threshold_swigregister(Threshold)

class ResetBase(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ResetBase, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ResetBase, name)
    __repr__ = _swig_repr
    def __call__(*args): return _brianlib.ResetBase___call__(*args)
    def __init__(self, *args):
        this = _brianlib.new_ResetBase(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _brianlib.delete_ResetBase
    __del__ = lambda self : None;
ResetBase_swigregister = _brianlib.ResetBase_swigregister
ResetBase_swigregister(ResetBase)

class Reset(ResetBase):
    __swig_setmethods__ = {}
    for _s in [ResetBase]: __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Reset, name, value)
    __swig_getmethods__ = {}
    for _s in [ResetBase]: __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, Reset, name)
    __repr__ = _swig_repr
    __swig_setmethods__["value"] = _brianlib.Reset_value_set
    __swig_getmethods__["value"] = _brianlib.Reset_value_get
    if _newclass:value = _swig_property(_brianlib.Reset_value_get, _brianlib.Reset_value_set)
    __swig_setmethods__["state"] = _brianlib.Reset_state_set
    __swig_getmethods__["state"] = _brianlib.Reset_state_get
    if _newclass:state = _swig_property(_brianlib.Reset_state_get, _brianlib.Reset_state_set)
    def __init__(self, *args):
        this = _brianlib.new_Reset(*args)
        try: self.this.append(this)
        except: self.this = this
    def __call__(*args): return _brianlib.Reset___call__(*args)
    __swig_destroy__ = _brianlib.delete_Reset
    __del__ = lambda self : None;
Reset_swigregister = _brianlib.Reset_swigregister
Reset_swigregister(Reset)

class Refractoriness(Reset):
    __swig_setmethods__ = {}
    for _s in [Reset]: __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Refractoriness, name, value)
    __swig_getmethods__ = {}
    for _s in [Reset]: __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, Refractoriness, name)
    __repr__ = _swig_repr
    __swig_setmethods__["period"] = _brianlib.Refractoriness_period_set
    __swig_getmethods__["period"] = _brianlib.Refractoriness_period_get
    if _newclass:period = _swig_property(_brianlib.Refractoriness_period_get, _brianlib.Refractoriness_period_set)
    def __init__(self, *args):
        this = _brianlib.new_Refractoriness(*args)
        try: self.this.append(this)
        except: self.this = this
    def __call__(*args): return _brianlib.Refractoriness___call__(*args)
    __swig_destroy__ = _brianlib.delete_Refractoriness
    __del__ = lambda self : None;
Refractoriness_swigregister = _brianlib.Refractoriness_swigregister
Refractoriness_swigregister(Refractoriness)

class NetworkOperation(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, NetworkOperation, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, NetworkOperation, name)
    __repr__ = _swig_repr
    def __call__(*args): return _brianlib.NetworkOperation___call__(*args)
    def __init__(self, *args):
        this = _brianlib.new_NetworkOperation(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _brianlib.delete_NetworkOperation
    __del__ = lambda self : None;
NetworkOperation_swigregister = _brianlib.NetworkOperation_swigregister
NetworkOperation_swigregister(NetworkOperation)

class StateMonitor(NetworkOperation):
    __swig_setmethods__ = {}
    for _s in [NetworkOperation]: __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, StateMonitor, name, value)
    __swig_getmethods__ = {}
    for _s in [NetworkOperation]: __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, StateMonitor, name)
    __repr__ = _swig_repr
    __swig_setmethods__["group"] = _brianlib.StateMonitor_group_set
    __swig_getmethods__["group"] = _brianlib.StateMonitor_group_get
    if _newclass:group = _swig_property(_brianlib.StateMonitor_group_get, _brianlib.StateMonitor_group_set)
    __swig_setmethods__["state"] = _brianlib.StateMonitor_state_set
    __swig_getmethods__["state"] = _brianlib.StateMonitor_state_get
    if _newclass:state = _swig_property(_brianlib.StateMonitor_state_get, _brianlib.StateMonitor_state_set)
    __swig_setmethods__["values"] = _brianlib.StateMonitor_values_set
    __swig_getmethods__["values"] = _brianlib.StateMonitor_values_get
    if _newclass:values = _swig_property(_brianlib.StateMonitor_values_get, _brianlib.StateMonitor_values_set)
    def __init__(self, *args):
        this = _brianlib.new_StateMonitor(*args)
        try: self.this.append(this)
        except: self.this = this
    def __call__(*args): return _brianlib.StateMonitor___call__(*args)
    def __getitem__(*args): return _brianlib.StateMonitor___getitem__(*args)
    __swig_destroy__ = _brianlib.delete_StateMonitor
    __del__ = lambda self : None;
StateMonitor_swigregister = _brianlib.StateMonitor_swigregister
StateMonitor_swigregister(StateMonitor)

class Network(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Network, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Network, name)
    __repr__ = _swig_repr
    __swig_setmethods__["groups"] = _brianlib.Network_groups_set
    __swig_getmethods__["groups"] = _brianlib.Network_groups_get
    if _newclass:groups = _swig_property(_brianlib.Network_groups_get, _brianlib.Network_groups_set)
    __swig_setmethods__["operations"] = _brianlib.Network_operations_set
    __swig_getmethods__["operations"] = _brianlib.Network_operations_get
    if _newclass:operations = _swig_property(_brianlib.Network_operations_get, _brianlib.Network_operations_set)
    __swig_setmethods__["connections"] = _brianlib.Network_connections_set
    __swig_getmethods__["connections"] = _brianlib.Network_connections_get
    if _newclass:connections = _swig_property(_brianlib.Network_connections_get, _brianlib.Network_connections_set)
    def add(*args): return _brianlib.Network_add(*args)
    def update(*args): return _brianlib.Network_update(*args)
    def run(*args): return _brianlib.Network_run(*args)
    def __init__(self, *args):
        this = _brianlib.new_Network(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _brianlib.delete_Network
    __del__ = lambda self : None;
Network_swigregister = _brianlib.Network_swigregister
Network_swigregister(Network)

class CircularVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CircularVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CircularVector, name)
    __swig_setmethods__["X"] = _brianlib.CircularVector_X_set
    __swig_getmethods__["X"] = _brianlib.CircularVector_X_get
    if _newclass:X = _swig_property(_brianlib.CircularVector_X_get, _brianlib.CircularVector_X_set)
    __swig_setmethods__["cursor"] = _brianlib.CircularVector_cursor_set
    __swig_getmethods__["cursor"] = _brianlib.CircularVector_cursor_get
    if _newclass:cursor = _swig_property(_brianlib.CircularVector_cursor_get, _brianlib.CircularVector_cursor_set)
    __swig_setmethods__["n"] = _brianlib.CircularVector_n_set
    __swig_getmethods__["n"] = _brianlib.CircularVector_n_get
    if _newclass:n = _swig_property(_brianlib.CircularVector_n_get, _brianlib.CircularVector_n_set)
    __swig_setmethods__["retarray"] = _brianlib.CircularVector_retarray_set
    __swig_getmethods__["retarray"] = _brianlib.CircularVector_retarray_get
    if _newclass:retarray = _swig_property(_brianlib.CircularVector_retarray_get, _brianlib.CircularVector_retarray_set)
    def __init__(self, *args):
        this = _brianlib.new_CircularVector(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _brianlib.delete_CircularVector
    __del__ = lambda self : None;
    def reinit(*args): return _brianlib.CircularVector_reinit(*args)
    def advance(*args): return _brianlib.CircularVector_advance(*args)
    def __len__(*args): return _brianlib.CircularVector___len__(*args)
    def __getitem__(*args): return _brianlib.CircularVector___getitem__(*args)
    def __setitem__(*args): return _brianlib.CircularVector___setitem__(*args)
    def __getslice__(*args): return _brianlib.CircularVector___getslice__(*args)
    def get_conditional(*args): return _brianlib.CircularVector_get_conditional(*args)
    def __setslice__(*args): return _brianlib.CircularVector___setslice__(*args)
    def __repr__(*args): return _brianlib.CircularVector___repr__(*args)
    def __str__(*args): return _brianlib.CircularVector___str__(*args)
CircularVector_swigregister = _brianlib.CircularVector_swigregister
CircularVector_swigregister(CircularVector)

class SpikeContainer(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SpikeContainer, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SpikeContainer, name)
    __swig_setmethods__["S"] = _brianlib.SpikeContainer_S_set
    __swig_getmethods__["S"] = _brianlib.SpikeContainer_S_get
    if _newclass:S = _swig_property(_brianlib.SpikeContainer_S_get, _brianlib.SpikeContainer_S_set)
    __swig_setmethods__["ind"] = _brianlib.SpikeContainer_ind_set
    __swig_getmethods__["ind"] = _brianlib.SpikeContainer_ind_get
    if _newclass:ind = _swig_property(_brianlib.SpikeContainer_ind_get, _brianlib.SpikeContainer_ind_set)
    def __init__(self, *args):
        this = _brianlib.new_SpikeContainer(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _brianlib.delete_SpikeContainer
    __del__ = lambda self : None;
    def reinit(*args): return _brianlib.SpikeContainer_reinit(*args)
    def push(*args): return _brianlib.SpikeContainer_push(*args)
    def lastspikes(*args): return _brianlib.SpikeContainer_lastspikes(*args)
    def __getitem__(*args): return _brianlib.SpikeContainer___getitem__(*args)
    def get_spikes(*args): return _brianlib.SpikeContainer_get_spikes(*args)
    def __getslice__(*args): return _brianlib.SpikeContainer___getslice__(*args)
    def __repr__(*args): return _brianlib.SpikeContainer___repr__(*args)
    def __str__(*args): return _brianlib.SpikeContainer___str__(*args)
SpikeContainer_swigregister = _brianlib.SpikeContainer_swigregister
SpikeContainer_swigregister(SpikeContainer)

class ConnectionMatrix(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ConnectionMatrix, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ConnectionMatrix, name)
    __repr__ = _swig_repr
    def add_row(*args): return _brianlib.ConnectionMatrix_add_row(*args)
    def add_rows(*args): return _brianlib.ConnectionMatrix_add_rows(*args)
    def __init__(self, *args):
        this = _brianlib.new_ConnectionMatrix(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _brianlib.delete_ConnectionMatrix
    __del__ = lambda self : None;
ConnectionMatrix_swigregister = _brianlib.ConnectionMatrix_swigregister
ConnectionMatrix_swigregister(ConnectionMatrix)

class DenseConnectionMatrix(ConnectionMatrix):
    __swig_setmethods__ = {}
    for _s in [ConnectionMatrix]: __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, DenseConnectionMatrix, name, value)
    __swig_getmethods__ = {}
    for _s in [ConnectionMatrix]: __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, DenseConnectionMatrix, name)
    __repr__ = _swig_repr
    __swig_setmethods__["W"] = _brianlib.DenseConnectionMatrix_W_set
    __swig_getmethods__["W"] = _brianlib.DenseConnectionMatrix_W_get
    if _newclass:W = _swig_property(_brianlib.DenseConnectionMatrix_W_get, _brianlib.DenseConnectionMatrix_W_set)
    __swig_setmethods__["n"] = _brianlib.DenseConnectionMatrix_n_set
    __swig_getmethods__["n"] = _brianlib.DenseConnectionMatrix_n_get
    if _newclass:n = _swig_property(_brianlib.DenseConnectionMatrix_n_get, _brianlib.DenseConnectionMatrix_n_set)
    __swig_setmethods__["m"] = _brianlib.DenseConnectionMatrix_m_set
    __swig_getmethods__["m"] = _brianlib.DenseConnectionMatrix_m_get
    if _newclass:m = _swig_property(_brianlib.DenseConnectionMatrix_m_get, _brianlib.DenseConnectionMatrix_m_set)
    def __init__(self, *args):
        this = _brianlib.new_DenseConnectionMatrix(*args)
        try: self.this.append(this)
        except: self.this = this
    def add_row(*args): return _brianlib.DenseConnectionMatrix_add_row(*args)
    __swig_destroy__ = _brianlib.delete_DenseConnectionMatrix
    __del__ = lambda self : None;
DenseConnectionMatrix_swigregister = _brianlib.DenseConnectionMatrix_swigregister
DenseConnectionMatrix_swigregister(DenseConnectionMatrix)

class Connection(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Connection, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Connection, name)
    __repr__ = _swig_repr
    __swig_setmethods__["source"] = _brianlib.Connection_source_set
    __swig_getmethods__["source"] = _brianlib.Connection_source_get
    if _newclass:source = _swig_property(_brianlib.Connection_source_get, _brianlib.Connection_source_set)
    __swig_setmethods__["target"] = _brianlib.Connection_target_set
    __swig_getmethods__["target"] = _brianlib.Connection_target_get
    if _newclass:target = _swig_property(_brianlib.Connection_target_get, _brianlib.Connection_target_set)
    __swig_setmethods__["connmat"] = _brianlib.Connection_connmat_set
    __swig_getmethods__["connmat"] = _brianlib.Connection_connmat_get
    if _newclass:connmat = _swig_property(_brianlib.Connection_connmat_get, _brianlib.Connection_connmat_set)
    __swig_setmethods__["state"] = _brianlib.Connection_state_set
    __swig_getmethods__["state"] = _brianlib.Connection_state_get
    if _newclass:state = _swig_property(_brianlib.Connection_state_get, _brianlib.Connection_state_set)
    __swig_setmethods__["delay"] = _brianlib.Connection_delay_set
    __swig_getmethods__["delay"] = _brianlib.Connection_delay_get
    if _newclass:delay = _swig_property(_brianlib.Connection_delay_get, _brianlib.Connection_delay_set)
    def __init__(self, *args):
        this = _brianlib.new_Connection(*args)
        try: self.this.append(this)
        except: self.this = this
    def propagate(*args): return _brianlib.Connection_propagate(*args)
    def do_propagate(*args): return _brianlib.Connection_do_propagate(*args)
    __swig_destroy__ = _brianlib.delete_Connection
    __del__ = lambda self : None;
Connection_swigregister = _brianlib.Connection_swigregister
Connection_swigregister(Connection)



