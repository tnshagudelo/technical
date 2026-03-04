"""
Stack — LIFO data structure implemented with a Python list.
"""


class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        """Add item to the top of the stack."""
        self._items.append(item)

    def pop(self):
        """Remove and return the top item. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        """Return the top item without removing it. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("peek at empty stack")
        return self._items[-1]

    def is_empty(self):
        """Return True if the stack contains no items."""
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return f"Stack({self._items})"


# ---------------------------------------------------------------------------
# Example: check whether parentheses in a string are balanced
# ---------------------------------------------------------------------------

def is_balanced(expression: str) -> bool:
    """Return True if every opening bracket has a matching closing bracket."""
    pairs = {")": "(", "}": "{", "]": "["}
    stack = Stack()
    for char in expression:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False
    return stack.is_empty()


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s)          # Stack([1, 2, 3])
    print(s.pop())    # 3
    print(s.peek())   # 2

    print(is_balanced("({[]})"))   # True
    print(is_balanced("({[})"))    # False
