def my_generator():
    try:
        yield "Starting"
        yield "Running"
    except GeneratorExit:
        print("Generator is being closed!")
    finally:
        print("Cleanup actions if any")


# Create a generator instance
gen = my_generator()

# Iterate through the generator
print(next(gen))  # Prints 'Starting'
print(next(gen))  # Prints 'Running'

# Close the generator
gen.close()  # Prints 'Generator is being closed!' and 'Cleanup actions if any'
