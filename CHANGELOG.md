# Change Log
All notable changes to this project will be documented in this file.
 
The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).
 
## [Unreleased] - yyyy-mm-dd
 
### To Be Added

- Maybe consider adding support for comma-separated arguments for functions.
At that point I might as well just also add tuples and lists.

- Alternatively, maybe add an "iterable" function that takes a single string
argument and runs ast.literal_eval on it. That way I don't need to figure out
how to make iterables on my own.
 
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

- Initial commit.