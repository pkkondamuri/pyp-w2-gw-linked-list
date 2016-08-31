class Node(object):
    """
    Node class representing each of the linked nodes in the list.
    """

    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next

    def __str__(self):
        pass

    def __eq__(self, other):
        if not self or not other:
            return False
        elif self.elem == other.elem and self.next == other.next:
            return True
        return False
    def __repr__(self):
        pass
