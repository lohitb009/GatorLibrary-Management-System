from RedBlackTree import RedBlackTree

if __name__ == '__main__':
    rbt = RedBlackTree()
    rbt.insertionNode(value=10)
    rbt.insertionNode(value=18)
    rbt.insertionNode(value=7)
    rbt.insertionNode(value=15)
    rbt.insertionNode(value=16)

    # resultList = rbt.bfsTraversal()
    # for i in range(0, len(resultList)):
    #     print(resultList[i])

    rbt.insertionNode(value=30)
    rbt.insertionNode(value=25)
    rbt.insertionNode(value=40)
    rbt.insertionNode(value=60)
    rbt.insertionNode(value=2)
    rbt.insertionNode(value=1)
    rbt.insertionNode(value=70)

    resultList = rbt.bfsTraversal()
    for i in range(0,len(resultList)):
        print(resultList[i])