def lengthAfterTransformations(s: str, t: int) -> int:
    for _ in range(t):
        s = s.replace("z", "ab")
        s = s.replace("y", "z")
    return f"Nowy: {s}, długość: {len(s)}"





print(lengthAfterTransformations("abcyy", 2))