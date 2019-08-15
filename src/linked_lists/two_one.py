from src.linked_lists.link_list import Node
from collections import defaultdict


def remove_duplicates(node: Node):
    seen_map: defaultdict = defaultdict(bool)

    previous_node: Node = node
    current_node: Node = node

    while current_node.next is not None:
        if seen_map[node.value]:
            previous_node.next = current_node.next
        else:
            seen_map[node.value] = True

        previous_node = current_node
        current_node = current_node.next
