{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "443c48a7-d154-48b3-a85b-3184c25f2827",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "x_0 = 1.0  # starting value\n",
    "epsilon = 0.01  # used for calculating derivatives\n",
    "stopping = 0.01  # stopping criteria for newton algorithm\n",
    "\n",
    "\n",
    "def func(x):\n",
    "    '''Define the prime function'''\n",
    "    return (x - 2) ** 2\n",
    "\n",
    "\n",
    "def diff(f, x, eps=epsilon):\n",
    "    '''Calculate the first derivative of a function f at point x'''\n",
    "    return (f(x + eps) - f(x)) / eps\n",
    "\n",
    "\n",
    "def diff2(f, x, eps=epsilon):\n",
    "    '''Calculate the second derivative of a function f at point x'''\n",
    "    return (diff(f, x + eps, eps) - diff(f, x, eps)) / eps\n",
    "\n",
    "\n",
    "def optimize(x0=x_0, f=func, eps=stopping):\n",
    "    '''Use Newton's method for optimization'''\n",
    "    xt = x0\n",
    "    while True:\n",
    "        d = diff(f, xt) / diff2(f, xt)\n",
    "        if abs(d) <= eps:\n",
    "            break\n",
    "        else:\n",
    "            xt = xt - d\n",
    "    print(\"Optimizing result is\", xt, \".\")\n",
    "\n",
    "optimize(x_0,func)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
