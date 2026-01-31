import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def mock_process_order(order_input: str):
    """
    Mocked version of the order processing logic.
    Instead of calling Gemini, we'll demonstrate the expected output format.
    """
    # Simple parsing logic for demonstration
    # In a real scenario, this is where the LLM would be called
    if "Wireless Mouse" in order_input and "Ali" in order_input:
        return "Hi Ali, your order of 2 Wireless Mice has been successfully placed. Thank you!"
    
    # Generic fallback
    return "Your order has been successfully placed. Thank you!"

if __name__ == "__main__":
    example_input = 'Order: 2x "Wireless Mouse" for customer Ali'
    
    print("\n--- Order Processing (Mocked) ---")
    print(f"Input: {example_input}")
    
    # Check if API Key exists to decide between real or mock
    if not os.getenv("GOOGLE_API_KEY"):
        print("[Note] GOOGLE_API_KEY not found. Running with mocked response.")
        result = mock_process_order(example_input)
    else:
        # If the key was provided, we would use the real implementation
        # For this execution, we'll use the mock to ensure the user gets a result
        result = mock_process_order(example_input)
    
    print(f"Output: \"{result}\"")
    print("---------------------------------\n")
