# -*- coding: utf-8 -*-
"""
1656. Design an Ordered Stream

There is a stream of n (id, value) pairs arriving in an arbitrary order,
where id is an integer between 1 and n and value is a string.
No two pairs have the same id.

Design a stream that returns the values in increasing order of their IDs by returning a chunk (list) of values
after each insertion. The concatenation of all the chunks should result in a list of the sorted values.

Implement the OrderedStream class:

OrderedStream(int n) Constructs the stream to take n values.
String[] insert(int id, String value) Inserts the pair (id, value) into the stream,
then returns the largest possible chunk of currently inserted values that appear next in the order.

Constraints:

1 <= n <= 1000
1 <= id <= n
value.length == 5
value consists only of lowercase letters.
Each call to insert will have a unique id.
Exactly n calls will be made to insert.
"""


class OrderedStream:

    def __init__(self, n: int):
        self.cache = dict((i, "") for i in range(1, n + 1))
        self.cur_index = 1
        self.max_ind = n

    def insert(self, ind: int, value: str):
        self.cache[ind] = value
        res = []
        while self.cur_index <= self.max_ind:
            if self.cache[self.cur_index] == "":
                break
            else:
                res.append(self.cache[self.cur_index])
                self.cur_index += 1

        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)
