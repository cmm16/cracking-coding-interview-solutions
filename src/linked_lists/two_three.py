from src.linked_lists.link_list import Node
from copy import deepcopy


def delete_middle_node(node: Node) -> None:
    node = deepcopy(node.next)
    del node.next

