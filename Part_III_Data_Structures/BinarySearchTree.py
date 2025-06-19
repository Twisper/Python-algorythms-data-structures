class TreeNode:
    """
    A binary search tree node
    """
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

class BinarySearchTree:
    """
    A binary search tree
    """
    def __init__(self):
        self.root = None

    def insert(self, key):
        """
        This method will insert a key into the tree

        Args:
             key: The key to insert

        Returns:
            None
        """
        y = None
        x = self.root
        node = TreeNode(key)
        while x is not None:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if not y:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

    def search(self, key):
        """
        This method will search for a key into the tree

        Args:
             key: The key to search

        Returns:
            None
        """
        current_node = self.root
        while current_node is not None and current_node.key != key:
            if key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return current_node

    def maximum(self, current_node):
        """
        This method will return the maximum value in the tree or subtree

        Args:
             current_node: The current node

        Returns:
            Node with maximum key
        """
        if current_node is None:
            return None
        while current_node.right:
            current_node = current_node.right
        return current_node

    def minimum(self, current_node):
        """
        This method will return the minimum value in the tree or subtree

        Args:
             current_node: The current node

        Returns:
            Node with minimum key
        """
        if current_node is None:
            return None
        while current_node.left:
            current_node = current_node.left
        return current_node

    def successor(self, node):
        """
        This method will return the successor of the node

        Args:
            node: The current node

        Returns:
            Node with successor key
        """
        if node is None:
            return None
        if node.right is not None:
            return self.minimum(node.right)
        y = node.parent
        while y is not None and node == y.right:
            node = y
            y = y.parent
        return y

    def predecessor(self, node):
        """
        This method will return the predecessor of the node

        Args:
             node: The current node

        Returns:
            Node with predecessor key
        """
        if node is None:
            return None
        if node.left is not None:
            return self.maximum(node.left)
        y = node.parent
        while y is not None and node == y.left:
            node = y
            y = y.parent
        return y

    def _transplant(self, node, new_node):
        """
        This method will transplant a new node, deleting old one

        Args:
            node: The current node, which will be transplanted
            new_node: The new node, which will change node

        Returns:
            None
        """
        if not node.parent:
            self.root = new_node
        elif node.parent.left == node:
            node.parent.left = new_node
        else:
            node.parent.right = new_node
        if new_node is not None:
            new_node.parent = node.parent

    def delete(self, node):
        """
        This method will delete the node

        Args:
             node: node to delete

        Returns:
            None
        """
        if node is None:
            return
        if not node.left:
            self._transplant(node, node.right)
        elif not node.right:
            self._transplant(node, node.left)
        else:
            y = self.minimum(node.right)
            if y.parent != node:
                self._transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self._transplant(node, y)
            y.left = node.left
            y.left.parent = y