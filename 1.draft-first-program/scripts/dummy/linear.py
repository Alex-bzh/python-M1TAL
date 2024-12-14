#!/usr/bin/env python

import numpy as np

def generate_data(size=100):
  """Generate random data from a linear function with Gaussian noise."""
  noise = np.random.normal(loc=0, scale=10, size=size)
  x = np.arange(size)
  y = 2 * x - 4 + noise

  return x, y

if __name__ == '__main__':
  """Usage example.
  Works only when used as standalone.
  """
  import matplotlib.pyplot as plt

  # generate data
  X, Y = generate_data(size=100)
  
  # make plot
  coef = np.polyfit(X, Y, 1)
  poly1d_fn = np.poly1d(coef)
  plt.plot(X, Y, 'yo', X, poly1d_fn(X), '--k')

  # display plot
  plt.show()
