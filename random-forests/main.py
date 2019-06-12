from harness import *
from math import sqrt

# Test bagging on the sonar dataset
seed(2)

# load and prepare data
filename = '../data/sonar.all-data.csv'
dataset = load_csv(filename)

# convert string attributes to integers
for i in range(len(dataset[0])-1):
	str_column_to_float(dataset, i)

# convert class column to integers
str_column_to_int(dataset, len(dataset[0])-1)

# evaluate algorithm
n_folds = 5
max_depth = 6
min_size = 2
sample_size = 0.50
n_features = int(sqrt(len(dataset[0])-1))
for n_trees in [1, 5, 10]:
	scores = evaluate_algorithm(dataset, bagging, n_folds, max_depth, min_size, sample_size, n_trees, n_features)
	print('Trees: %d' % n_trees)
	print('Scores: %s' % scores)
	print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))
