# collective_queue_ADT-
Creating a `README.md` file for your GitHub repository is essential to explain the purpose, functionality, and usage of your code. Below is a sample `README.md` file for your `collective_queue.py` implementation:

---

# Collective Queue Implementation in Python

This repository contains a Python implementation of various queue data structures, including fixed-size, dynamic, and circular queues. The implementation adheres to the **FIFO (First-In-First-Out)** principle and provides a wide range of operations for managing queues.

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Classes and Methods](#classes-and-methods)
4. [Usage](#usage)
5. [Examples](#examples)
6. [Contributing](#contributing)
7. [License](#license)

---

## Overview

This project implements several types of queues in Python, including:
- **Fixed-Size Queue**: A queue with a predefined maximum size.
- **Dynamic Queue**: A queue that can grow dynamically as elements are added.
- **Circular Queue**: A queue that uses a circular buffer to efficiently manage space.
- **Circular Dynamic Queue**: A combination of circular and dynamic queues, allowing for efficient space management and dynamic growth.

The implementation is designed to be flexible, allowing for various data types and providing methods for common queue operations such as `enqueue`, `dequeue`, `merge`, `reverse`, and more.

---

## Features

- **Multiple Queue Types**: Supports fixed-size, dynamic, and circular queues.
- **Type Safety**: Ensures that all elements in the queue are of the same type.
- **Efficient Operations**: Optimized for common queue operations like `enqueue`, `dequeue`, and `merge`.
- **Iterable**: Queues can be iterated over using Python's `for` loop.
- **Merge Operations**: Supports merging queues with or without modifying the original queue.
- **Ordering and Reversing**: Provides methods to order or reverse the queue without modifying the original.
- **Error Handling**: Includes robust error handling for edge cases like empty queues or type mismatches.

---

## Classes and Methods

### 1. **`collective_queue` (Abstract Base Class)**
   - Defines the interface for all queue implementations.
   - Methods:
     - `enqueue(data)`: Adds an element to the queue.
     - `dequeue()`: Removes and returns the first element from the queue.
     - `clear()`: Clears the queue.
     - `merge_with_change(second)`: Merges another iterable into the queue, modifying the original.
     - `merge_without_change(second)`: Merges another iterable into a copy of the queue.
     - `traverse()`: Prints the elements of the queue.
     - `__iter__()`: Makes the queue iterable.
     - `size()`: Returns the number of elements in the queue.
     - `is_empty()`: Checks if the queue is empty.
     - `first()`: Returns the first element without removing it.
     - `last()`: Returns the last element without removing it.
     - `contains(value)`: Checks if a value exists in the queue.
     - `to_list()`: Converts the queue to a list.
     - `copy()`: Returns a deep copy of the queue.
     - `reverse()`: Reverses the queue.
     - `order_with_change()`: Orders the queue (ascending or descending).
     - `order_without_change()`: Orders a copy of the queue.

### 2. **`array_fixed_queue`**
   - A fixed-size queue implementation using a dynamic list.
   - Methods:
     - `enqueue(data)`: Adds an element to the queue if there is space.
     - `dequeue()`: Removes and returns the first element.
     - `merge_with_change(second)`: Merges another iterable into the queue.
     - `merge_without_change(second)`: Merges another iterable into a copy of the queue.
     - `reverse_without_change()`: Reverses a copy of the queue.
     - `order_without_change(the_type)`: Orders a copy of the queue (ascending or descending).

### 3. **`array_dynamic_queue`**
   - A dynamic queue implementation with no size limit.
   - Methods:
     - Similar to `array_fixed_queue`, but without size constraints.

### 4. **`array_circular_fixed_queue`**
   - A circular queue implementation with a fixed size.
   - Methods:
     - `enqueue(data)`: Adds an element to the queue, wrapping around if necessary.
     - `dequeue()`: Removes and returns the first element.
     - `merge_with_change(second)`: Merges another iterable into the queue.
     - `merge_without_change(second)`: Merges another iterable into a copy of the queue.
     - `reverse_without_change()`: Reverses a copy of the queue.
     - `order_without_change(the_type)`: Orders a copy of the queue (ascending or descending).

### 5. **`arrary_circular_dynamic_queue`**
   - A circular dynamic queue implementation with no size limit.
   - Methods:
     - Similar to `array_circular_fixed_queue`, but with dynamic resizing.

---

## Usage

To use the queue implementations, simply import the desired class from the `collective_queue.py` file:

```python
from collective_queue import array_fixed_queue, array_dynamic_queue, array_circular_fixed_queue, arrary_circular_dynamic_queue

# Example: Fixed-size queue
fixed_queue = array_fixed_queue(limit=10, the_type=int)
fixed_queue.enqueue(5)
fixed_queue.enqueue(10)
print(fixed_queue.dequeue())  # Output: 5

# Example: Dynamic queue
dynamic_queue = array_dynamic_queue(the_type=int)
dynamic_queue.enqueue(20)
dynamic_queue.enqueue(30)
print(dynamic_queue.dequeue())  # Output: 20

# Example: Circular queue
circular_queue = array_circular_fixed_queue(limit=5)
circular_queue.enqueue(1)
circular_queue.enqueue(2)
print(circular_queue.dequeue())  # Output: 1
```

---

## Examples

### Example 1: Basic Queue Operations
```python
from collective_queue import array_fixed_queue

queue = array_fixed_queue(limit=5, the_type=int)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Output: 1
print(queue.first())    # Output: 2
print(queue.last())     # Output: 3
```

### Example 2: Merging Queues
```python
from collective_queue import array_dynamic_queue

queue1 = array_dynamic_queue(the_type=int)
queue1.enqueue(1)
queue1.enqueue(2)

queue2 = array_dynamic_queue(the_type=int)
queue2.enqueue(3)
queue2.enqueue(4)

merged_queue = queue1.merge_without_change(queue2)
print(merged_queue.queue())  # Output: [1, 2, 3, 4]
```

---

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

---

