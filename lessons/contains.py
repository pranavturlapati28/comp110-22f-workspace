"""Example implementing a a list utility function"""

def contains(needle: str, haystack: list[str]) -> bool:
    count: int = 0
    while count < len(haystack):
        if needle == haystack[count]:
            return True
        count += 1
    return False
