# Stack

A **stack** is a linear data structure that follows the **LIFO** (Last In, First Out) principle — the last element added is the first one removed.

## Operations

| Operation | Description | Time Complexity |
|-----------|-------------|-----------------|
| `push(x)` | Add element to the top | O(1) |
| `pop()` | Remove and return the top element | O(1) |
| `peek()` | Return the top element without removing it | O(1) |
| `is_empty()` | Check whether the stack is empty | O(1) |

## Common Use Cases

- Undo / redo functionality
- Parsing expressions (e.g., matching parentheses)
- Depth-first search (DFS) traversal
- Call stack in programming languages

## Example

See [`python/stack.py`](python/stack.py) for a clean implementation with examples.
