#!/usr/bin/env python3
import sys

def main():
    def solve (nums):
        # maintain monotonic decreasing stack
        n = len(nums)
        stack = []
        for i in range(0, n):
            while len(stack) > 0 and stack[-1] <= nums[i]:
                stack.pop()
            stack.append(nums[i])   
        return len(stack)
        
    arr = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue  # skip empty lines
        nums = list(map(int, line.split()))
        print(solve(nums))
        

if __name__ == "__main__":
    main()

