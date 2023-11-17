from typing import List

from Books import Books


class Node:
    def __init__(self, bookId, bookName, authorName,
                 left = None, right = None, parent = None, color = "Red"):

        self.value = Books(
            bookId= bookId,
            bookName= bookName,
            authorName= authorName)

        self.left = left
        self.right = right
        self.parent= parent
        self.color = color
