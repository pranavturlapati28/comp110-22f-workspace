from itertools import count


def love(subject: str) -> str:
    """Given a subfject as a parameter, rrturns a loving string."""
    return f"I love you {subject}!"

print(love("Pranav"))


def spread_love(to: str, n: int) -> str:
    "Generates a str repearing a loving message n times."
    love_note: str = ""
    counter: int = 0
    while counter < n:
        love_note += love(to) + "\n"
        counter += 1
    return love_note