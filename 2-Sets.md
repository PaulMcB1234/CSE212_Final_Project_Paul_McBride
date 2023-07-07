# Sets
With most types of data structures, the location of data is important. With sets, the order the data is saved and called on is largly unimportant.

## Order is Unimportant
Since the order isn't necessary for us to analyze the data in the set, this opens us up for many things, which are shown in the table below.

### Characteristics of Sets
* Faster performance for finding, removing (pop), and adding (push)
* No duplicates are allowed. This can create conflicts when two sets of data are equal or are being put into the same file location by the program, but there are ways around this.
* The order of the sets are unimportant. The function Hash doesn't look at when the value was added.

### Possible uses of Sets.
* Finding unique values in a list.
* Quick access to previous calculations.
* Finding intersections and unions between two sets.
* 
![](https://github.com/PaulMcB1234/CSE212_Final_Project_Paul_McBride/blob/main/Picture%20Set.jpg)

## Example
Lets say we're given 2 sets that have some amount of values in them that correspond to employee ID numbers for two different areas of a company. We can find what employees attend both ares by finding the tntersection of the two sets. Or we could find a total list of the employees with no duplicates by finding the union of the two sets. Examples of the intersection and union functions can be found below.
'''
set3 = intersection(set1, set2)
set3 = set1 & set2

set4 = union(set1, set2)
set4 = set1 | set2
'''

## Problem to Solve
Write a function that analyzes two sets, each with a list of ingredients for a pizza, and determine what ingredients are the same in one set, and what ingredients are different in another set. Test cases and an outline have been provided [here](https://github.com/PaulMcB1234/CSE212_Final_Project_Paul_McBride/blob/main/Pizza_Ingredients).


To go back to the home page, click [here](https://github.com/PaulMcB1234/CSE212_Final_Project_Paul_McBride/blob/main/0-Welcome.md)
