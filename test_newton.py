import numpy as np
import pytest
import math

import newton

def test_basic_function():
    assert np.isclose(newton.optimize(2.95, np.cos)['x'], math.pi)


def test_bad_input():
    with pytest.raises(TypeError, match='x0 must be numeric'):
        newton.optimize(np.cos, 2.95)

if not callable(f):
   raise TypeError(f"Argument is not a function, it is of type {type(f)}")
    
if x > 1e7:
   raise RuntimeError(f"At iteration {iter}, optimization appears to be diverging")
import warnings
if x > 3:
   warnings.warn(f"{x} is greater than 3.")