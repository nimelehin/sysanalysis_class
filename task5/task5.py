#!/usr/bin/env python3

import argparse
import json
import numpy as np


def zap(templates):
    maxx = 0
    for i in range(len(templates)):
        if isinstance(templates[i], str):
            maxx += 1
        if isinstance(templates[i], list):
            maxx += len(templates[i])

    matrix = np.full((maxx, maxx), 0)
    for i in range(len(templates)):
        if isinstance(templates[i], str):
            for j in range(maxx):
                if j != int(templates[i])-1:
                    if matrix[(int(templates[i])-1), j] == 0:
                        matrix[(int(templates[i])-1), j] = 1
                    else:
                        matrix[(int(templates[i])-1), j] = 0
            matrix[:, (int(templates[i])-1)] = 1

        elif isinstance(templates[i], list):
            ls = []
            for _ in templates[i]:
                ls.append(int(_)-1)
            for l in ls:
                for j in range(maxx):
                    if j not in ls:
                        if matrix[l, j] == 0:
                            matrix[l, j] = 1
                        else:
                            matrix[int(l), j] = 0
                matrix[:, l] = 1

    return matrix


def task(templates, templates_2):
    templates = json.loads(templates)
    templates_2 = json.loads(templates_2)
    a = (zap(templates))
    b = (zap(templates_2))
    at = a.T
    bt = b.T

    c = np.multiply(a, b)
    d = np.multiply(at, bt)

    e = c | d

    l = [[str(j+1), str(k+1)] for j in range(len(e))
         for k in range(j, len(e[j])) if e[j][k] == 0]
    return json.dumps(l)

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(prog='Task5')
#     parser.add_argument('filename1')
#     parser.add_argument('filename2')
#     args = parser.parse_args()

#     with open(args.filename1) as f:
#         file_content = f.read()
#         templates = json.loads(file_content)
#     with open(args.filename2) as f:
#         file_content = f.read()
#         templates_2 = json.loads(file_content)

#     with open('result.json', 'w') as res:
#         res.write(task(templates, templates_2))
