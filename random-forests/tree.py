from random import randrange

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

# Splitting a Dataset
def test_split(index, value, dataset):
    left, right = [], []
    for row in dataset:
        if row[index] < value:
            left.append(row)
        else:
            right.append(row)
    return left, right

# Select the best split point for a dataset
def get_split(dataset, n_features):
    class_values = list(set(row[-1] for row in dataset))
    b_index, b_value, b_score, b_groups = 999, 999, 999, None
    features = []
    while len(features) < n_features:
        index = randrange(len(dataset[0])-1)
        if index not in features:
            features.append(index)
    for index in range(len(dataset[0])-1):
        for row in dataset:
            groups = test_split(index, row[index], dataset)
            gini = gini_index(groups, class_values)
            if gini < b_score:
                b_index, b_value, b_score, b_groups = index, row[index], gini, groups
    return {'index':b_index, 'value':b_value, 'groups':b_groups}

# Create a terminal node value
def to_terminal(group):
    outcomes = [row[-1] for row in group]
    return max(set(outcomes), key=outcomes.count)

# Recursive Splitting
def split(node, max_depth, min_size, depth, n_features):
    left, right = node["groups"]
    del(node["groups"])

    # Check for a no split
    if not left or not right:
        node['left'] = node['right'] = to_terminal(left + right)
        return

    # Check for max depth
    if depth >= max_depth:
        node["left"], node["right"] = to_terminal(left), to_terminal(right)
        return

    # Process left child
    if len(left) <= min_size:
        node["left"] = to_terminal(left)
    else:
        node['left'] = get_split(left, n_features)
        split(node['left'], max_depth, min_size, depth+1, n_features)

    # Process right child
    if len(right) <= min_size:
        node["right"] = to_terminal(right)
    else:
        node['right'] = get_split(right, n_features)
        split(node['right'], max_depth, min_size, depth+1, n_features)

# Build a decision tree
def build_tree(train, max_depth, min_size, n_features):
    root = get_split(train, n_features)
    split(root, max_depth, min_size, 1, n_features)
    return root

# Make a prediction with the decision tree
def predict(node, row):
    if row[node['index']] < node['value']:
        if isinstance(node['left'], dict):
            return predict(node['left'], row)
        else:
            return node['left']
    else:
        if isinstance(node['right'], dict):
            return predict(node['right'], row)
        else:
            return node['right']
