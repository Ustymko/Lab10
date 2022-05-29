import math


class Coordinate:
    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y

    def get_x(self) -> float:
        return self.__x

    def get_y(self) -> float:
        return self.__y

    def __str__(self) -> str:
        return f"X: {self.__x}, Y: {self.__y}"

    def __eq__(self, other):
        return self.__x == other.get_x() and self.__y == other.get_y()


class Node:
    def __init__(self, data: Coordinate):
        self.__data = data
        self.__next = None

    def get_data(self) -> Coordinate:
        return self.__data

    def __str__(self) -> str:
        return f"X: {self.__data.get_x()}, Y: {self.__data.get_y()}"

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node


class Queue:
    def __init__(self):
        self.__head = self.__tail = None

    def add_node(self, data: Coordinate):
        temp = Node(data)
        if self.__tail is None:
            self.__head = self.__tail = temp
            return
        self.__tail.set_next(temp)
        self.__tail = temp

    def delete_node(self):
        if self.__head is None:
            return
        temp = self.__head
        self.__head = temp.get_next()
        if self.__head is None:
            self.__tail = None

    def get_length_between_head_and_tail(self) -> float:
        x_difference_squared = (self.__tail.get_data().get_x() - self.__head.get_data().get_x()) ** 2
        y_difference_squared = (self.__tail.get_data().get_y() - self.__head.get_data().get_y()) ** 2
        result_length = math.sqrt(x_difference_squared + y_difference_squared)
        return result_length

    def get_number_of_particular_node_beginning_from_front(self, data_of_particular_node: Coordinate):
        iterator = self.__head
        index = 0
        while iterator is not None:
            if iterator.get_data() == data_of_particular_node:
                return index + 1
            index += 1
            iterator = iterator.get_next()
        return "No node with these coordinates"

    def get_queue_size(self):
        iterator = self.__head
        size = 0
        while iterator is not None:
            size += 1
            iterator = iterator.get_next()
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
