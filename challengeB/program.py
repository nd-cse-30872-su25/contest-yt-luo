#!/usr/bin/env python3
import sys

def main():
    def solve (s, t):
        if len(s) != len(t):
            return False
        n = len(s)
        mapping = {}
        for i in range (n):
            if s[i] in mapping:
                if mapping.get(s[i]) != t[i]:
                    return False
            else:
                mapping[s[i]] = t[i] 
        return True
                
    for line in sys.stdin:
        line = line.strip()
        s, t = line.split()
        if solve(s, t):
            print("Isomorphic")
        else:
            print("Not Isomorphic")


if __name__ == "__main__":
    main()
