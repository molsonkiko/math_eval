# Change Log
All notable changes to this project will be documented in this file.
 
The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).
 
## [Unreleased] - yyyy-mm-dd
 
### To Be Added

- Maybe consider adding support for comma-separated arguments for functions.
At that point I might as well just also add tuples and lists.


## [0.2.3] - 2021-10-17

math_eval version 0.2.3 is now available on the Python package index. It has 
been tested for Python 3.6 to 3.9.

## Changed
- Fixed bug where using the unary "-" in combination with slicing \[\]
would raise an uninformative error message instead of returning the
correct value. Now `compute("-x[0]")([1])` will return -1 rather than an error.

- Added `iterable()` function to `compute()`, which takes a backtick-enclosed string literal as argument and invokes [`ast.literal_eval()`](https://docs.python.org/3/library/ast.html?highlight=literal_eval#ast.literal_eval).

## [0.2.1] - 2021-10-12

## Changed
- Add support for bool and fractions.Fraction types to safe_compute.
Note that subtypes of those classes will NOT be supported, and there are
not plans to change this. Fraction, int, float, Decimal, bool, and commplex
cover all the types of numbers that anyone might reasonably need, 
including special values like float('nan') and math.inf.

## [0.2.0] - 2021-10-08
  
math_eval version 0.2.0, is now available on the Python package index. It has 
been tested for Python 3.6 to 3.9.
 
### Changed

- Changed the map function so that it runs much faster.
For example, consider fun = compute("``x*2`` map y").
This worked before, and it works now.
But previously, if I called fun(itbl), resolve_binop would call compute("x\*2"),
incurring a time cost of about 40 microseconds.
If you're calling fun on a lot of iterables, this adds up.
In the current version, compute("x\*2") is called once as fun is being defined.
Every subsequent time fun is called, the super-fast-running function produced
by compute("x\*2") is run.


## [0.1.0] - 2021-10-02
 
### Added

- Initial commit, although unfortunately the repository no longer exists.
You can still get the source code for 0.1.0 from the Python package index.
There's no reason to do so though, and it's almost identical to the current
code.