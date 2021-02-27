# `scf` documentation

`scf` is a Python package for working with Survey of Consumer Finances microdata.

Install via:

```
pip install git+https://github.com/PSLmodels/scf.git
```

Try it with:
```
import scf

scf.load(years=[2016, 2019], columns=['income', 'networth'])
```

This will return a `pandas` `DataFrame` with columns for
`income`, `networth`, `year`, and `wgt` (the survey weight).
