#!/usr/bin/env python
# encoding: utf-8
# product.py
# product
# Created by txooo on 2018/11/19
# Copyright © 2018 txooo. All rights reserved.

"""
pip install matplotlib
"""

import pylab
import scipy

x = scipy.linspace(-2, 2, 1500)
y1 = scipy.sqrt(1 - (abs(x) - 1) ** 2)
y2 = -3 * scipy.sqrt(1 - (abs(x) / 2) ** 0.5)
pylab.fill_between(x, y1, color="red")
pylab.fill_between(x, y2, color="red")
pylab.xlim([-2.5, 2.5])
pylab.text(
    0,
    -0.4,
    "L LOVE YOU",
    fontdict={"fontsize": 30, "fontweight": "bold"},
    color="blue",
    horizontalalignment="center",
)
pylab.show()
