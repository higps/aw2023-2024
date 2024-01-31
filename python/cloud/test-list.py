def sum_of_lists(list_of_lists):
    """
    Calculate the sum of each list in the given list of lists.

    Parameters:
    - list_of_lists (list of list): List containing multiple lists of numerical values.

    Returns:
    - list: A list containing the sum of each individual list.
    """
    return [sum(lst) for lst in list_of_lists]

# Example usage:
lists = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = sum_of_lists(lists)
print(result)