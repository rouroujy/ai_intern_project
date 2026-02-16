import logging

def divide(a:float,b:float) ->float:
    if b ==0:
        logging.error("Division by zero attempted")
        raise ValueError("Cannot divide by zero")
    result = a / b
    logging.info(f"{a}/{b}={result}")
    return result