import queue


q = queue.Queue()

q.put("Hallo")
q.put("Welt")
q.put("Mars")

print(q)

print(q.get())

while not q.empty():
    e = q.get()
    print(e)


pq = queue.PriorityQueue()
pq.put((10, "Hallo Welt"))
pq.put((15, "Mars"))
pq.put((5, "Wichtig"))

print(pq.get())

