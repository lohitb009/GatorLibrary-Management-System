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

            if parent.value > node.value:
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

    def insertionNode(self, value):
        # create an object of class Node
        objNewNode = Node(value=value)

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

            for i in range(0,size):

                # pop the node from the queue
                popNode = bfsQueue.popleft()

                # check for parent
                parentValue = None

                # generate a tuple-pair
                if popNode.parent is not None:
                    parentValue = popNode.parent.value

                pair = (popNode.value, popNode.color, parentValue)

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


