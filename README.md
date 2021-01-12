# Pipe.py

A non-intrusive Python pipeline. 

There are only pipeline. If you want more functional tools, you should look for another library.

## Install

```
pip install only-pipe
```

Or fetch from github

```
pip install git+https://github.com/abersheeran/only-pipe
```

## Usage

Use pipeline to pass data as a positional parameter to the next function:

```python
from pipe import F

range(10) | F(filter, lambda x: x % 2) | F(sum) == 25
```

Or you need to pass multiple parameters through the pipeline:

```python
from pipe import FF


def get_data():
    return 1, 2


get_data() | FF(lambda x, y: x + y) == 3
```

Use alias like follow code, you can use `map`/`filter`/`reduce` more conveniently:

```python
from functools import reduce
from pipe import F

Filter = F(F, filter)
Map = F(F, map)
Reduce = F(F, reduce)

range(100) | Filter(lambda x: x % 2) | Map(lambda x: x * x) | Reduce(lambda x, y: x + y)
```

## Set Global

Maybe you don't want to use `from pipe import F` in every file of the entire project, you can use the following code to set it as a global function, just like `min`/`max`/`sum`.

```python
import pipe

pipe.set_global(pipe.F, pipe.FF)
```

Maybe you also want to expose `functools.reduce` to the world, just like `map`/`filter`.

```python
import pipe
import functools

pipe.set_global(pipe.F, pipe.FF, functools.reduce)
```

## More

No more ~ This library has less than ten lines of valid code, but it is very effective. 

If you like it, please give a Star. 😀

This repository is released under the MIT. Do what you want!
