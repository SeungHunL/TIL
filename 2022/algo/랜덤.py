import random


class Cal:
    def __init__(self):
        a = 0.9
        self.result = [f"{a}^{i}" for i in range(1, 11)]

    def ran(self, num):
        ans = [(1, 0)]
        while num:
            choice = random.choice(self.result)
            ans.append((choice, "1-" + choice))
            num -= 1
        return ans


el = Cal()
ans = el.ran(10)
for a in ans:
    print(a)
