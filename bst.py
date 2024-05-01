class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, new_value: float) -> None:
        if self.root is None:
            self.root = Node(value=new_value)
            return

        current_node = self.root
        while True:
            # print(self.height)
            if new_value < current_node.value and current_node.left is not None:
                current_node = current_node.left
            elif new_value > current_node.value and current_node.right is not None:
                current_node = current_node.right
            elif new_value < current_node.value:
                current_node.left = Node(value=new_value)
                break
            elif new_value > current_node.value:
                current_node.right = Node(value=new_value)
                break

    def search(self, value: int) -> bool:
        if self.root is None:
            return False

        current = self.root
        while current is not None:
            if current.value == value:
                return True
            elif value > current.value:
                current = current.right
            elif value < current.value:
                current = current.left

        return False

    def in_order_traversal(self) -> list[int]:
        """returns a list of all the values"""

        ordered_list = []

        def _rec_in_order_traversal(node: Node):
            if node.left is not None:
                _rec_in_order_traversal(node.left)

            ordered_list.append(node.value)

            if node.right is not None:
                _rec_in_order_traversal(node.right)

        _rec_in_order_traversal(self.root)
        return ordered_list

    def find_min(self) -> int:
        """returns the smallest number in the tree
        (you cannot turn the tree into a list then return
        an element from the list you must do it by traversing the tree)"""
        current = self.root
        while True:
            if current.left is None:
                return current.value
            else:
                current = current.left

    def find_max(self) -> int:
        """returns the largest number in the tree
        (you cannot turn the tree into a list then
        return an element from the list, you must do
        it by traversing the tree)"""
        current = self.root
        while True:
            if current.right is None:
                return current.value
            else:
                current = current.right

    def height(self) -> int:
        """returns the depth of the tree (how far is the furthest node from the root node?)"""

        def _height(root):
            if root is None:
                return -1

            left_height = _height(root.left)

            right_height = _height(root.right)

            return max(left_height, right_height) + 1

        return _height(self.root)

    def count_leaves(self) -> int:
        """returns the number of leaf nodes in the tree (leaf nodes are without any children)"""

        leaves_count = []

        def _rec_count_leaves(node: object) -> int:
            if node.left is not None:
                _rec_count_leaves(node.left)

            if node.left is None and node.right is None:
                leaves_count.append(node)

            if node.right is not None:
                _rec_count_leaves(node.right)

        _rec_count_leaves(self.root)
        return len(leaves_count)

    def serialize(self) -> str:
        """turns the BST into a string"""

        def _rec_serialize(root):
            if root is None:
                return "None,"
            return (
                str(root.value)
                + ","
                + _rec_serialize(root.left)
                + _rec_serialize(root.right)
            )

        serialized_str = _rec_serialize(self.root)

        return serialized_str

    def deserialize(self, tree: str) -> None:
        """deserialize a serialized BST (take a string version of a BST and
        make an empty BST filled with those values). The new tree should match
        the tree that was serialized."""

        def build_tree(values):
            value = next(values)
            if value == "None":
                return None
            node = Node(int(value))
            node.left = build_tree(values)
            node.right = build_tree(values)
            return node

        values = iter(tree.split(","))
        self.root = build_tree(values)
