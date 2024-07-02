from nada_dsl import *

# Mocking the Input and SecretInteger classes to simulate setting values for testing purposes
class MockInput:
    def __init__(self, name, party):
        self.name = name
        self.party = party
        self.value = None

    def set_value(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value if isinstance(other, MockInput) else self.value == other

    def __lt__(self, other):
        return self.value < other.value if isinstance(other, MockInput) else self.value < other

    def __le__(self, other):
        return self.value <= other.value if isinstance(other, MockInput) else self.value <= other

    def __gt__(self, other):
        return self.value > other.value if isinstance(other, MockInput) else self.value > other

    def __ge__(self, other):
        return self.value >= other.value if isinstance(other, MockInput) else self.value >= other

class MockSecretInteger:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return MockSecretInteger(self.value + other.value)

    def __sub__(self, other):
        return MockSecretInteger(self.value - other.value)

    def __mul__(self, other):
        return MockSecretInteger(self.value * other.value)

    def __truediv__(self, other):
        return MockSecretInteger(self.value // other.value)

    def __mod__(self, other):
        return MockSecretInteger(self.value % other.value)

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __ne__(self, other):
        return self.value != other.value

# Define a function to test nada_main with given inputs
def test_nada_main(my_int1, my_int2, operation):
    global Input, SecretInteger  # Use global to override the classes used in nada_main
    Input = MockInput  # Override the Input class with the mock class for testing
    SecretInteger = MockSecretInteger  # Override the SecretInteger class with the mock class for testing
    
    # Set inputs
    a = SecretInteger(my_int1)
    b = SecretInteger(my_int2)
    op = operation
    
    # Perform the operation based on the input
    if op == "add":
        result = a + b
    elif op == "subtract":
        result = a - b
    elif op == "multiply":
        result = a * b
    elif op == "divide":
        result = a / b if b != SecretInteger(0) else SecretInteger(0)
    elif op == "max":
        result = a if a > b else b
    elif op == "min":
        result = a if a < b else b
    elif op == "power":
        result = SecretInteger(1)
        for _ in range(b.value):
            result *= a
    elif op == "modulus":
        result = a % b if b != SecretInteger(0) else SecretInteger(0)
    else:
        result = SecretInteger(0)  # Default result if operation is not recognized

    print(f"Operation: {operation}, Result: {result.value}")

# Test cases
print("Test Case 1: Addition")
test_nada_main(12, 5, "add")

print("\nTest Case 2: Subtraction")
test_nada_main(12, 5, "subtract")

print("\nTest Case 3: Multiplication")
test_nada_main(12, 5, "multiply")

print("\nTest Case 4: Division")
test_nada_main(12, 5, "divide")

print("\nTest Case 5: Maximum")
test_nada_main(12, 5, "max")

print("\nTest Case 6: Minimum")
test_nada_main(12, 5, "min")

print("\nTest Case 7: Power")
test_nada_main(2, 3, "power")

print("\nTest Case 8: Modulus")
test_nada_main(12, 5, "modulus")
