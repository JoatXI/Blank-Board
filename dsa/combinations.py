"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

"""

def combine(n, k):
        final_combos = []
        combo = []

        def backtrack(num):
            if len(combo) == k:
                print("combo made:", combo)
                final_combos.append(combo[:])
                print("returning...")
                return

            for i in range(num, n + 1):
                print("combo status:", combo)
                combo.append(i)
                print("added: ", i)
                backtrack(i + 1)
                print("backtracking: ", combo)
                combo.pop()
                print("Popped Combo: ", combo)

        backtrack(1)
        return final_combos
    
tracker = combine(4, 2)

print(tracker)