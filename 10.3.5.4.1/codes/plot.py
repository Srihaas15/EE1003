import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the compiled shared object file
lu_solver = ctypes.CDLL("./lu_solver.so")

# Create an array to hold results (x, y)
result = (ctypes.c_double * 2)()

# Call the function
lu_solver.solve(result)

# Extract the values
x, y = result[0], result[1]

print(f"Solution: x = {x}, y = {y}")

# Generate y values only for the positive range
y_vals = np.linspace(0, 100, 100)

# Compute corresponding x values
x1_vals = 1000 - 20 * y_vals
x2_vals = 1080 - 26 * y_vals

# Filter only positive x-values
valid_indices_1 = x1_vals >= 0
valid_indices_2 = x2_vals >= 0

plt.figure(figsize=(8, 6))

# Plot only for positive x-values
plt.plot(y_vals[valid_indices_1], x1_vals[valid_indices_1], label="x + 20y = 1000")
plt.plot(y_vals[valid_indices_2], x2_vals[valid_indices_2], label="x + 26y = 1080")

# Plot the solution point
if x >= 0 and y >= 0:
    plt.scatter(y, x, color="red", label=f"Solution ({x:.2f}, {y:.2f})")

# Adjust axes limits
plt.xlim(0, max(y_vals))
plt.ylim(0, max(max(x1_vals), max(x2_vals)))

# Labels and title
plt.xlabel("y")
plt.ylabel("x")
#plt.title("Solution of Linear Equations (Positive Axes Only)")
plt.legend()
plt.grid()
plt.savefig("../figs/fig.png")
plt.show()

