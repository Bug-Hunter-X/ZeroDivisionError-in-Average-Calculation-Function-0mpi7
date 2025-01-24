def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage that might cause ZeroDivisionError if not handled
data = []
average = calculate_average(data)
print(f"Average: {average}")