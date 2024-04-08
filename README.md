# <p align="center">`dovekie`</p>

<p align="center">
    <a href="https://github.com/codereport/dovekie/issues" alt="contributions welcome">
        <img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat" /></a>
    <a href="https://lbesson.mit-license.org/" alt="MIT license">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" /></a>    
    <a href="https://www.python.org/">
        <img src="https://img.shields.io/badge/Python-3-ff69b4.svg"/></a>
    <a href="https://github.com/codereport?tab=followers" alt="GitHub followers">
        <img src="https://img.shields.io/github/followers/codereport.svg?style=social&label=Follow" /></a>
    <a href="https://GitHub.com/codereport/dovekie/stargazers/" alt="GitHub stars">
        <img src="https://img.shields.io/github/stars/codereport/dovekie.svg?style=social&label=Star" /></a>
    <a href="https://twitter.com/code_report" alt="Twitter">
        <img src="https://img.shields.io/twitter/follow/code_report.svg?style=social&label=@code_report" /></a>
</p>

`dovekie` is a [Python](https://www.python.org/) library that provides SKI combinators from [Combinatory Logic](https://combinatorylogic.com/) and common unary and binary functions that are often used with these combinators. It is the spiritual equivalent of the:

* C++ [`blackbird` library](https://github.com/codereport/blackbird)
* Rust [`bluebird` library](https://github.com/codereport/bluebird)

<p align="center">
  <img src="https://github.com/codereport/dovekie/assets/36027403/3a51f52e-165c-40e0-a3e0-6318915cef8f" alt="image-removebg-preview">
</p>

How to install:
```bash
pip3 install dovekie
```

And how to use:
```py
import operator as op
from itertools import accumulate

import dovekie as d


def mco(xs: list[int]) -> int:
    return max(accumulate(xs, d.phi1(op.add, op.mul, d.r)))

print(mco([1, 0, 1, 1, 1, 0, 0, 1, 1, 0])) # 3
```
