from bst import BST, Node
import random


def test_insert():
    test_bst = BST()

    test_nodes = [Node(i) for i in range(1, 11)]

    test_bst.insert(test_nodes[4])

    test_nodes.remove(test_nodes[4])

    for node in test_nodes:
        test_bst.insert(node)

    test_left = test_bst.root.left

    assert test_left.right.value == 2

    test_left_right = test_left.right

    new_node = Node(1.5)
    test_bst.insert(new_node)
    assert test_left_right.left == new_node
    assert test_left_right.left.value == 1.5


def test_search():
    test_bst = BST()

    test_nodes = [Node(i) for i in range(1, 101)]
    random.shuffle(test_nodes)

    # for node in test_nodes:
    #     print(node.value)

    for node in test_nodes:
        # print(node.value)
        test_bst.insert(node)

    assert test_bst.search(45) is True
    assert test_bst.search(95) is True
    assert test_bst.search(102) is False
    assert test_bst.search(0) is False


def test_in_order_traversal():
    test_bst = BST()

    test_nodes = [Node(i) for i in range(1, 11)]
    random.shuffle(test_nodes)

    # for node in test_nodes:
    #     print(node.value)

    for node in test_nodes:
        # print(node.value)
        test_bst.insert(node)

    assert test_bst.in_order_traversal() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_find_min():
    test_bst = BST()

    test_nodes = [Node(i) for i in range(1, 11)]
    random.shuffle(test_nodes)

    # for node in test_nodes:
    #     print(node.value)

    for node in test_nodes:
        # print(node.value)
        test_bst.insert(node)

    assert test_bst.find_min() == 1

    test_bst2 = BST()

    test_nodes = [Node(i) for i in range(32, 190)]
    random.shuffle(test_nodes)

    # for node in test_nodes:
    #     print(node.value)

    for node in test_nodes:
        # print(node.value)
        test_bst2.insert(node)

    assert test_bst2.find_min() == 32


def test_find_max():
    test_bst = BST()

    test_nodes = [Node(i) for i in range(1, 11)]
    random.shuffle(test_nodes)

    # for node in test_nodes:
    #     print(node.value)

    for node in test_nodes:
        # print(node.value)
        test_bst.insert(node)

    assert test_bst.find_max() == 10

    test_bst2 = BST()

    test_nodes = [Node(i) for i in range(32, 190)]
    random.shuffle(test_nodes)

    # for node in test_nodes:
    #     print(node.value)

    for node in test_nodes:
        # print(node.value)
        test_bst2.insert(node)

    assert test_bst2.find_max() == 189


def test_height():
    test_bst = BST()

    test_nodes = [Node(i) for i in [5, 3, 1, 7, 4, 2, 6, 9, 8, 10]]

    # for node in test_nodes:
    #     print(node.value)

    for node in test_nodes:
        # print(node.value)
        test_bst.insert(node)

    assert test_bst.get_height() == 3


def test_count_leaves():
    test_bst = BST()

    test_nodes = [Node(i) for i in [5, 3, 1, 7, 4, 2, 6, 9, 8, 10]]

    # for node in test_nodes:
    #     print(node.value)

    for node in test_nodes:
        # print(node.value)
        test_bst.insert(node)

    assert test_bst.count_leaves() == 5


def test_serialize():
    test_bst = BST()

    test_nodes = [Node(i) for i in [5, 3, 1, 7, 4, 2, 6, 9, 8, 10]]

    # for node in test_nodes:
    #     print(node.value)

    for node in test_nodes:
        # print(node.value)
        test_bst.insert(node)

    assert test_bst.serialize() == "5,3,1,7,4,2,6,9,8,10"
    assert test_bst.serialize() != "5,3,1,7,4,2,6,9,8,10,11"
    assert test_bst.serialize() != ""


def test_deserialize():
    test_bst = BST()

    test_nodes = [Node(i) for i in [5, 3, 1, 7, 4, 2, 6, 9, 8, 10]]

    # for node in test_nodes:
    #     print(node.value)

    for node in test_nodes:
        # print(node.value)
        test_bst.insert(node)

    serialized = test_bst.serialize()

    new_bst = test_bst.deserialize(serialized)

    assert serialized == new_bst.serialize()


def test_delete():
    test_bst = BST()

    test_nodes = [Node(i) for i in [5, 3, 1, 7, 4, 2, 6, 9, 8, 10]]

    # for node in test_nodes:
    #     print(node.value)

    for node in test_nodes:
        # print(node.value)
        test_bst.insert(node)

    assert test_bst.delete(4).serialize() == "5,3,1,7,2,6,9,8,10"


def test_balance():
    test_bst = BST()

    test_nodes = [Node(i) for i in [5, 4, 3, 2, 1, 10, 7, 15]]

    # for node in test_nodes:
    #     print(node.value)

    for node in test_nodes:
        # print(node.value)
        test_bst.insert(node)

    test_bst.balance()

    assert test_bst.serialize() == "4,2,1,3,7,5,10,15"
