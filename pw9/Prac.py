import math,matplotlib.pyplot as po
po.plot([i / 50 for i in range(-250, 251)],[2 * v + math.sin(v) ** 2 + 3 for v in [i / 50 for i in range(-250, 251)]])
po.title("hello,po!")
po.xlabel("x")
po.ylabel("y")
po.grid(True)
po.savefig("po.pdf")