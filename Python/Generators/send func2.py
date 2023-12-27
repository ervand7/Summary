def counter_generator():
    count = 0
    while True:
        increment = yield count
        if increment is not None:
            count += increment
        else:
            count += 1


# Create the generator
counter = counter_generator()

# Start the generator
print(next(counter))  # Prints 0

# Send different values to the generator
print(counter.send(2))  # Prints 2 (0 + 2)
print(counter.send(3))  # Prints 5 (2 + 3)
print(next(counter))  # Prints 6 (5 + 1)
print(counter.send(1))  # Prints 7 (6 + 1)
