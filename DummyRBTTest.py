from RedBlackTree import RedBlackTree

if __name__ == '__main__':
    objRBT = RedBlackTree()
    objRBT.insertionNode(bookId= 101, bookName= None, authorName= None)
    objRBT.insertionNode(bookId=48, bookName=None, authorName=None)
    objRBT.insertionNode(bookId=132, bookName=None, authorName=None)
    objRBT.insertionNode(bookId=25, bookName=None, authorName=None)
    objRBT.insertionNode(bookId=73, bookName=None, authorName=None)
    objRBT.insertionNode(bookId=12, bookName=None, authorName=None)
    objRBT.insertionNode(bookId=6, bookName=None, authorName=None)

    # resultList = objRBT.bfsTraversal()
    #
    # print("\nInsertion Result:\n")
    # for i in range(0,len(resultList)):
    #     print(resultList[i])

    # delete bookId = 12
    objRBT.delete(bookId= 12)

    # resultList = objRBT.bfsTraversal()
    #
    # print("\nDeletion Result:\n")
    # for i in range(0, len(resultList)):
    #     print(resultList[i])

    objRBT.insertionNode(bookId=125, bookName=None, authorName=None)
    objRBT.insertionNode(bookId=180, bookName=None, authorName=None)
    objRBT.insertionNode(bookId=115, bookName=None, authorName=None)
    objRBT.insertionNode(bookId=210, bookName=None, authorName=None)
    objRBT.insertionNode(bookId=80, bookName=None, authorName=None)
    objRBT.insertionNode(bookId=60, bookName=None, authorName=None)
    objRBT.insertionNode(bookId=4, bookName=None, authorName=None)
    objRBT.insertionNode(bookId=65, bookName=None, authorName=None)

    resultList = objRBT.bfsTraversal()

    print("\nInsertion Result:\n")
    for i in range(0,len(resultList)):
        print(resultList[i])


    # delete bookId 125, 115, 210, 25, 80
    objRBT.delete(bookId=125)
    objRBT.delete(bookId=115)
    objRBT.delete(bookId=210)
    objRBT.delete(bookId=25)
    objRBT.delete(bookId=80)


    resultList = objRBT.bfsTraversal()

    print("\nDeletion Result:\n")
    for i in range(0, len(resultList)):
        print(resultList[i])
