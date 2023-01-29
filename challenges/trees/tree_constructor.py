def tree_constructor(strArr):
    """
    2023-01-23 07:35:25
    Checks for following:
    - All children should be unique
    - All parents should have max one left/right child
    - All nodes are connected and have 1 root node.

    Examples
    Input: ["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]
    Output: true

          4    
         /
        2
      /  \
    1     7
         /
        5
         \
          9

    Input: ["(1,2)", "(3,2)", "(2,12)", "(5,2)"]
          12
         /
        2
      /  \   x
    1      3   5
    Output: false
        - because node 2 has more than 2 children

    - check if every node has one or no left child smaller than node value
    AND one or no right child right child greater than node value

    {
        [node_value]: {
            left: None | left child node value
            right: None | right child node value
        }
    }

    - no same node can have different children
    """
    children_set = set()
    parents = {}
    for s in strArr:
        child, parent = eval(s)
        if child not in children_set:
            children_set.add(child)
        else:
            return "false"

        if parent not in parents:
            parents[parent] = [None, None]

        if child < parent and parents[parent][0] is None:
            parents[parent][0] = child
        elif child > parent and parents[parent][1] is None:
            parents[parent][1] = child
        # either child == parent or parent already has left/right child
        else:
            return "false"
    # If all nodes are connected, there should only be one root node
    # where all parent in parents dict should be found in children_set
    # except for one that is the root node.
    parents = set(parents.keys())
    root_node_set = parents - children_set

    return "true" if len(root_node_set) == 1 else "false"


def tree_constructor_2(strArr):
    """
    2023-01-28 21:48:20
    """
    parents_dict = {}
    child_set = set()
    for c, p in map(eval, strArr):
        if c in child_set:
            return "false"
        child_set.add(c)

        if p not in parents_dict:
            parents_dict[p] = [None, None]
        if c < p and parents_dict[p][0] is None:
            parents_dict[p][0] = c
        elif c > p and parents_dict[p][1] is None:
            parents_dict[p][1] = c
        else:
            return "false"
    return (
        "true" if len([p for p in parents_dict if p not in child_set]) == 1 else "false"
    )
