import sys
from src.data_processing.aggregator import aggregate_numbers

def compute_something(a: float, b: float) -> float:
    """
    A trivial function to demonstrate logic 
    that Keploy's LLM can test.
    """
    return (a + b) * 2

def main():
    """Entry point for the application."""
    if len(sys.argv) > 1:
        numbers = [float(x) for x in sys.argv[1:]]
        result = aggregate_numbers(numbers)
        print(f"Aggregated result is: {result}")
    else:
        print("No arguments provided—demonstrating compute_something(2, 3):")
        demo_result = compute_something(2, 3)
        print(f"compute_something(2, 3) => {demo_result}")

if __name__ == "__main__":
    main()
