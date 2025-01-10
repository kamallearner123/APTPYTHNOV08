def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result

# Example usage
numbers = [1, 2, 2, 3,3,3,3,3, 4, 4, 5]
print(list(set(numbers)))
result = remove_duplicates(numbers)
print(result)