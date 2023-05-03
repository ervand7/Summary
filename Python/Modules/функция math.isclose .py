# Import math Library
import math

# compare the closeness of two values
print(math.isclose(8.005, 8.450, abs_tol=0.4))  # False
print(math.isclose(8.005, 8.450, abs_tol=0.5))  # True
