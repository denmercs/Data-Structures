from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value > value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                return self.left.insert(value)

        if self.value <= value:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                return self.right.insert(value)

    def contains(self, target):
        if target == self.value:
            return True
        elif target > self.value:
            if self.right != None:
                return self.right.contains(target)
            else:
                return False

        elif target < self.value:
            if self.left != None:
                return self.left.contains(target)
            else:
                return False

    def get_max(self):
        if self.right != None:
            return self.right.get_max()
        else:
            return self.value

    def for_each(self, cb):

        cb(self.value)
        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node == None:
            return
        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        node_queue = Queue()

        node_queue.enqueue(node)

        while node_queue.len() > 0:
            current_node = node_queue.dequeue()
            print(current_node.value)

            if current_node.left != None:
                node_queue.enqueue(current_node.left)
            if current_node.right != None:
                node_queue.enqueue(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        node_stack = Stack()

        node_stack.push(node)

        while node_stack.len() > 0:
            current_node = node_stack.pop()
            print(current_node.value)

            if current_node.left != None:
                node_stack.push(current_node.left)
            if current_node.right != None:
                node_stack.push(current_node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
