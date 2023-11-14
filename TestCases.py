from collections import deque

from RedBlackTree import RedBlackTree
from reservationDetails import Reservation


class TestCases:

    def __init__(self, outputFileName):
        # Check if the file exists, if not, create it
        try:
            with open(outputFileName, "x"):
                pass  # Create the file if it doesn't exist
        except FileExistsError:
            pass  # The file already exists

        self.output_file = open(outputFileName, "a")  # Open the file in append mode

        # create an object of class RedBlackTree
        self.rbt = RedBlackTree()

        # set the timeCount
        self.timeCount = 0

    def __chkForAvailability(self, availabilityStatus):
        if availabilityStatus is True:
            return "Yes"
        else:
            return "No"

    def __chkForReservationHeap(self, reservationHeap):
        if len(reservationHeap) == 0:
            return []
        else:
            # add all the patronIds in the list and return the value
            patronIdList = []

            # iterate the reservationHeap
            for i in range(0, len(reservationHeap)):
                reservationObj = reservationHeap[i]
                patronIdList.append(reservationObj.patronId)

            return patronIdList

    def InsertBook(self, book_id, title, author, available):
        # update the timeCount
        self.timeCount += 1

        self.rbt.insertionNode(bookId=book_id, bookName=title, authorName=author)
        return

    def PrintBook(self, book_id):
        # update the timeCount
        self.timeCount += 1

        # here you need to do normal traversal in BST
        currentNode = self.rbt.root

        while currentNode is not None:

            if currentNode.value.bookId == book_id:
                # found it
                result = (f"BookID = {currentNode.value.bookId}\n"
                          f"Title = {currentNode.value.bookName}\n"
                          f"Author = {currentNode.value.authorName}\n"
                          f"Availability = {self.__chkForAvailability(currentNode.value.availabilityStatus)}\n"
                          f"BorrowedBy = {currentNode.value.borrowedBy}\n"
                          f"Reservations = {self.__chkForReservationHeap(currentNode.value.reservationHeap)}\n")
                # print(result)
                self.write_to_output(result)
                break

            elif currentNode.value.bookId > book_id:
                # traverse on lhs
                currentNode = currentNode.left

            elif currentNode.value.bookId < book_id:
                # traverse on rhs
                currentNode = currentNode.right

            continue
        return

    def PrintBooks(self, start_id, end_id):
        # update the timeCount
        self.timeCount += 1

        # add all the book_id in the set

        bookId_set = set()
        for i in range(start_id, end_id + 1):
            bookId_set.add(i)

        # perform bfsTraversal

        # initialize bfsQueue
        bfsQueue = deque()

        # add root to the queue
        bfsQueue.append(self.rbt.root)

        # initialize lvl
        lvl = 0

        while len(bfsQueue) != 0:
            # set queue size
            size = len(bfsQueue)

            for i in range(0, size):
                # pop the node from the queue
                popNode = bfsQueue.popleft()

                if popNode.value.bookId in bookId_set:
                    # remove the bookId from the set
                    bookId_set.remove(popNode.value.bookId)

                    result = (f"BookID = {popNode.value.bookId}\n"
                              f"Title = {popNode.value.bookName}\n"
                              f"Author = {popNode.value.authorName}\n"
                              f"Availability = {self.__chkForAvailability(popNode.value.availabilityStatus)}\n"
                              f"BorrowedBy = {popNode.value.borrowedBy}\n"
                              f"Reservations = {self.__chkForReservationHeap(popNode.value.reservationHeap)}\n")

                    # print(result)
                    self.write_to_output(result)

                # chk for set
                if len(bookId_set) == 0:
                    break

                # add children of popNode to the bfsQueue
                if popNode.left is not None:
                    bfsQueue.append(popNode.left)

                if popNode.right is not None:
                    bfsQueue.append(popNode.right)

            # chk for set
            if len(bookId_set) == 0:
                break
        return

    def BorrowBook(self, patron_id, book_id, patron_priority):
        # update the timeCount
        self.timeCount += 1

        # Implementation for BorrowBook function

        # find the book
        bookNode = self.rbt.root

        while bookNode.value.bookId != book_id:

            if bookNode.value.bookId > book_id:
                # traverse lhs
                bookNode = bookNode.left

            else:
                # traverse rhs
                bookNode = bookNode.right

            continue

        # chk if book is borrowed or not
        if bookNode.value.availabilityStatus is True:
            # set the status to False
            bookNode.value.availabilityStatus = False

            # set the borrowedBy to patron_id
            bookNode.value.borrowedBy = patron_id

            result = (f"Book {book_id} Borrowed by "
                      f"Patron {patron_id}\n")
            # print(result)
            self.write_to_output(result)

        else:
            # book is unavailable, add the entry to the reservation-heap
            reservationObj = Reservation(patronId=patron_id,
                                         priorityNumber=patron_priority,
                                         timeOfReservation=self.timeCount)

            # add the reservationObj inside the reservationHeap
            objBook = bookNode.value
            objBook.add_reservation(reservation=reservationObj)

            result = (f"Book {book_id} Reserved by "
                      f"Patron {patron_id}\n")
            # print(result)
            self.write_to_output(result)

        return

    def ReturnBook(self, patron_id, book_id):

        # update the timeCount
        self.timeCount += 1

        # Implementation for ReturnBook function

        # find the book
        bookNode = self.rbt.root

        while bookNode.value.bookId != book_id:

            if bookNode.value.bookId > book_id:
                # traverse lhs
                bookNode = bookNode.left

            else:
                # traverse rhs
                bookNode = bookNode.right

            continue

        objBook = bookNode.value

        if len(objBook.reservationHeap) == 0:

            # set the availabilityStatus to True if reservationHeap is empty
            objBook.availabilityStatus = True

            # no entry in reservationHeap
            objBook.borrowedBy = None

            # output file write
            result = (f"Book {book_id} Returned by"
                      f"Patron {patron_id}\n")
            # print(result)
            self.write_to_output(result)


        else:
            # set the borrowedBy to next patronId
            reservationObj = objBook.remove_reservation()

            # set the borrowedBy to reservationObj patronId
            objBook.borrowedBy = reservationObj.patronId

            # output file write
            result = (f"Book {book_id} Returned by "
                      f"Patron {patron_id}\n")
            # print(result)
            self.write_to_output(result)

            result = (f"Book {book_id} Allotted To "
                      f"Patron {reservationObj.patronId}\n")
            # print(result)
            self.write_to_output(result)

        return

    def Quit(self):
        # update the timeCount
        self.timeCount += 1

        # set the object to None i.e.
        self.rbt = None

        result = "Program Terminated!!\n"
        # print(result)
        self.write_to_output(result)

    def write_to_output(self, result):
        # Write the result to the output file
        self.output_file.write(result + "\n")