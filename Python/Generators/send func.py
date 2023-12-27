def simple_generator():
    x = yield "Started"  # Generator pauses here and returns 'Started'
    yield f"Received: {x}"  # On next call, it yields this value


# Create the generator instance
gen = simple_generator()

# Start the generator
print(next(gen))  # This will print "Started"

# Send a value to the generator
print(gen.send(10))  # This will print "Received: 10"
