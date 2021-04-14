# coverage-recursion-error

install package from requirements.txt

and run:

```
python3 -m pytest --cov=src
```

RecursionError gain when

.coveragerc
```
[run]
branch = True
```

If false - it finished successful
