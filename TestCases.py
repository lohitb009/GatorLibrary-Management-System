import os
from collections import deque

from RedBlackTree import RedBlackTree
from reservationDetails import Reservation


class TestCases:

    def __init__(self, outputFileName):
        # Check if the file exists
        file_exists = os.path.isfile(outputFileName)

        # If the file exists, flush its contents
        if file_exists:
            with open(outputFileName, "w") as file:
                file.write("")  # Flush the contents by overwriting an empty string

        # Open the file in append mode
        self.output_file = open(outputFileName, "a")

        # create an object of class RedBlackTree
        self.rbt = RedBlackTree()

        # set the timeCount
        self.timeCount = 0

        # inorder traversal list
        self.__inorderTraversalList = []


    def __inorderTraversal(self, node):

        # base-case
        while node is None:
            return

        # logic-case

        # traverse on lhs
        self.__inorderTraversal(node.left)

        # add root
        rootValue = node.value
        self.__inorderTraversalList.append(rootValue)

        # traverse on rhs
        self.__inorderTraversal(node.right)

        return

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
                result = (f"\nBookID = {currentNode.value.bookId}\n"
                          f"Title = {currentNode.value.bookName}\n"
                          f"Author = {currentNode.value.authorName}\n"
                          f"Availability = {self.__chkForAvailability(currentNode.value.availabilityStatus)}\n"
                          f"BorrowedBy = {currentNode.value.borrowedBy}\n"
                          f"Reservations = {self.__chkForReservationHeap(currentNode.value.reservationHeap)}")
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

                    result = (f"\nBookID = {popNode.value.bookId}\n"
                              f"Title = {popNode.value.bookName}\n"
                              f"Author = {popNode.value.authorName}\n"
                              f"Availability = {self.__chkForAvailability(popNode.value.availabilityStatus)}\n"
                              f"BorrowedBy = {popNode.value.borrowedBy}\n"
                              f"Reservations = {self.__chkForReservationHeap(popNode.value.reservationHeap)}")

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

            result = (f"\nBook {book_id} Borrowed by "
                      f"Patron {patron_id}")
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

            result = (f"\nBook {book_id} Reserved by "
                      f"Patron {patron_id}")
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
            result = "\nBook "+str(book_id)+ " Retuned by Patron "+str(patron_id)
            # print(result)
            self.write_to_output(result)


        else:
            # set the borrowedBy to next patronId
            reservationObj = objBook.remove_reservation()

            # set the borrowedBy to reservationObj patronId
            objBook.borrowedBy = reservationObj.patronId

            # output file write
            result = (f"\nBook {book_id} Returned by "
                      f"Patron {patron_id}")
            # print(result)
            self.write_to_output(result)

            result = (f"\nBook {book_id} Allotted To "
                      f"Patron {reservationObj.patronId}")
            # print(result)
            self.write_to_output(result)

        return

    def Quit(self):
        # update the timeCount
        self.timeCount += 1

        # set the object to None i.e.
        self.rbt = None

        result = "\nProgram Terminated!!"
        # print(result)
        self.write_to_output(result)

    def DeleteBook(self, bookId):
        # update the timeCount
        self.timeCount += 1

        # call the delete function -- we will get only the node.value
        deleteNodeValue = self.rbt.delete(bookId=bookId)

        # base-case
        if deleteNodeValue == "no_bookId":
            return

        # set general delete message
        generalMessage = "\nBook " + str(bookId) + " is no longer available."

        # chk for reservation heap
        if len(deleteNodeValue.reservationHeap) == 0:
            self.write_to_output(generalMessage)


        else:
            patronIdStr = ""

            # iterate the minHeap
            while len(deleteNodeValue.reservationHeap) != 0:
                patronDetails = deleteNodeValue.reservationHeap.popleft()
                patron_Id = patronDetails.patronId
                patronIdStr += str(patron_Id) + ", "
            '''end of while loop'''

            patronIdStr = patronIdStr.rstrip(", ")
            additionalMessage = (generalMessage +' '+
                                 "Reservation made by patrons " + patronIdStr + " have been cancelled!")
            self.write_to_output(additionalMessage)

        return

    def FindClosestBook(self, targetId):

        # do the inorder traversal of the tree
        self.__inorderTraversalList = []
        self.__inorderTraversal(self.rbt.root)

        # find the closest pair
        minDifference = float('inf')

        # getClosestBooksList
        closestBooksList = []

        # inorder traversal of the list
        for i in range(0,len(self.__inorderTraversalList)):
            bookDetails = self.__inorderTraversalList[i]

            # Calculate absolute difference
            absolute_difference = abs(bookDetails.bookId - targetId)

            # base-case
            if i == 0:
                minDifference = absolute_difference
                closestBooksList.append(bookDetails)
                continue

            # logic-case
            if minDifference > absolute_difference:

                minDifference = absolute_difference

                if len(closestBooksList) > 1:
                    # if you have more than 1 objects in the list
                    closestBooksList = [bookDetails]
                else:
                    # just update the last element added in the list
                    closestBooksList[-1] = bookDetails

            elif minDifference == absolute_difference:
                # difference is same, append the bookDetails in the list
                closestBooksList.append(bookDetails)

        '''end of for loop'''

        # add the closest books list to the output
        for books in closestBooksList:
            result = (f"\nBookID = {books.bookId}\n"
                      f"Title = {books.bookName}\n"
                      f"Author = {books.authorName}\n"
                      f"Availability = {self.__chkForAvailability(books.availabilityStatus)}\n"
                      f"BorrowedBy = {books.borrowedBy}\n"
                      f"Reservations = {self.__chkForReservationHeap(books.reservationHeap)}")
            # print(result)
            self.write_to_output(result)
        '''end of for loop'''
        
        return

    # to implement
    def ColorFlipCount(self):
        pass

    def write_to_output(self, result):
        # Write the result to the output file
        self.output_file.write(result + "\n")
