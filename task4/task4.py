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

    nodes = list(set(np.array(vertecies).reshape((-1,))))

    def nodefixup(a):
        return int(a)-1
    nodes = list(map(nodefixup, nodes))
    ans = [list() for _ in range(len(nodes))]

    for node in nodes:
        for clist in cnt:
            ans[node].append(clist.count(str(node+1)))

    npans = np.array(ans)
    nprans = npans / (len(nodes) - 1)
    s = (nprans * np.log2(nprans, where=(nprans != 0)))
    s = np.nan_to_num(s, nan=0)
    return np.sum(s) * -1


# if __name__ == "__main__":
#     print(task("""1,2
# 1,3
# 3,4
# 3,5"""))
