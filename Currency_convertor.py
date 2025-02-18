"""This Python code implements a basic currency converter that allows users to convert amounts between different currencies using predefined exchange rates. 
The `get_exchange_rate` function retrieves the exchange rate for a specified currency pair from a hardcoded dictionary. 
The `currency_converter` function interacts with the user to input the source currency, target currency, and the amount to convert. 
It then calculates the converted amount by multiplying the input amount by the retrieved exchange rate and displays the result. 
If the currency pair is not supported, it provides an error message. 
The code effectively facilitates simple currency conversions between USD, EUR, JPY, and INR."""

def get_exchange_rate(from_currency, to_currency):
    rates = {
        ("USD", "EUR"): 0.92,
        ("USD", "JPY"): 110.50,
        ("USD", "INR"): 83.50,
        ("EUR", "USD"): 1.09,
        ("EUR", "JPY"): 120.45,
        ("EUR", "INR"): 91.65,
        ("JPY", "USD"): 0.0090,
        ("JPY", "EUR"): 0.0083,
        ("JPY", "INR"): 0.75,
        ("INR", "USD"): 0.012,
        ("INR", "EUR"): 0.011,
        ("INR", "JPY"): 1.33
    }
    return rates.get((from_currency, to_currency))

def currency_converter():
    print("Currency Converter")
    
    from_currency = input("Enter the currency to convert from (e.g., USD, EUR, JPY, INR): ").upper()
    to_currency = input("Enter the currency to convert to (e.g., USD, EUR, JPY, INR): ").upper()
    amount = float(input("Enter the amount to convert: "))
    
    exchange_rate = get_exchange_rate(from_currency, to_currency)
    
    if exchange_rate is not None:
        converted_amount = amount * exchange_rate
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    else:
        print("Invalid currency pair or rate not available.")

currency_converter()
