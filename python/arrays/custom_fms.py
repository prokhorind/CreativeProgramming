# Custom filter function
def custom_filter(func, collection):
    result = []
    for item in collection:
        if func(item):  # Apply the lambda and check the condition
            result.append(item)
    return result

# Custom map function
def custom_map(func, collection):
    result = []
    for item in collection:
        result.append(func(item))  # Apply the lambda to transform the item
    return result

# Custom reduce function
def custom_reduce(func, collection, initializer=None):
    iterator = iter(collection)
    if initializer is None:
        # Use the first element as the initial value if no initializer is provided
        accumulator = next(iterator)
    else:
        accumulator = initializer
    for item in iterator:
        accumulator = func(accumulator, item)  # Apply the lambda to accumulate
    return accumulator


# Example usage

# Custom filter: Get even numbers
nums = [1, 2, 3, 4, 5, 6]
filtered = custom_filter(lambda x: x % 2 == 0, nums)
print(f"Filtered (even numbers): {filtered}")  # Output: [2, 4, 6]

# Custom map: Square each number
squared = custom_map(lambda x: x ** 2, nums)
print(f"Mapped (squared numbers): {squared}")  # Output: [1, 4, 9, 16, 25, 36]

# Custom reduce: Sum of all numbers
summed = custom_reduce(lambda a, b: a + b, nums)
print(f"Reduced (sum): {summed}")  # Output: 21

# Custom reduce with initializer: Product of all numbers
product = custom_reduce(lambda a, b: a * b, nums, initializer=1)
print(f"Reduced (product): {product}")  # Output: 720
