# <img src= "https://www.wylieisd.net/cms/lib/TX01918453/Centricity/ModuleInstance/113690/large/Groves%20Gator.jpg?rnd=0.336122636839805" width="70" height="60" />Gator Library Management System
<i> Lohit Bhambri (lohit.bhambri@ufl.edu)</i>

### How to run the project
Firstly you need to navigate to the project directory where ```Main.py``` file is
available. <br>
To test and run all the test-case associated with this project, use the following 
command:

```python
python Main.py input1.txt
python Main.py input2.txt
python Main.py input3.txt
python Main.py input4.txt
```

It will generate the following output files
```
input1_output1.txt
input2_output2.txt
input3_output3.txt
input4_output4.txt
```

### RedBlackTree.py

| Method                 | Description                                          | Time Complexity    |
|------------------------|------------------------------------------------------|---------------------|
| \_\_nodeInsertion      | Inserts a node into the Red-Black Tree.             | O(log N)            |
| \_\_colorConflictResolution | Resolves conflicts arising from red-red violation during insertion. | O(log N)            |
| insertionNode          | Inserts a new node with given book details.         | O(log N)            |
| \_\_searchNode         | Searches for a node with a given bookId.            | O(log N)            |
| \_\_getSuccessor        | Returns the in-order successor of a given node.    | O(log N)            |
| \_\_getReplacementNode  | Returns the replacement node for deletion.          | O(log N)            |
| \_\_getSibling          | Returns the sibling of a given node.                | O(1)                |
| \_\_rotateRight         | Performs a right rotation to fix coloring during deletion. | O(1)                |
| \_\_rotateLeft          | Performs a left rotation to fix coloring during deletion.  | O(1)                |
| \_\_hasRedChild         | Checks if a given node has a red child.             | O(1)                |
| \_\_fixDoubleBlack      | Fixes double black violations during deletion.    | O(log N)            |
| \_\_swapValues          | Swaps values between two nodes.                     | O(1)                |
| \_\_deleteRBTNode       | Deletes a node from the Red-Black Tree.             | O(log N)            |
| delete                 | Deletes a node with the given bookId.              | O(log N)            |

Note: The time complexities are stated in terms of the height of the Red-Black Tree (log N), where N is the number of nodes in the tree.



### Books.py

| Method                   | Description                                          | Time Complexity    |
|--------------------------|------------------------------------------------------|--------------------|
| \_\_init\_\_              | Initializes a book with given book details.         | O(1)               |
| add_reservation          | Adds a reservation to the book's reservation list and sorts it. | O(log n)          |
| remove_reservation       | Removes and returns the earliest reservation from the book. | O(log n)           |

Note: The time complexity for sorting in `add_reservation` is O(n log n), where n is the number of reservations. The removal operation in `remove_reservation` is O(log n) due to the min-heap properties.
