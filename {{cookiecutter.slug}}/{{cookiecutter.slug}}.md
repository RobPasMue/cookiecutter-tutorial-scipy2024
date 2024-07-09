---
title: "{{ cookiecutter.title }}"
tags:
- python
status: work-in-progress
---

# {{ cookiecutter.title }}

## TLDR

`Enum` supports **aliases**.
=>
We can define multiple `Enum` members with the same value.

## Explanation

## Example

Let's define an `Enum` where multiple names refer to the color blue:

```python
from enum import Enum


class Color(Enum):
    BLUE = 1
    AZUL = 1
    RED = 2
    GREEN = 3
```

Usage:

```python
print(Color.BLUE)
```

=>

```
Color.BLUE
```

```python
print(Color.AZUL)
```

=>

```
Color.BLUE
```

## Terminology

* An `Enum` has members.
* `Enum` members have `name` and `value`.

## More Info

* [Reference docs - Python Standard Library](https://docs.python.org/3/library/enum.html)
* [HOWTO docs](https://docs.python.org/3/howto/enum.html)
* [How to use strings as name aliases in Python enums](https://www.notinventedhere.org/articles/python/how-to-use-strings-as-name-aliases-in-python-enums.html)
