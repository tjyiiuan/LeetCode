# -*- coding: utf-8 -*-
"""
985. Sum of Even Numbers After Queries

We have an array A of integers, and an array queries of queries.

For the i-th query val = queries[i][0], index = queries[i][1], we add val to A[index].
Then, the answer to the i-th query is the sum of the even values of A.

(Here, the given index = queries[i][1] is a 0-based index, and each query permanently modifies the array A.)

Return the answer to all queries.  Your answer array should have answer[i] as the answer to the i-th query.

Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
1 <= queries.length <= 10000
-10000 <= queries[i][0] <= 10000
0 <= queries[i][1] < A.length
"""


class Solution:
    def sumEvenAfterQueries(self, arr, queries):
        sum_cache = sum(val for val in arr if val % 2 == 0)
        res = []
        for num, ind in queries:
            new_val = arr[ind] + num
            if arr[ind] % 2 == 0:
                if new_val % 2 == 0:
                    sum_cache += num
                else:
                    sum_cache -= arr[ind]
            elif new_val % 2 == 0:
                sum_cache += new_val

            arr[ind] = new_val
            res.append(sum_cache)

        return res
