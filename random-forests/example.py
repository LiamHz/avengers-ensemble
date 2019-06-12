from random import seed
from random import random
from random import randrange

from bagging import subsample, mean

seed(1)
dataset = [[randrange(10)] for i in range(20)]
print('True Mean: %.3f' % mean([row[0] for row in dataset]))
# Estimated mean
ratio = 0.10
for size in [1, 10, 100]:
    sample_means = []
    for i in range(size):
        sample  = subsample(dataset, ratio)
        sample_mean = mean([row[0] for row in sample])
        sample_means.append(sample_mean)
    print('Samples=%d, Estimated Mean: %.3f' % (size, mean(sample_means)))
