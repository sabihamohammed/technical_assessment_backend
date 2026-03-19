# Task: Error Handling & Resilience
# Goal: Calculate a discount safely.

def calculate_discount(price, discount_percent):
    """
    Instructions: Handle cases where discount_percent is 0 
    or if inputs are strings/None. Return 0 for invalid inputs.
    """
    try:
        if price is None or discount_percent is None:
            return 0
        
        price = float(price)
        discount_percent= float(discount_percent)

        if discount_percent == 0:
            return 0
        return price * discount_percent/100
    except(ValueError,TypeError):
        return 0
    

# Test Case
print(calculate_discount(100, "10")) # Should return 0 or handle conversion
print(calculate_discount(100, 0))    # Should return 0
