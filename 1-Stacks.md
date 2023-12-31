# Stacks
Stacks are one the most basic kinds of data structures. 


## Last In, First Out
They function a lot like a stack of pancakes. We put add to the stack on the top and remove from the stack from the top. It's not reasonable to add or remove from the middle or bottom of the stack, that would disrupt the stack and isn't viable.

There are specific commands to do this. The table below shows

Functionallity                     | Code
---------------------------------- | -------------------
Add                                | stack.append(value)
Remove from the back of the stack  | stack.pop()
Find the Size                      | len(stack)

![](https://github.com/PaulMcB1234/CSE212_Final_Project_Paul_McBride/blob/main/Picture%20Stack.jpg)

Most functions the stacks utilize hae a big(O) notation of O(1) by themselves, but as many are put into place, the notation can change.

## Example
Consider the following code.
> stack = [1,2,3]
>
> stack.append(4)
>
> stack.append(5)
>
> stack.pop()
>
> print(stack)
>
> stack.pop(1)
>
> print(stack)


The first print statemnet gives us [1, 2, 3, 4]

The second print statement gives us [1, 3, 4]

Why did the "stack.pop(1)" remove the 2? It is because the 2 was in the "1" index of the stack. This means that we can remove from the middle of the stack, but part of the power of the stack is that we can have things in a designed order if we choose too.



## Problem to Solve
Write a function that will take a list of orders that have been placed for pancakes. There are only three types of pancakes available; plain, blueberry, and chocolate. Test cases and an outline have been provided [here](https://github.com/PaulMcB1234/CSE212_Final_Project_Paul_McBride/blob/main/Pancake_Orders).


To go back to the home page, click [here](https://github.com/PaulMcB1234/CSE212_Final_Project_Paul_McBride/blob/main/0-Welcome.md)
