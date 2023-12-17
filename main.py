import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 5*x**3 - 7*x + 9

# Derivative function
def derivative(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2*h)

def second_derivative(f, x, h=1e-5):
    return (f(x + h) - 2*f(x) + f(x - h)) / (h**2)

x_range = np.linspace(-5, 5, 400)
y_values = f(x_range)
y_derivatives = derivative(f, x_range)
y_second_derivatives = second_derivative(f, x_range)

x_test = 3
y_test = f(x_test)
y_test_derivative = derivative(f, x_test)

plt.figure(figsize=(18, 6))

# Plot original function
plt.subplot(1, 3, 1)
plt.plot(x_range, y_values, label='f(x)')
plt.scatter(x_test, y_test, color='red')  # highlights the test point
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of 5x^3 - 7x + 9')
plt.grid(True)
plt.legend()

# Plot first derivative
plt.subplot(1, 3, 2)
plt.plot(x_range, y_derivatives, label="f'(x)", color='green')
plt.scatter(x_test, y_test_derivative, color='red')  # highlights the test point
plt.xlabel('x')
plt.ylabel("f'(x)")
plt.title(f"Derivative of 5x^3 - 7x + 9\nDerivative at x = {x_test}: {y_test_derivative:.2f}")
plt.grid(True)
plt.legend()

# Plot second derivative
plt.subplot(1, 3, 3)
plt.plot(x_range, y_second_derivatives, label="f''(x)", color='blue')
plt.xlabel('x')
plt.ylabel("f''(x)")
plt.title("Second Derivative of 5x^3 - 7x + 9")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

print(f"Value of f({x_test}):", y_test)
print(f"First Derivative of f at {x_test}:", y_test_derivative)
print(f"Second Derivative of f at {x_test}:", second_derivative(f, x_test))





#################################

a, b, c = 2.0, -3.0, 10.0
d = a * b + c

print(f"Result of a * b + c: {d}")

# For slope calculation
h = 0.0001
c += h
c += h
d2 = a*b + c



print(f"Result with adjusted c: {d2}")
print(f"Slope: {(d2 - d) / h}")


######################################

class Value:
    def __init__(self, data, _children=(), _op=''):
        self.data = data
        self._prev = set(_children)
        self._op = _op

    def __repr__(self):
        return f"Value(data={self.data}, operation={self._op})"

    def __add__(self, other):
        return Value(self.data + other.data, (self, other), "+")

    def __mul__(self, other):
        return Value(self.data * other.data, (self, other), "*")

    # Method to trace back the operation history  in class Value
    def history(self):
        result = [str(self)]
        for prev in self._prev:
            result.extend(prev.history())
        return result

# Operations
f = Value(2.0)
g = Value(-3.0)
j = Value(10.0)

res = f * g + j

print("Result:", res)
print("\nOperation History:")
for item in res.history():
    print(item)
