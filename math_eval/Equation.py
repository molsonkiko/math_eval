'''Python 2 had a package on the PYPI called Equation that did something like
safe_compute. This is a revival of that.
The Equation class is more or less a wrapper around safe_compute with
some extra math functions thrown in.
Every single-variable function in Python's built-in "math" module 
is available for use here.
'''
from math import *
import math
from .math_eval import *

one_arg_mathfuncs = {}

for funcname in dir(math):
    func = globals()[funcname]
    try:
        func(2)
        one_arg_mathfuncs[funcname] = func
    except:
        pass
safe_ufunctions.update(one_arg_mathfuncs)
ufunctions.update(one_arg_mathfuncs)

class Equation:
    def __init__(self, eqn):
        self.eqn = eqn
        self.expr = compute(eqn, safe = True)
        self.varnames = get_varnames(tokenize(eqn), safe = True)
        
    def __call__(self, *args):
        return self.expr(*args)
        
    def __repr__(self):
        return f"Equation({self.eqn})"
    __str__ = __repr__