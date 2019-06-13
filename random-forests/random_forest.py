from random import seed
from random import random
from random import randrange

from tree import *

# Create a random subsample from the dataset with replacement
def subsample(dataset, ratio=1.0):
    sample = []
    n_sample = round(len(dataset) * ratio)
    while len(sample) < n_sample:
        index = randrange(len(dataset))
        sample.append(dataset[index])
    return sample

# Calculate the mean of a list of numbers
def mean(numbers):
	return sum(numbers) / float(len(numbers))

# Make a prediction from a list of bagged trees
def bagging_predict(trees, row):
    predictions = [predict(tree, row) for tree in trees]
    return max(set(predictions), key=predictions.count)

# Bagging Algorithm
def random_forest(train, test, max_depth, min_size, sample_size, n_trees, n_features):
    trees = []
    for i in range(n_trees):
        sample = subsample(train, sample_size)
        tree = build_tree(sample, max_depth, min_size, n_features)
        trees.append(tree)
    predictions = [bagging_predict(trees, row) for row in test]
    return predictions
