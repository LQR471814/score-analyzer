from decimal import Decimal


closeness_threshold = 1 ** -5

# * simpler rational numbers will be rated higher
# * value should be a between [0, 1]
# * returns value between [0, 1]
def score_simplicity(value: float) -> float:
    exact_value = Decimal(str(value))

    for denominator in range(1, 1000):
        if exact_value % Decimal(1 / denominator) < closeness_threshold:
            return 1 / denominator

    return -1
