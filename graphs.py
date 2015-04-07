#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import math
import numpy as np
from matplotlib import pyplot as plt

xs = np.linspace(-2, 2, 100)
ys = [math.exp(-x**2) for x in xs]

plt.plot(xs, ys)
plt.axis([-2, 2, 0, 1.1])
plt.title('Gaussian Distribution')

plt.savefig('graph.png', dpi=150)