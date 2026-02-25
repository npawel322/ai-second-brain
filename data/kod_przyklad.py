def calculate_growth(initial_value, rate, years):
    """
    Oblicza wzrost inwestycji w czasie.
    rate: stopa procentowa (np. 0.05 dla 5%)
    """
    return initial_value * (1 + rate) ** years

# Ważne: Ta funkcja wykorzystuje potęgowanie do obliczeń procentu składanego.