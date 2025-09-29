def safe_divide(numerator, denominator):
    """Perform division with robust error handling.
    
    Args:
        numerator: The numerator value (can be string or number).
        denominator: The denominator value (can be string or number).
        
    Returns:
        str: A message indicating the result or error.
    """
    try:
        # Attempt to convert inputs to float
        num = float(numerator)
        denom = float(denominator)
        
        # Attempt to perform division
        result = num / denom
        return f"The result of the division is {result}"
        
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."