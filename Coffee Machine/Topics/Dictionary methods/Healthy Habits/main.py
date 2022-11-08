sum_ = 0
for i in walks:
    sum_ += i["distance"]

print(sum_ // len(walks))
