# Random Number Generation Scripts

This repository contains two Python scripts that demonstrate how to generate random numbers using different random number generation methods: Python's built-in `random` module and `numpy`'s `random` module. Each script performs the same tasks but with different libraries for random number generation, offering an alternative approach to generating pseudo-random numbers in Python. These scripts were created with assistance from ChatGPT.

## Scripts Overview

### `rng.py`

This script uses Python's built-in `random` module to generate random numbers. It demonstrates:

- Generating five random numbers between 0 and 99.
- Generating five random numbers with a fixed seed (`3323`) between 0 and 99.
- Generating seven random numbers with a fixed seed (`80`) between 0 and 255.
- Generating ten random numbers with a fixed seed (`443`) between 0 and 255.

**Key features**:
- Uses `random.randint(a, b)` to generate random integers between `a` and `b`.
- Uses `random.seed(seed)` to set a seed for reproducibility.

```python
import random
```

### 'rng_numpy.py'

This script uses numpy's random module to generate random numbers. It performs the same tasks as rng.py, but utilizes numpy's random number generation functions, which are generally faster and more suited for scientific and mathematical applications.

- Generating five random numbers between 0 and 99.
- Generating five random numbers with a fixed seed (3323) between 0 and 99.
- Generating seven random numbers with a fixed seed (80) between 0 and 255.
- Generating ten random numbers with a fixed seed (443) between 0 and 255.

**Key features**:

- Uses np.random.randint(a, b, size) to generate random integers between a and b of specified size.
- Uses np.random.seed(seed) to set a seed for reproducibility.

```python
import numpy as np
```

##How to Run

###Prerequisites

Make sure you have Python installed on your system. If you plan to use the numpy script, ensure that numpy is installed. You can install it using pip:

```python
pip install numpy
```

###Running the Scripts

To run the 'rng.py' script, execute the following command:

```python
python rng.py
```

To run the 'rng_numpy.py' script, execute the following command:

```python
python rng_numpy.py
```
