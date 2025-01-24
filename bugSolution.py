def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list gracefully
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage with error handling
data = []
average = calculate_average(data)
print(f"Average: {average}")
data = [10, 20, 30]
average = calculate_average(data)
print(f"Average: {average}") 