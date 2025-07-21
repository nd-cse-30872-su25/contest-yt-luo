#!/usr/bin/env python3
import sys

def main():
    def getways(total):
        def tuple_to_list(t):
            i, j, k = t
            return [2] * i + [3] * j + [7] * k

        a = total // 2
        b = total // 3
        c = total // 7
        res = []
        for i in range(0, a + 1):
            for j in range(0, b + 1):
                for k in range(0, c + 1):
                    if 2 * i + 3 * j + 7 * k == total:
                        res.append((i, j, k))
        res.sort(reverse=True)
        final_res = []
        for t in res:
            final_res.append(tuple_to_list(t))
        return final_res

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        total = int(line)
        ways = getways(total)
        count = len(ways)

        if count == 0:
            print(f"There are 0 ways to achieve a score of {total}:")
        elif count == 1:
            print(f"There is 1 way to achieve a score of {total}:")
        else:
            print(f"There are {count} ways to achieve a score of {total}:")

        for way in ways:
            print(' '.join(map(str, way)))

if __name__ == "__main__":
    main()
