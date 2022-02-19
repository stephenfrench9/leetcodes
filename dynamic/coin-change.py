# https://leetcode.com/problems/coin-change/
from functools import reduce
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        solns = {0: []}  # {21:[(3, 5), (2, 3)]} is 3 5s and 2 3s for 5 total coins

        for c in coins:
            def per_ele(acc, soln_total):
                remaining = amount - soln_total

                max_coins = remaining // c

                for num in range(max_coins + 1):
                    candidate_amount = soln_total + c * num

                    existing_solution = acc.get(candidate_amount)
                    existing_coin_number = sum(entry[0] for entry in existing_solution) if existing_solution is not None else -1

                    new_solution = solns.get(soln_total)+[(num, c)]
                    new_coin_number = sum(entry[0] for entry in new_solution)

                    if existing_solution is None or new_coin_number < existing_coin_number:
                        acc[candidate_amount] = new_solution

                return acc

            solns = reduce(per_ele, solns.keys(), {})

        final_soln = solns.get(amount)

        if final_soln is not None:
            return sum([entry[0] for entry in final_soln])
        else:
            return -1


        # solns.sort(key=lambda soln: sum([entry[0] for entry in soln]))
        #
        # def valid(soln):
        #     soln_total = sum([entry[0] * entry[1] for entry in soln])
        #     return soln_total == amount
        #
        # for soln in solns:
        #     if valid(soln):
        #         return sum([entry[0] for entry in soln])
        #
        # return -1
