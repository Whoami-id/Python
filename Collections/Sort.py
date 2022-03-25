l = ["Max", "Monika", "Erik"]
l.sort()
print(l)

l.sort(reverse=True)
print(l)
l2 = sorted(l)
print(l2)


def get_length(item):
    return len(item)

l.sort(key=get_length)
print(l)

d = {"köln":"CGN", "Budapest":"BUD", "Saigon":"SGN"}
print(sorted(d, reverse=True))