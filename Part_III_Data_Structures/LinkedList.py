class Node:
    """The class that represents a node in a linked list"""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class linkedList:
    """The class that represents a doubly linked list"""
    def __init__(self):
        self.head = None

    def insert_after(self, key, key_before):
        """
        Inserts a new node with 'key' after the node with 'key_before'

        Args:
            key: The key of a new node to insert
            key_before: The key of a node after which to insert

        Returns:
            True if insertion was successful, False otherwise
        """
        new_node = Node(key)
        current = self.head
        if not current:
            self.head = new_node
            print(f"Created head in the list with key {key}")
            return True
        else:
            while current.right and current.key != key_before:
                current = current.right
            if current.key != key_before:
                print(f"Insertion is impossible, element with key {key_before} is not found")
                return False
            if current.right:
                current.right.left = new_node
                new_node.right = current.right
            current.right = new_node
            new_node.left = current
            print(f"Inserted node with key {key} after the node with key {key_before}")
            return True

    def search(self, key):
        """
        Searches a node with a given 'key'

        Args:
            key: The key of node to search

        Returns:
            Node if found, None otherwise
        """
        current = self.head
        while current:
            if current.key == key:
                print(f"Found node with key {key}")
                return current
            current = current.right
        print(f"Node with key {key} is not found")
        return None

    def delete(self, key):
        """
        Deletes a node with a given 'key'

        Args:
            key: The key of node to delete

        Returns:
            True if deletion was successful, False otherwise
        """
        current = self.head
        if not current:
            print("Nothing to delete")
            return False
        if self.head.key == key:
            self.head = self.head.right
            if self.head:
                self.head.left = None
            print(f"Deleted head with key {key}")
            return True
        while current.key != key and current.right:
            current = current.right
        if current.key != key:
            print(f"Node with key {key} is not found")
            return False
        else:
            current.left.right = current.right
            if current.right:
                current.right.left = current.left
            print(f"Deleted node with key {key}")
            return True