import math


class Coordinate:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"X: {self.x}, Y: {self.y}"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Node:
    def __init__(self, data: Coordinate):
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return f"X: {self.data.x}, Y: {self.data.y}"


class Queue:
    def __init__(self):
        self.head = self.tail = None

    def add_node(self, data: Coordinate):
        temp = Node(data)
        if self.tail is None:
            self.head = self.tail = temp
            return
        self.tail.next = temp
        self.tail = temp

    def delete_node(self):
        if self.head is None:
            return
        temp = self.head
        self.head = temp.next
        if self.head is None:
            self.tail = None

    def get_length_between_head_and_tail(self) -> float:
        x_difference_squared = (self.tail.data.y - self.head.data.x) ** 2
        y_difference_squared = (self.tail.data.y - self.head.data.y) ** 2
        result_length = math.sqrt(x_difference_squared + y_difference_squared)
        return result_length

    def get_number_of_particular_node_beginning_from_front(self, data_of_particular_node: Coordinate):
        iterator = self.head
        index = 0
        while iterator is not None:
            if iterator.data == data_of_particular_node:
                return index + 1
            index += 1
            iterator = iterator.next
        return "No node with these coordinates"

    def get_queue_size(self):
        iterator = self.head
        size = 0
        while iterator is not None:
            size += 1
            iterator = iterator.next
        return size


my_q = Queue()

my_q.add_node(Coordinate(1, 2))
my_q.add_node(Coordinate(2, 3))
my_q.add_node(Coordinate(3, 4))

print(my_q.get_number_of_particular_node_beginning_from_front(Coordinate(1, 2)))
print(my_q.get_length_between_head_and_tail())
print(my_q.get_queue_size())
my_q.delete_node()
print(my_q.get_queue_size())
print(my_q.get_number_of_particular_node_beginning_from_front(Coordinate(1, 2)))
print(my_q.get_length_between_head_and_tail())
