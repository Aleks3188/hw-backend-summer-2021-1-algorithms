__all__ = ("find_shortest_longest_word",)


def find_shortest_longest_word(text: str) -> tuple[str, str] | tuple[None, None]:
    words = text.split()
    
    min_word = None
    max_word = None
    
    if words:
        min_word = min(words, key=len)
        max_word = max(words, key=len)
    
    return (min_word, max_word)
