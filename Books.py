from collections import deque


class Books:
    def __init__(self, bookId, bookName, authorName):
        self.bookId = bookId
        self.bookName = bookName
        self.authorName = authorName
        self.availabilityStatus = True
        self.borrowedBy = None
        self.reservationHeap = deque()

    def add_reservation(self, reservation):
        self.reservationHeap.append(reservation)
        self.reservationHeap = deque(sorted(self.reservationHeap))

    def remove_reservation(self):
        if self.reservationHeap:
            return self.reservationHeap.popleft()
        else:
            return None