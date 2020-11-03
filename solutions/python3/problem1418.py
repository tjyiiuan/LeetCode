# -*- coding: utf-8 -*-
"""
1418. Display Table of Food Orders in a Restaurant

Given the array orders, which represents the orders that customers have done in a restaurant.
More specifically orders[i]=[customerNamei,tableNumberi,foodItemi] where customerNamei is the name of the customer,
tableNumberi is the table customer sit at, and foodItemi is the item customer orders.

Return the restaurant's “display table”. The “display table” is a table whose row entries denote how many of
each food item each table ordered. The first column is the table number and the remaining columns correspond to
each food item in alphabetical order.
The first row should be a header whose first column is “Table”, followed by the names of the food items.
Note that the customer names are not part of the table.
Additionally, the rows should be sorted in numerically increasing order.

Constraints:

1 <= orders.length <= 5 * 10^4
orders[i].length == 3
1 <= customerNamei.length, foodItemi.length <= 20
customerNamei and foodItemi consist of lowercase and uppercase English letters and the space character.
tableNumberi is a valid integer between 1 and 500.
"""


class Solution:
    def displayTable(self, orders):
        dish_cache = set()
        order_cache = {}
        for _, table, dish in orders:
            table = int(table)
            dish_cache.add(dish)

            if table not in order_cache:
                order_cache[table] = {dish: 1}
            elif dish not in order_cache[table]:
                order_cache[table][dish] = 1
            else:
                order_cache[table][dish] += 1

        dish_cache = sorted(dish_cache)
        res = [["Table"] + dish_cache]
        for table, dish_dict in sorted(order_cache.items()):
            one_table = [str(table)]
            for dish in dish_cache:
                one_table.append(str(dish_dict.get(dish, 0)))
            res.append(one_table)

        return res
