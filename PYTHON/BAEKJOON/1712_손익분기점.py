a, b, c = map(int, input().split())
limit = a // (c - b) if c - b > 0 else 0
print(limit+1 if limit > 0 else -1)
print(100 // -0)