def nonewlines(s: str) -> str:
    return s.replace('\n', ' ').replace('\r', ' ')
    return s.replace('\n', ' ').replace('\r', ' ').replace("[", "<").replace("]", ">")
