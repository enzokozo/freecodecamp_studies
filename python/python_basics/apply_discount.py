def apply_discount(price, discount):
    """
    This function applies a discount to a price and returns the discounted price.
    """

    # Type validation
    if not isinstance(price, (int,float)):
        return 'The price should be a number'
    
    if not isinstance(discount, (int,float)):
        return 'The discount should be a number'
    
    # Value validation
    if price <= 0:
        return 'The price should be greater than 0'
    
    if not (0 <= discount <= 100):
        return 'The discount should be between 0 and 100'
    
    # Calculate the discounted price
    return price * (1 - discount / 100)