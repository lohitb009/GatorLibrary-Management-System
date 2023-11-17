from Node import Node
from collections import deque


class RedBlackTree:

    def __init__(self):
        self.root = None

    '''
    private function: balance nodeInsertion logic
    '''

    def __nodeInsertion(self, node=None):
        # compare the root value
        parent = self.root

        while True:

            if parent.value.bookId > node.value.bookId:
                # objNewNode on lhs
                if parent.left is not None:
                    parent = parent.left
                    continue
                else:
                    parent.left = node
                    node.parent = parent
                    break

            else:
                # objNewNode on rhs
                if parent.right is not None:
                    parent = parent.right
                    continue
                else:
                    parent.right = node
                    node.parent = parent
                    break
        return node

    def __colorConflictResolution(self, node=None):
        childNode = node
        parentNode = node.parent
        grandParentNode = parentNode.parent
        siblingNode = None

        if parentNode.color == "Black":
            # parent-color is black, simply break
            return

        elif parentNode.color == "Red" and childNode.color == "Red":
            # red-red conflict!!

            # get siblingNode
            if grandParentNode.left == parentNode:
                siblingNode = grandParentNode.right
            else:
                siblingNode = grandParentNode.left

            # compare siblingNode color and parent color
            if siblingNode is not None and siblingNode.color == "Red" and parentNode.color == "Red":
                # recolor both parentNode and siblingNode
                siblingNode.color = "Black"
                parentNode.color = "Black"

                # chk if to continue further
                if grandParentNode == self.root:
                    # grandParentNode is root, no need to continue further
                    return
                else:
                    # reverse the colors starting from grandParentNode till root
                    # if grandParentNode != self.root:

                    if grandParentNode.color == "Red":
                        grandParentNode.color = "Black"
                    else:
                        grandParentNode.color = "Red"
                        # check for red-red conflict again
                        self.__colorConflictResolution(node=grandParentNode)

                        # update the grandParentNode rfr
                        # grandParentNode = grandParentNode.parent

            elif siblingNode is None or siblingNode.color == "Black":
                '''
                We need to do rotations
                '''

                # get childNode direction
                childNodeDir = None
                if parentNode.left == childNode:
                    childNodeDir = "left"
                else:
                    childNodeDir = "right"

                # get parentNode direction
                parentNodeDir = None
                if grandParentNode.left == parentNode:
                    parentNodeDir = "left"
                else:
                    parentNodeDir = "right"

                # perform rotations
                self.__rotations(childNodeDir=childNodeDir, parentNodeDir=parentNodeDir,
                                 childNode=childNode, parentNode=parentNode,
                                 grandParentNode=grandParentNode)

    '''
    For rotations childNode = RIGHT and parentNode = LEFT
    '''

    def __leftRotations_right_left(self, childNode, parentNode, grandParentNode):
        '''
        1. childNode will be at parentNode position
        2. parentNode will be at the left of childNode
        '''

        # update grandParentNode.left rfr to the childNode
        grandParentNode.left = None
        grandParentNode.left = childNode

        # update parentNode.right rfr to None
        parentNode.right = None
        parentNode.parent = None
        parentNode.parent = childNode

        # update childNode.left rfr to parentNode
        childNode.parent = grandParentNode
        childNode.left = parentNode

        '''
        return newOrder
        
        grandParentNode -- grandParentNode
        parentNode -- childNode
        childNode -- parentNode
        '''

        return [grandParentNode, childNode, parentNode]

    def __rightRotations_right_left(self, childNode, parentNode, grandParentNode):

        # this will also be used in left-left rotations

        '''
        1. parentNode will be at grandParent position
        2. grandParentNode will be at parentNode.right position
        '''

        grand_grandParentNode = grandParentNode.parent

        # update grandparent.left rfr will be None
        grandParentNode.left = None

        if grand_grandParentNode is not None:
            if grand_grandParentNode.right == grandParentNode:
                grand_grandParentNode.right = parentNode
            else:
                grand_grandParentNode.left = parentNode

        grandParentNode.parent = parentNode
        grandParentNode.left = parentNode.right

        # update parentNode.right.parent
        if parentNode.right is not None:
            parentNode.right.parent = grandParentNode

        # update parentNode.right rfr
        parentNode.right = grandParentNode
        parentNode.parent = grand_grandParentNode

        # check if my parentNode is root
        if parentNode.parent is None:
            self.root = parentNode

        '''
        return newOrder

        grandParentNode -- parentNode
        parentNode -- grandParentNode i.e. parentNode.right
        childNode -- childNode i.e. parentNode.left
        '''

        return [parentNode, grandParentNode, childNode]

    '''
    For rotations childNode = LEFT and parentNode = RIGHT
    '''

    def __rightRotations_left_right(self, childNode, parentNode, grandParentNode):
        '''
        1. childNode will be at parentNode position
        2. parentNode will be at the right of childNode
        '''

        # update grandParentNode.right rfr to the childNode
        grandParentNode.right = None
        grandParentNode.right = childNode

        # update parentNode.left rfr to None
        parentNode.left = None
        parentNode.parent = None
        parentNode.parent = childNode

        # update childNode.right rfr to parentNode
        childNode.parent = grandParentNode
        childNode.right = parentNode

        '''
        return newOrder

        grandParentNode -- grandParentNode
        parentNode -- childNode
        childNode -- parentNode
        '''

        return [grandParentNode, childNode, parentNode]

    def __leftRotations_left_right(self, childNode, parentNode, grandParentNode):

        # this will also be used in right-right rotations

        '''
        1. parentNode will be at grandParent position
        2. grandParentNode will be at parentNode.left position
        '''

        grand_grandParentNode = grandParentNode.parent

        # update grandparent.right rfr will be None
        grandParentNode.right = None

        if grand_grandParentNode is not None:
            if grand_grandParentNode.right == grandParentNode:
                grand_grandParentNode.right = parentNode
            else:
                grand_grandParentNode.left = parentNode

        grandParentNode.parent = parentNode
        grandParentNode.right = parentNode.left

        # update the parentNode.left.parent to grandParent
        if parentNode.left is not None:
            parentNode.left.parent = grandParentNode

        # update parentNode.left rfr
        parentNode.left = grandParentNode
        parentNode.parent = grand_grandParentNode

        # check if my parentNode is root
        if parentNode.parent is None:
            self.root = parentNode

        '''
        return newOrder

        grandParentNode -- parentNode
        parentNode -- childNode i.e. parentNode.right
        childNode -- grandParentNode i.e. parentNode.left
        '''

        return [parentNode, childNode, grandParentNode]

    def __rotations(self, childNodeDir, parentNodeDir,
                    childNode, parentNode, grandParentNode):

        if childNodeDir == "right" and parentNodeDir == "left":
            '''
            1 . do left rotation
            '''
            result = self.__leftRotations_right_left(childNode=childNode, parentNode=parentNode,
                                                     grandParentNode=grandParentNode)

            # grandParentNode is unchanged
            grandParentNode = result[0]

            # parentNode is changed
            parentNode = result[1]

            # childNode is changed
            childNode = result[2]

            '''
            2. do right rotation
            '''
            result = self.__rightRotations_right_left(childNode=childNode, parentNode=parentNode,
                                                      grandParentNode=grandParentNode)

            # grandParentNode is unchanged
            grandParentNode = result[0]

            # parentNode is changed
            parentNode = result[1]

            # childNode is changed
            childNode = result[2]

            '''
            3. do recoloring
            '''
            grandParentNode.color = "Black"
            parentNode.color = "Red"
            childNode.color = "Red"

            # print("ok")


        elif childNodeDir == "left" and parentNodeDir == "right":
            '''
            1 . do right rotation
            '''
            result = self.__rightRotations_left_right(childNode=childNode, parentNode=parentNode,
                                                      grandParentNode=grandParentNode)

            # grandParentNode is unchanged
            grandParentNode = result[0]

            # parentNode is changed
            parentNode = result[1]

            # childNode is changed
            childNode = result[2]

            '''
            2. do left rotation
            '''
            result = self.__leftRotations_left_right(childNode=childNode, parentNode=parentNode,
                                                     grandParentNode=grandParentNode)

            # grandParentNode is unchanged
            grandParentNode = result[0]

            # parentNode is changed
            parentNode = result[1]

            # childNode is changed
            childNode = result[2]

            '''
            3. do recoloring
            '''
            grandParentNode.color = "Black"
            parentNode.color = "Red"
            childNode.color = "Red"

        elif childNodeDir == "right" and parentNodeDir == "right":

            '''
            1. do left rotation
            '''

            result = self.__leftRotations_left_right(childNode=childNode, parentNode=parentNode,
                                                     grandParentNode=grandParentNode)

            # grandParentNode is unchanged
            grandParentNode = result[0]

            # parentNode is changed
            parentNode = result[1]

            # childNode is changed
            childNode = result[2]

            '''
            3. do recoloring
            '''
            grandParentNode.color = "Black"
            parentNode.color = "Red"
            childNode.color = "Red"

        elif childNodeDir == "left" and parentNodeDir == "left":
            '''
            1. do right rotation
            '''
            result = self.__rightRotations_right_left(childNode=childNode, parentNode=parentNode,
                                                      grandParentNode=grandParentNode)

            # grandParentNode is unchanged
            grandParentNode = result[0]

            # parentNode is changed
            parentNode = result[1]

            # childNode is changed
            childNode = result[2]

            '''
            3. do recoloring
            '''
            grandParentNode.color = "Black"
            parentNode.color = "Red"
            childNode.color = "Red"

    def insertionNode(self, bookId, bookName, authorName):
        # create an object of class Node
        objNewNode = Node(bookId=bookId,
                          bookName=bookName, authorName=authorName)

        # case 1 -- tree is empty
        if self.root is None:
            objNewNode.color = "Black"  # the very first node is black
            self.root = objNewNode
            return

        # case 2 -- tree is not empty
        if self.root is not None:
            objNewNode = self.__nodeInsertion(objNewNode)

        # now check for color conflict
        self.__colorConflictResolution(objNewNode)

    # write the traversal function
    def bfsTraversal(self):

        # set the resultList
        resultList = []

        # initialize an empty queue
        bfsQueue = deque()

        # add root to the queue
        bfsQueue.append(self.root)

        # initialize lvl
        lvl = 0

        while len(bfsQueue) != 0:
            # set queue size
            size = len(bfsQueue)

            # local list
            local = []

            for i in range(0, size):

                # pop the node from the queue
                popNode = bfsQueue.popleft()

                # check for parent
                parentValue = None

                # generate a tuple-pair
                if popNode.parent is not None:
                    parentValue = popNode.parent.value.bookId

                pair = (popNode.value.bookId, popNode.color, parentValue)

                # add pair inside local
                local.append(pair)

                # add children of popNode to the bfsQueue
                if popNode.left is not None:
                    bfsQueue.append(popNode.left)

                if popNode.right is not None:
                    bfsQueue.append(popNode.right)

            '''end of for loop'''
            resultList.append(local)

            # update lvl
            lvl += 1
        '''end of while loop'''

        # update lvl
        lvl -= 1

        # return the result
        return resultList

    def __searchNode(self, bookId):
        currentNode = self.root

        while currentNode is not None:
            if currentNode.value.bookId == bookId:
                break
            elif bookId < currentNode.value.bookId:
                currentNode = currentNode.left
            elif bookId > currentNode.value.bookId:
                currentNode = currentNode.right

        return currentNode

    def __getSuccessor(self, node):
        successor = node

        while successor.left is not None:
            successor = successor.left

        return successor

    def __getReplacementNode(self, node):

        if node.left is not None and node.right is not None:
            '''
            if the node has two children, return the in-order successor of the node
            '''
            return self.__getSuccessor(node.right)

        if node.left is None and node.right is None:
            # if node is a leaf node, return None
            return None

        if node.left is not None:
            # if node.left child is not null, return left
            return node.left

        if node.left is not None:
            # if node.left child is not null, return left
            return node.left

        else:
            # if node.right is not null, return right
            return node.right

    def __getSibling(self, node):
        if node == self.root:
            return None

        if node.parent.left == node:
            return node.parent.right

        else:
            return node.parent.left

    """
    The function is used as part of fixing up the coloring
        of red-black tree, while insertion or deletion operations.

            B                                          A
           / \        ->(rotate right on B)->         / \
          A   E                                      C   B
         / \                                            / \
        C   D                                          D   E
    """

    def __rotateRight(self, node):

        leftChild = node.left
        node.left = leftChild.right

        if leftChild.right is not None:
            leftChild.right.parent = node
        leftChild.parent = node.parent

        if node.parent is None:
            self.root = leftChild
        elif node == node.parent.right:
            node.parent.right = leftChild
        else:
            node.parent.left = leftChild

        leftChild.right = node
        node.parent = leftChild

        return node

    """
    The function is used as part of fixing up the coloring
        of red-black tree, while insertion or deletion operations.

        A                                          B
       / \        ->(rotate left on A)->          / \
      C   B                                      A   E
         / \                                    / \
        D   E                                  C   D
    
    """

    def __rotateLeft(self, node):

        rightChild = node.right
        node.right = rightChild.left

        if rightChild.left is not None:
            rightChild.left.parent = node
        rightChild.parent = node.parent

        if node.parent is None:
            self.root = rightChild
        elif node == node.parent.left:
            node.parent.left = rightChild
        else:
            node.parent.right = rightChild

        rightChild.left = node
        node.parent = rightChild

        return node

    def __hasRedChild(self, node):
        return ((node.left is not None and node.left.color == "Red")
                or (node.right is not None and node.right.color == "Red"))

    def __fixDoubleBlack(self, node):
        if node == self.root:
            return

        parent = node.parent
        sibling = self.__getSibling(node)

        if sibling is not None:
            if sibling.color == "Red":

                if sibling.parent.left == sibling:
                    # If sibling is left child of its parent, rotate right on parent
                    self.__rotateRight(parent)
                else:
                    # If sibling is right child of its parent, rotate left on parent
                    self.__rotateLeft(parent)

                # fix the colors of parent and sibling
                parent.color = "Red"
                sibling.color = "Black"

                '''
                since the double black still exists on the node, call fix double black for node
                '''
                self.__fixDoubleBlack(node)

            else:
                if self.__hasRedChild(sibling):

                    # if the sibling has left red child
                    if sibling.left is not None and sibling.left.color == "Red":

                        if sibling.parent.left == sibling:
                            # if sibling is the left child of its parent (LL Case)

                            # fix the colors
                            sibling.left.color = sibling.color
                            sibling.color = parent.color
                            # rotate right
                            self.__rotateRight(parent)

                        else:
                            # if sibling is right child of its parent (RL case)

                            # fix colors
                            sibling.left.color = parent.color
                            # rotate right on sibling
                            self.__rotateRight(sibling)
                            # rotate left on parent
                            self.__rotateLeft(parent)

                    else:
                        # If the sibling has right red child

                        if sibling.parent.left == sibling:
                            # If sibling is left child of its parent (LR case)

                            # fix colors
                            sibling.right.color = parent.color
                            # rotate left on sibling
                            self.__rotateLeft(sibling)
                            # rotate right on parent
                            self.__rotateRight(parent)

                        else:
                            # If sibling is right child of its parent (RR case)

                            # fix the colors
                            sibling.right.color = sibling.color
                            sibling.color = parent.color
                            # rotate right on parent
                            self.__rotateLeft(parent)

                else:
                    # if sibling has no red child

                    # fix the color of sibling
                    sibling.color = "Red"
                    if parent.color == "Black":
                        # If parent was black and since the double black os propagated to parent now, call fix double black
                        self.__fixDoubleBlack(parent)
                    else:
                        # Since parent was red, it can cover the deficit, make it black.
                        parent.color = "Black"

        else:
            # if sibling is null, fix double black on parent
            self.__fixDoubleBlack(parent)


    def __swapValues(self, node1, node2):
        temp = node1.value
        node1.value = node2.value
        node2.value = temp

    def __deleteRBTNode(self, nodeToDelete):

        # 2. get the replacementNode
        replacementNode = self.__getReplacementNode(nodeToDelete)

        # 3. check if replacementNode and nodeToDelete are both black
        if (replacementNode is None or replacementNode.color == "Black") and (nodeToDelete.color == "Black"):
            bothBlack = True
        else:
            bothBlack = False

        if replacementNode is None:

            if nodeToDelete == self.root:
                self.root = None

            else:

                # getSibling = self.__getSibling(nodeToDelete)

                if bothBlack is True:
                    # call fixDoubleBlack case on nodeToDelete
                    self.__fixDoubleBlack(nodeToDelete)

                elif self.__getSibling(nodeToDelete) is not None:
                    # else if sibling is not null color it red
                    self.__getSibling(nodeToDelete).color = "Red"

                if nodeToDelete.parent.left == nodeToDelete:
                    # If node to delete is left child of parent, make left child of parent null
                    nodeToDelete.parent.left = None
                elif nodeToDelete.parent.right == nodeToDelete:
                    # If node to delete is right child of parent, make right child of parent null
                    nodeToDelete.parent.right = None

            return

        # If the node to delete has atmost one child
        if nodeToDelete.left is None or nodeToDelete.right is None:

            if nodeToDelete == self.root:
                # If node to delete is root
                nodeToDelete.value = replacementNode.value
                # make root's left and right child null
                nodeToDelete.left = nodeToDelete.right = None

            else:
                # if node to delete is not root
                if nodeToDelete.parent.left == nodeToDelete:
                    # if node to delete is left child of parent, make replacement node as left child
                    nodeToDelete.parent.left = replacementNode
                else:
                    # if node to delete is right child of parent, make replacement node as right child
                    nodeToDelete.parent.right = replacementNode

                # Update parent node
                replacementNode.parent = nodeToDelete.parent

                if bothBlack is True:
                    # if both of node to delete and replacement nodes were black, call the fix double black
                    self.__fixDoubleBlack(replacementNode)
                else:
                    # else make the replacement node as black
                    replacementNode.color = "Black"

            return

        # if the node to delete had both left and right child, swap rides between node to delete and replacement node
        self.__swapValues(nodeToDelete, replacementNode)
        # call delete for replacement node
        self.__deleteRBTNode(replacementNode)

    def delete(self, bookId):
        # search the node to delete
        # 1. get nodeToDelete
        nodeToDelete = self.__searchNode(bookId=bookId)

        if nodeToDelete is None:
            return "no_bookId"

        # 2. get the value of the nodeToDelete
        value = nodeToDelete.value

        # 3. perform delete
        self.__deleteRBTNode(nodeToDelete= nodeToDelete)

        # 4. return the value
        return value

