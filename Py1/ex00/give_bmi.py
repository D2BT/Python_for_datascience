import numpy as np


def give_bmi(
    height: list[int | float],
    weight: list[int | float],
) -> list[int | float]:
    """Compute the BMI (weight / height**2) for each height/weight pair."""
    try:
        if not isinstance(height, list) or not isinstance(weight, list):
            raise TypeError("height and weight must be lists")
        if len(height) != len(weight):
            raise ValueError("height and weight must have the same size")
        for h, w in zip(height, weight):
            if not isinstance(h, (int, float)) or isinstance(h, bool):
                raise TypeError("height must contain only int or float")
            if not isinstance(w, (int, float)) or isinstance(w, bool):
                raise TypeError("weight must contain only int or float")
        height_arr = np.array(height)
        weight_arr = np.array(weight)
        bmi = weight_arr / (height_arr ** 2)
        return bmi.tolist()
    except (TypeError, ValueError) as e:
        print(f"give_bmi: error: {e}")
        return None


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return, for each value, True if it is strictly above limit."""
    try:
        if not isinstance(bmi, list):
            raise TypeError("bmi must be a list")
        if not isinstance(limit, (int)):
            raise TypeError("limit must be an int")
        for b in bmi:
            if not isinstance(b, (int, float)) or isinstance(b, bool):
                raise TypeError("bmi must contain only int or float")
        return [b > limit for b in bmi]
    except (TypeError, ValueError) as e:
        print(f"apply_limit: error: {e}")
        return None


def main():
    """Test give_bmi and apply_limit, including the error cases."""
    height = [2.71, 1.15]
    weight = [165.3, 38.4]

    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))

    # error cases give_bmi is expected to handle without crashing
    print(give_bmi([1.8, 1.7], [70]))        # different sizes
    print(give_bmi([1.8, "x"], [70, 65]))     # wrong element type

    # error cases apply_limit is expected to handle without crashing
    print(apply_limit(bmi, "26"))            # limit is not an int
    print(apply_limit([1, "x"], 26))         # invalid element in bmi
    print(apply_limit("not a list", 26))     # bmi is not a list


if __name__ == "__main__":
    main()
