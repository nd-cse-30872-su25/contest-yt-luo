#!/usr/bin/env python3
import sys
import itertools

# calculate left and right expression and then bruteforce
def calculateleft(ops):
    cur = 9
    l = [8, 7, 6]
    for i in range(3):
        if ops[i] == "+":
            cur += l[i]
        elif ops[i] == "-":
            cur -= l[i]
        else:
            cur *= l[i]
    return cur

def calculateright(ops):
    cur = 1
    rev_ops = ops[::-1]
    r = [2, 3, 4, 5]
    for i in range(4):
        if rev_ops[i] == "+":
            cur = r[i] + cur
        elif rev_ops[i] == "-":
            cur = r[i] - cur
        else:
            cur = r[i] * cur
    return cur

def solve(num):
    ops = ['+', '-', '*']
    for combo in itertools.product(ops, repeat=8):
        s = ''.join(combo)
        op_l = s[0:3]
        middle = s[3]
        op_r = s[4:]
        left = calculateleft(op_l)
        right = calculateright(op_r)
        valid = False
        if middle == "+" and left + right == num:
            valid = True
        elif middle == "-" and left - right == num:
            valid = True
        elif middle == "*" and left * right == num:
            valid = True

        if valid:
            expr = f"(((9 {op_l[0]} 8) {op_l[1]} 7) {op_l[2]} 6) {middle} (5 {op_r[0]} (4 {op_r[1]} (3 {op_r[2]} (2 {op_r[3]} 1)))) = {num}"
            print(expr)
            return
    print("No solution found for", num)

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        num = int(line)
        solve(num)

if __name__ == "__main__":
    main()

