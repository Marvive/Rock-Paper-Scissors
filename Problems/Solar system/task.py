# create the planets.txt
file = open("planets.txt", "w", encoding="utf-8")
_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
for i in _list:
    file.write(i + "\n")

file.close()
