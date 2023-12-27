def example_generator():
    try:
        yield "Started"
        yield "Continuing"
    except Exception as e:
        yield f"Caught an exception: {e}"
    yield "Ended"


# Create the generator instance
gen = example_generator()

# Iterate through the generator
print(next(gen))  # Prints 'Started'
print(next(gen))  # Prints 'Continuing'

# Throw an exception into the generator
print(gen.throw(Exception, "This is an error"))  # Prints 'Caught an exception: This is an error'

# Continue iteration
print(next(gen))  # Prints 'Ended'
