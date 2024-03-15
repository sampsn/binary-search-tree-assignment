class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.position = None


class BST:
    def __init__(self):
        self.root = None
        self.height = None
        self.size = 0

    def insert(self, new_node: object) -> None:
        if self.root is None:
            self.root = new_node
            new_node.position = 0
            self.height = 0
            self.size += 1
            return

        current_node = self.root
        current_height = 0
        while True:
            # print(self.height)
            if new_node.value < current_node.value and current_node.left is not None:
                current_node = current_node.left
                current_height += 1
                if current_height > self.height:
                    self.height = current_height
            elif new_node.value > current_node.value and current_node.right is not None:
                current_node = current_node.right
                current_height += 1
                if current_height > self.height:
                    self.height = current_height
            elif new_node.value < current_node.value:
                new_node.position = self.size
                current_node.left = new_node
                self.size += 1
                current_height += 1
                if current_height > self.height:
                    self.height = current_height
                break
            elif new_node.value > current_node.value:
                new_node.position = self.size
                current_node.right = new_node
                self.size += 1
                current_height += 1
                if current_height > self.height:
                    self.height = current_height
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

        def _rec_in_order_traversal(node: object):
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

    def get_height(self) -> int:
        """returns the depth of the tree (how far is the furthest node from the root node?)"""
        return self.height

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
        ordered_objects = []

        def _rec_serialize(node: object) -> int:
            if node.left is not None:
                _rec_serialize(node.left)

            ordered_objects.append(node)

            if node.right is not None:
                _rec_serialize(node.right)

        _rec_serialize(self.root)

        original_order = [None] * len(ordered_objects)
        for node in ordered_objects:
            original_order[node.position] = node.value

        # serialized_str = ",".join([str(value) for value in original_order])

        serialized_str = ",".join(map(lambda x: str(x), original_order))

        return serialized_str

    def deserialize(self, tree: str) -> object:
        """deserialize a serialized BST (take a string version of a BST and
        make an empty BST filled with those values). The new tree should match
        the tree that was serialized."""

        value_list = tree.split(",")

        nodes = [Node(i) for i in value_list]

        new_bst = BST()
        for node in nodes:
            new_bst.insert(node)

        return new_bst

    # Extra Challenge
    def delete(self, value: int) -> object:
        serialized = self.serialize()
        new_values = "".join(serialized.split(str(value) + ","))

        self.root = self.deserialize(new_values).root

        return self

    # EXTRA EXTRA Challenge
    def balance(self) -> None:
        in_order_list = self.in_order_traversal()

        balanced_list = []

        def _rec_balance(values: list[int]):
            if len(values) == 2:
                balanced_list.append(values[0])
                balanced_list.append(values[1])
                return
            if len(values) == 1:
                balanced_list.append(values[0])
                return

            # print(str(values) + "top")
            if len(values) % 2 == 0:
                mid = (len(values) // 2) - 1
            else:
                mid = len(values) // 2
            mid_value = values[mid]
            balanced_list.append(mid_value)

            left_side = values[:mid]
            right_side = values[mid + 1 :]
            _rec_balance(left_side)
            _rec_balance(right_side)

        _rec_balance(in_order_list)

        serialized_str = ",".join(map(lambda x: str(x), balanced_list))

        self.root = self.deserialize(serialized_str).root
