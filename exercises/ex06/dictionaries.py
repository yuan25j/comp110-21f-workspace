"""Practice with dictionaries."""

__author__ = "730458275"

# Define your functions below


def invert(dict_one: dict[str, str]) -> dict[str, str]:
    """Inverts key and value of a dictionary."""
    new_dict: dict[str, str] = {}
    for x in dict_one:
        if dict_one[x] in new_dict:
            raise KeyError("There is a repeat of keys")
        new_dict[dict_one[x]] = x
    return new_dict


def favorite_color(dict_one: dict[str, str]) -> str:
    """Finds the most common color of a dict."""
    new_dict: dict[str, int] = {}
    max_count: int = 0
    max_color: str = ""
    for x in dict_one:
        if dict_one[x] in new_dict:
            new_dict[dict_one[x]] += 1
        else:
            new_dict[dict_one[x]] = 1
    for item in new_dict:
        if new_dict[item] > max_count:
            max_color = item
            max_count = new_dict[item]
    print(max_color)
    return max_color

    
def count(xs: list[str]) -> dict[str, int]:
    """Counts the times a value is in a list and creats a dictitonary."""
    new_dict: dict[str, int] = {}
    for x in xs:
        if x in new_dict:   
            new_dict[x] += 1
        else:
            new_dict[x] = 1
    return new_dict