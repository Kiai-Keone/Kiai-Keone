s = "A old heart for a old year, always!"
old = "old"
new = "new"

def replace(s, old, new):
    words = s.split(old)
    return new.join(words)

result = replace(s, old, new)
print(result)
