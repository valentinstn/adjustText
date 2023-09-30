from unittest import TestCase

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from adjustText import adjust_text


class AdjustTextTestCase(TestCase):

    def check_coord(self, 
                    text, 
                    expected_x: float, 
                    expected_y: float, 
                    precision = 5):
        self.assertAlmostEqual(text._x, expected_x, precision)
        self.assertAlmostEqual(text._y, expected_y, precision)

    def test_minimal_example(self):
        np.random.seed(0)
        x, y = np.random.random((2,10))
        plt.plot(x, y, 'bo')
        texts = [plt.text(x[i], y[i], 'Text%s' %i) for i in range(len(x))]
       
        self.check_coord(texts[8], 0.963662, 0.778157)  # this crosses the right Y axis
        adjust_text(texts)
        self.check_coord(texts[3], 0.580056, 0.914986)  # don't touch top x axis
        self.check_coord(texts[6], 0.472718, 0.009591)  # don't touch bottom x axis
        self.check_coord(texts[8], 0.960194, 0.767660)  # moved to left so that it doesn't touch the right y axis
        self.check_coord(texts[9], 0.382282, 0.859402)  # don't touch left y axis