import asyncio


# Turning a generator into a coroutine in Python typically involves using
# the asyncio library, which is the standard library for writing concurrent
# code using async/await syntax. Here's how you can convert a generator
# into a coroutine:

# Define an asynchronous generator
async def async_generator():
    for i in range(10):
        await asyncio.sleep(1)  # Simulate an async operation, e.g., IO
        yield i


# Consume the asynchronous generator
async def consume_async_generator():
    async for item in async_generator():
        print(item)


# Run the coroutine
asyncio.run(consume_async_generator())
