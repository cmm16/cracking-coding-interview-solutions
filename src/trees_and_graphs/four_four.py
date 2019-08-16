class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []


def is_balanced(node, max_children):

    if len(node.children) != max_children:
        print(node.value)
        for child in node.children:
            if len(child.children) != 0:
                return False
    else:
        current = True
        for child in node.children:
            print(current)
            current = current and is_balanced(child, max_children)

    return True


if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)

    node1.children.append(node2)
    node1.children.append(node3)

    node3.children.append(node4)
    node3.children.append(node5)

    node5.children.append(node6)
    node6.children.append(node7)

    print(is_balanced(node1, 2))
