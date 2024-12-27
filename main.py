import sys
from src.data_processing.aggregator import aggregate_numbers

def main():
    """Entry point for the application."""
    if len(sys.argv) > 1:
        numbers = [float(x) for x in sys.argv[1:]]
        result = aggregate_numbers(numbers)
        print(f"Aggregated result is: {result}")
    else:
        print("Please provide numbers as command-line arguments.")

if __name__ == "__main__":
    main()
