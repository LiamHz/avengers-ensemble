##############
# Gini Index #
##############

# The gini index is the name of the cost function used to evaluate splits in the dataset
# A gini score measures how mixed the classes are in the two groups created by the split

# Perfect seperation results in a gini score of 0
# Worst case split for 2 class problems is 0.5

# The gini index for each group is weighted by the size of the group relative to the parent

# Calculate the Gini index for a split dataset
def gini_index(groups, classes):
    # Count all samples at split point
    n_instances = float(sum([len(group) for group in groups]))
    # Sum weighted Gini index for each group
    gini = 0.0
    for group in groups:
        size = float(len(group))
        # Avoid divide by zero
        if size == 0:
            continue
        score = 0.0
        for class_val in classes:
            # Get proportion of class_val in class
            p = [row[-1] for row in group].count(class_val) / size
            score += p ** 2
        # Weight the group score by its relative size
        gini += (1.0 - score) * (size / n_instances)
    return gini

# Test Gini values
print(gini_index([[[1, 1], [1, 0]], [[1, 1], [1, 0]]], [0, 1]))
print(gini_index([[[1, 0], [1, 0]], [[1, 1], [1, 1]]], [0, 1]))
