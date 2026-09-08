# ft_package

A sample test package created for Exercise 09 of the Py0 piscine
(Training Piscine Python for Data Science - 0).

## Installation

```bash
pip install ./dist/ft_package-0.0.1.tar.gz
```

or

```bash
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

## Usage

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))   # 0
```
