# my solution
class MyQueue:

    def __init__(self):
        self.data = []

    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> int:
        first = self.data[0]
        for i in range(1, len(self.data)):
            self.data[i - 1] = self.data[i]
        self.data.pop()
        return first

    def peek(self) -> int:
        return self.data[0]

    def empty(self) -> bool:
        return len(self.data) == 0


# ChatGPT solution
class MyQueue:
    def __init__(self):
        # Two stacks to implement FIFO queue
        self.in_stack = []  # Stack for incoming elements
        self.out_stack = []  # Stack for outgoing elements

    def push(self, x: int):
        # Push element into in_stack
        self.in_stack.append(x)

    def pop(self) -> int:
        self.move()
        # Pop element from out_stack
        return self.out_stack.pop()

    def peek(self) -> int:
        self.move()
        # Peek the top element from out_stack
        return self.out_stack[-1]

    def empty(self) -> bool:
        # Queue is empty if both in_stack and out_stack are empty
        return not self.in_stack and not self.out_stack

    def move(self):
        # Move elements from in_stack to out_stack if out_stack is empty
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
