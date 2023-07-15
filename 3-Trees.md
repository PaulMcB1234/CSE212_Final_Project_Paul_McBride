# Trees


## Root to Branches
Trees are exactly as they sound, they start with what is called a root, and branch off into leafs. The "Root" refers to the first item in the tree (Level 1 in the picture below). The leaves are the ends of the tree (level 3 and 4 in the picture below). When addressing a particular node in the tree, we call the node that precedes it the "Parent" node. Which means that the node in question is called the "Child" node.

![](https://github.com/PaulMcB1234/CSE212_Final_Project_Paul_McBride/blob/main/Picture%20Tree.jpg)

The usefulness of a tree comes when we want to organize data in a certain order. Lets say the root of the tree is 10, and we want to add 12 to the tree. it would analyze if the number being added is greater than or less than the root and put it in accordingly as the right Child node of the root. If we wanted to then put in 11, it would see it's more than 10 but less than 12, so 11 would become the left Child node of 12.

This process called be called a Binary Search Tree, or BST. This can be a very fast way of access data, having a BigO Notation of O(log n).

## Example
Perhaps this example code will help:
~~~
Tree = BST() # Creates an empty tree
Tree.insert(10) # This becomes the root of the tree, since it's the first thing inserted into the tree
Tree.insert(12) # This is placed to the right of the root
Tree.insert(11) # This is placed to the left of the 12 node
Tree.insert(8) # This is placed to the right of root
print(tree) # this displays the tree in order like this: 8, 10, 11, 12
~~~


To go back to the home page, click [here](https://github.com/PaulMcB1234/CSE212_Final_Project_Paul_McBride/blob/main/0-Welcome.md)
