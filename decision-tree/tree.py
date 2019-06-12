from splitting import *

################
# Build a Tree #
################

# Building a tree has 3 main parts
# 1. Terminal Nodes
# 2. Recursive Splitting
# 3. Building a Tree

# Terminal Nodes has two aspects
# 1. Maximum Tree Depth
# 2. Minimum Node Records

# Create a terminal node value
def to_terminal(group):
    outcomes = [row[-1] for row in group]
    return max(set(outcomes), key=outcomes.count)

# Recursive Splitting
def split(node, max_depth, min_size, depth):
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
        node['left'] = get_split(left)
        split(node['left'], max_depth, min_size, depth+1)

    # Process right child
    if len(right) <= min_size:
        node["right"] = to_terminal(right)
    else:
        node['right'] = get_split(right)
        split(node['right'], max_depth, min_size, depth+1)

# Build a decision tree
def build_tree(train, max_depth, min_size):
    root = get_split(train)
    split(root, max_depth, min_size, 1)
    return root

# Print a decision tree
def print_tree(node, depth=0):
	if isinstance(node, dict):
		print('%s[X%d < %.3f]' % ((depth*' ', (node['index']+1), node['value'])))
		print_tree(node['left'], depth+1)
		print_tree(node['right'], depth+1)
	else:
		print('%s[%s]' % ((depth*' ', node)))

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
