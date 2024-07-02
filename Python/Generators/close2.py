# At the end of lifecycle (e.g. end of the program or deleting by GC
# generator closes implicitly anyway
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
print(next(gen))  # Starting
print(next(gen))  # Running
# Generator is being closed!
# Cleanup actions if any
