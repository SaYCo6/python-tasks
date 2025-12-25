def shortest_string(words):
    return min(words, key=len)

# Example
print(shortest_string(["code", "backend", "ai", "circle"]))
