#!/usr/bin/env python3
import sys
from collections import defaultdict

def build_family_maps(lines, idx, F):
    """
    Reads F lines starting at lines[idx], builds and returns:
      - parent_children: Dict[parent, List[child]]
      - child_parent:   Dict[child, main_parent]
      - spouse_map:     Dict[parent, their_spouse]
    and the updated idx after reading.
    """
    parent_children = defaultdict(list)
    child_parent    = {}
    spouse_map      = {}

    for _ in range(F):
        line = lines[idx]
        idx += 1

        # split parents vs children
        parents_part, children_part = line.split(":")
        parents  = parents_part.strip().split()
        children = children_part.strip().split()

        # record children
        for p in parents:
            parent_children[p].extend(children)

        # map each child to its “main” parent
        main_parent = parents[0]
        for c in children:
            child_parent[c] = main_parent

        # assume exactly two parents → they are spouses
        if len(parents) >= 2:
            a, b = parents[0], parents[1]
            spouse_map[a] = b
            spouse_map[b] = a

    return parent_children, child_parent, spouse_map, idx

def get_nieces(person, parent_children, child_parent):
    """
    Returns a sorted list of all children of person’s siblings
    (i.e. the nieces and nephews of person).
    """
    parent = child_parent.get(person)
    if not parent:
        return []

    siblings = [sib for sib in parent_children[parent] if sib != person]
    nieces = []
    for sib in siblings:
        nieces.extend(parent_children.get(sib, []))
    return sorted(nieces)

def main():
    lines = sys.stdin.read().splitlines()
    idx = 0
    while idx < len(lines):
        # 1) Number of families
        F = int(lines[idx].strip())
        if F == 0:
            break
        idx += 1

        # 2) Build the maps
        parent_children, child_parent, spouse_map, idx = build_family_maps(lines, idx, F)

        # 3) Number of gift‑givers
        G = int(lines[idx].strip())
        idx += 1

        # 4) Process each gift‑giver
        for _ in range(G):
            giver = lines[idx].strip()
            idx += 1

            # get both sets of nieces/nephews
            res1 = get_nieces(giver, parent_children, child_parent)
            spouse = spouse_map.get(giver)
            res2 = get_nieces(spouse, parent_children, child_parent) if spouse else []

            merged = sorted(set(res1 + res2))
            if not merged:
                print(f"{giver} does not need to buy gifts")
            else:
                print(f"{giver} needs to buy gifts for: {', '.join(merged)}")

if __name__ == "__main__":
    main()










