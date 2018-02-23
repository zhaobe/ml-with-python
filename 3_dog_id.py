import numpy as np
import matplotlib.pyplot as plt

# 1000 dog population
retrievers = 500
greyhound = 500

# avg height (in) with +/- 2 inches
h_retrievers = 22 + 2 * np.random.randn(retrievers)
h_grey = 24 + 2 * np.random.randn(greyhound)

# create histogram
plt.hist([h_retrievers, h_grey], stacked=True, color=['r','y'])
plt.show()

# height is bad feature
# eye color is bad feature

# avoid useless features
# independent features are best
# avoid redundant features
# features should be easy to understand
# simpler relationships are easier to learn

'''
---ideal---
1. informative
2. independent
3. simple
'''
