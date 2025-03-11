# Exercise 2: String Utilities


def reverse_string(s: str) -> str:
    return s[::-1]
    """
    Return the input string in reverse order.

    Args:
        s: Input string

    Returns:
        The reversed string
    """
    # TODO: Implement this function
    pass


def count_vowels(s: str) -> int:
    voyelles = "aeiouAEIOU"
    return sum(1 for char in s if char in voyelles)

    """
    Return the number of vowels (a, e, i, o, u) in the input string.
    Case-insensitive: both uppercase and lowercase vowels should be counted.

    Args:
        s: Input string

    Returns:
        The number of vowels in the string
    """
    # TODO: Implement this function
    pass


def is_palindrome(s: str) -> bool:
    s = s.lower().replace(" ", "")  
    return s == s[::-1]
    """
    Check if the input string is a palindrome.
    A palindrome reads the same backward as forward.
    Spaces and case should be ignored.

    Args:
        s: Input string

    Returns:
        True if the string is a palindrome, False otherwise
    """
    # TODO: Implement this function
    pass


def capitalize_words(s: str) -> str:
    return s.title()
    """
    Capitalize the first letter of each word in the input string.

    Args:
        s: Input string

    Returns:
        The input string with the first letter of each word capitalized
    """
    # TODO: Implement this function
    pass
