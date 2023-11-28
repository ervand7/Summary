from time import time

COUNT = 30_000_000

a = "Hello"
b = "world"

start = time()
for i in range(COUNT):
    result = a + b
end = time()
print(end - start)  # 2.37593412399292

start = time()
for i in range(COUNT):
    result = "".join([a, b])
end = time()
print(end - start)  # 3.4162027835845947

start = time()
for i in range(COUNT):
    result = f"{a}{b}"  # 2.5340590476989746
end = time()
print(end - start)

start = time()
for i in range(COUNT):
    result = "{0}{1}".format(a, b)  # 5.159554719924927
end = time()
print(end - start)

start = time()
for i in range(COUNT):
    result = "%s%s" % (a, b)
end = time()
print(end - start)  # 3.94754695892334
