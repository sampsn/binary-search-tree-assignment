from bst import BST, Node
import random


def test_insert():
    test_bst = BST()

    test_values = [i for i in range(1, 11)]

    test_bst.insert(test_values[4])

    test_values.remove(test_values[4])

    for value in test_values:
        test_bst.insert(value)

    test_left = test_bst.root.left

    assert test_left.right.value == 2

    test_left_right = test_left.right

    new_value = 1.5
    test_bst.insert(new_value)
    assert test_left_right.left.value == 1.5


def test_search():
    test_bst = BST()

    test_values = [i for i in range(1, 101)]
    random.shuffle(test_values)

    # for node in test_nodes:
    #     print(node.value)

    for value in test_values:
        # print(node.value)
        test_bst.insert(value)

    assert test_bst.search(45) is True
    assert test_bst.search(95) is True
    assert test_bst.search(102) is False
    assert test_bst.search(0) is False


def test_in_order_traversal():
    test_bst = BST()

    test_values = [i for i in range(1, 11)]
    random.shuffle(test_values)

    for value in test_values:
        # print(node.value)
        test_bst.insert(value)

    assert test_bst.in_order_traversal() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_find_min():
    test_bst = BST()

    test_values = [i for i in range(1, 11)]
    random.shuffle(test_values)

    # for node in test_nodes:
    #     print(node.value)

    for value in test_values:
        # print(node.value)
        test_bst.insert(value)

    assert test_bst.find_min() == 1

    test_bst2 = BST()

    test_values2 = [i for i in range(32, 190)]
    random.shuffle(test_values2)

    # for node in test_nodes:
    #     print(node.value)

    for value in test_values2:
        # print(node.value)
        test_bst2.insert(value)

    assert test_bst2.find_min() == 32


def test_find_max():
    test_bst = BST()

    test_values = [i for i in range(1, 11)]
    random.shuffle(test_values)

    # for node in test_nodes:
    #     print(node.value)

    for value in test_values:
        # print(node.value)
        test_bst.insert(value)

    assert test_bst.find_max() == 10

    test_bst2 = BST()

    test_values2 = [i for i in range(32, 190)]
    random.shuffle(test_values2)

    for value in test_values2:
        test_bst2.insert(value)

    assert test_bst2.find_max() == 189


def test_height():
    test_bst = BST()

    test_values = [i for i in [5, 3, 1, 7, 4, 2, 6, 9, 8, 10]]

    for value in test_values:
        test_bst.insert(value)

    assert test_bst.height() == 3


def test_count_leaves():
    test_bst = BST()

    test_values = [i for i in [5, 3, 1, 7, 4, 2, 6, 9, 8, 10]]

    for value in test_values:
        test_bst.insert(value)

    assert test_bst.count_leaves() == 5


def test_serialize():
    test_bst = BST()

    test_values = [i for i in [5, 3, 1, 7, 4, 2, 6, 9, 8, 10]]

    for value in test_values:
        test_bst.insert(value)

    assert (
        test_bst.serialize()
        == "5,3,1,None,2,None,None,4,None,None,7,6,None,None,9,8,None,None,10,None,None,"
    )
    assert test_bst.serialize() != ""


def test_deserialize():
    test_bst = BST()

    test_values = [i for i in [5, 3, 1, 7, 4, 2, 6, 9, 8, 10]]

    for value in test_values:
        test_bst.insert(value)

    serialized = test_bst.serialize()

    new_bst = BST()
    new_bst.deserialize(serialized)

    assert serialized == new_bst.serialize()
