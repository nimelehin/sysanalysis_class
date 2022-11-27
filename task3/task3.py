import numpy as np
import csv
from io import StringIO


def task(data):
    f = StringIO(data)
    reader = csv.reader(f, delimiter=',')
    vertecies = []
    for row in reader:
        vertecies.append(row)

    N = len(vertecies)

    cnt = [list() for _ in range(5)]
    for x in vertecies:
        cnt[0].append(x[0])
        cnt[1].append(x[1])

    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if vertecies[i][0] == vertecies[j][1]:
                cnt[2].append(vertecies[j][0])
            if vertecies[i][1] == vertecies[j][0]:
                cnt[3].append(vertecies[j][1])
            if vertecies[i][0] == vertecies[j][0]:
                cnt[4].append(vertecies[j][1])
    ans = []
    for x in cnt:
        ans.append(sorted(list(set(x))))
    return ans

# if __name__ == "__main__":
#     print(task("""1,2
# 1,3
# 3,4
# 3,5"""))
