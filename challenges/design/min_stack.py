"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.

Hide Hint #1  
Consider each node in the stack having a minimum value. (Credits to @aakarshmadhavan)
"""


class MinStack_keep_mins:
    """
    2022-07-23 16:38:52
    Runtime: 81 ms (72%)
    Memory Usage: 17.8 MB (73%)
    """

    def __init__(self):
        self.stack = []
        # you need to keep the list of mins so that you can pop all numbers
        # and still be able to return current min
        self.mins = []

    def push(self, val: int) -> None:
        # if you only keep the values less than the last min,
        # you lose the min when popping values equal to the min
        # if not self.min or (self.min and val <= self.min[-1]):
        # also, when mins array is empty, push any value into it
        if not self.mins or val <= self.mins[-1]:
            self.mins.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.mins[-1]:
            self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]
