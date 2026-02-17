# ==============================
# Text Animation Utility
# ==============================

# Import time module for delay
import time

# Function to simulate typing effect
def type_text(text, delay=0.02):
    
    # Loop through each character in text
    for char in text:
        
        # Print character without newline
        print(char, end="", flush=True)
        
        # Small delay between characters
        time.sleep(delay)
    
    # Print newline after complete text
    print()