import collections

from itertools import chain, combinations


def cutting_stock():
    valid_combo_1, comboList, final_combo = ([] for i in range(3))

    cuts = [1.500, 1.500, 1.500, 1.500,
            0.098, 0.098, 0.098, 0.098,
            0.600, 0.600, 0.600, 0.600,
            0.600, 0.600, 0.600, 0.600,
            0.600, 0.390, 0.390, 0.390,
            0.390, 0.390, 0.390, 0.350,
            0.350]

    stock_sizes = [0.250, 0.500, 1.000, 1.500]
    stock_prices = [3.29, 5.49, 10.69, 15.99]
    sorted_stock_sizes = sorted(stock_sizes, reverse=True)

    # Returns all possible  combinations up to range(0, x)  where 'x' is max sequence of numbers
    # Higher the number, computation time increases exponentially
    def all_subsets(ss):  # 2^len(ss) -1 number of combinations
        return chain(*map(lambda x: combinations(ss, x), range(0, 7)))

    # via LTGIV
    # Returns bool  based on if combination exists for remaining cuts
    def exactSubset(listLarge, listSubset):

        l2dLarge = {k: v for k, v in collections.Counter(listLarge).items()}
        l2dSubset = {k: v for k, v in collections.Counter(listSubset).items()}
        ret = False

        # Check values of subset
        for k2, v2 in l2dSubset.items():

            if k2 not in l2dLarge:
                ret = False
                break

            elif v2 > l2dLarge[k2]:
                ret = False
                break

            elif v2 <= l2dLarge[k2]:
                ret = True

            pass  # END

        return ret
        pass  # END FUNCTION

    # List for total combinations
    for subset in all_subsets(cuts):

        if len(subset) > 0:
            comboList.append(list(subset))

    # Valid combinations based on max cut length
    for combo in comboList:
        total = sum(combo)
        if total <= sorted_stock_sizes[0]:
            valid_combo_1.append(list(combo))

    fset = set(tuple(x) for x in valid_combo_1)
    valid_combo_1 = [list(x) for x in fset]

    sorted_combo = sorted(valid_combo_1, key=sum, reverse=True)
    cuts_2 = list(cuts)

    #  Create final combinations of cuts
    for combo in sorted_combo:

        while exactSubset(cuts_2, combo):
            for ele in combo:
                cuts_2.remove(ele)

            final_combo.append((combo))

    # Display to console
    print("------------------------------")
    print("Total Combos: {}".format(len(comboList)))
    print("Valid Combos: {}".format(len(valid_combo_1)))
    print("--- Combinations ---")
    for i, combo in enumerate(final_combo):
        print("{} - {}".format(i, combo))

    print("---")
    print("Total price at {} for {}mm: ${}".format(max(stock_prices), max(stock_sizes),
                                                   len(final_combo) * max(stock_prices)))
    print("------------------------------")

    pass


if __name__ == "__main__":
    cutting_stock()