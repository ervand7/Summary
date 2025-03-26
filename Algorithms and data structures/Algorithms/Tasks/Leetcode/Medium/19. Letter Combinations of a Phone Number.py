# ChatGPT solution
def letter_combinations(digits: str) -> list[str]:
    if not digits:
        return []

    phone_map = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }

    result = []

    def backtrack(index: int, path: str):
        if index == len(digits):
            result.append(path)
            return

        possible_letters = phone_map[digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)

    backtrack(0, "")
    return result


# Test examples:
print(letter_combinations("234"))

# Below is one way to visualize how the backtracking recursion flows for the input
# `"234"`. We'll show a *recursion tree* that illustrates each function call
# (`backtrack`) and the path (partial combination) it builds:
#
# ---
#
# ## Mapping
# - **2** → `abc`
# - **3** → `def`
# - **4** → `ghi`
#
# ---
#
# ## Recursion Tree
#
# We start at `index=0` with an empty `path=""`.
#
# 1. **First digit = '2'** (possible letters: `a, b, c`)
#
#    - **Pick `'a'`**
#      - Now `index=1, path="a"`
#      - **Second digit = '3'** (possible letters: `d, e, f`)
#
#        - **Pick `'d'`**
#          - `index=2, path="ad"`
#          - **Third digit = '4'** (possible letters: `g, h, i`)
#
#            - **Pick `'g'`**
#              - `index=3, path="adg"` → **Reached end** → Add `"adg"` to result
#
#            - **Pick `'h'`**
#              - `index=3, path="adh"` → **Reached end** → Add `"adh"` to result
#
#            - **Pick `'i'`**
#              - `index=3, path="adi"` → **Reached end** → Add `"adi"` to result
#
#        - **Pick `'e'`**
#          - `index=2, path="ae"`
#          - **Third digit = '4'** (possible letters: `g, h, i`)
#
#            - **Pick `'g'`** → `index=3, path="aeg"` → **Add `"aeg"`**
#            - **Pick `'h'`** → `index=3, path="aeh"` → **Add `"aeh"`**
#            - **Pick `'i'`** → `index=3, path="aei"` → **Add `"aei"`**
#
#        - **Pick `'f'`**
#          - `index=2, path="af"`
#          - **Third digit = '4'** (possible letters: `g, h, i`)
#
#            - **Pick `'g'`** → `index=3, path="afg"` → **Add `"afg"`**
#            - **Pick `'h'`** → `index=3, path="afh"` → **Add `"afh"`**
#            - **Pick `'i'`** → `index=3, path="afi"` → **Add `"afi"`**
#
#    ---
#    - **Pick `'b'`**
#      - Now `index=1, path="b"`
#      - **Second digit = '3'** (possible letters: `d, e, f`)
#
#        - **Pick `'d'`**
#          - `index=2, path="bd"`
#          - **Third digit = '4'** → letters `g, h, i`
#
#            - **Pick `'g'`** → `index=3, path="bdg"` → **Add `"bdg"`**
#            - **Pick `'h'`** → `index=3, path="bdh"` → **Add `"bdh"`**
#            - **Pick `'i'`** → `index=3, path="bdi"` → **Add `"bdi"`**
#
#        - **Pick `'e'`**
#          - `index=2, path="be"`
#          - **Third digit = '4'** → letters `g, h, i`
#
#            - **Pick `'g'`** → `index=3, path="beg"` → **Add `"beg"`**
#            - **Pick `'h'`** → `index=3, path="beh"` → **Add `"beh"`**
#            - **Pick `'i'`** → `index=3, path="bei"` → **Add `"bei"`**
#
#        - **Pick `'f'`**
#          - `index=2, path="bf"`
#          - **Third digit = '4'** → letters `g, h, i`
#
#            - **Pick `'g'`** → `index=3, path="bfg"` → **Add `"bfg"`**
#            - **Pick `'h'`** → `index=3, path="bfh"` → **Add `"bfh"`**
#            - **Pick `'i'`** → `index=3, path="bfi"` → **Add `"bfi"`**
#
#    ---
#    - **Pick `'c'`**
#      - Now `index=1, path="c"`
#      - **Second digit = '3'** (possible letters: `d, e, f`)
#
#        - **Pick `'d'`**
#          - `index=2, path="cd"`
#          - **Third digit = '4'** → letters `g, h, i`
#
#            - **Pick `'g'`** → `index=3, path="cdg"` → **Add `"cdg"`**
#            - **Pick `'h'`** → `index=3, path="cdh"` → **Add `"cdh"`**
#            - **Pick `'i'`** → `index=3, path="cdi"` → **Add `"cdi"`**
#
#        - **Pick `'e'`**
#          - `index=2, path="ce"`
#          - **Third digit = '4'** → letters `g, h, i`
#
#            - **Pick `'g'`** → `index=3, path="ceg"` → **Add `"ceg"`**
#            - **Pick `'h'`** → `index=3, path="ceh"` → **Add `"ceh"`**
#            - **Pick `'i'`** → `index=3, path="cei"` → **Add `"cei"`**
#
#        - **Pick `'f'`**
#          - `index=2, path="cf"`
#          - **Third digit = '4'** → letters `g, h, i`
#
#            - **Pick `'g'`** → `index=3, path="cfg"` → **Add `"cfg"`**
#            - **Pick `'h'`** → `index=3, path="cfh"` → **Add `"cfh"`**
#            - **Pick `'i'`** → `index=3, path="cfi"` → **Add `"cfi"`**
#
# ---
#
# ## Final Combinations
#
# By the end, the algorithm collects all these 27 combinations:
#
# ```
# [
#  "adg","adh","adi","aeg","aeh","aei","afg","afh","afi",
#  "bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi",
#  "cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"
# ]
# ```
#
# Each branch of the recursion picks one letter from the current digit and then moves on to pick one from the next digit, and so on, until it has chosen one letter for *every* digit. The tree format helps see how paths extend character by character in a systematic (depth-first) manner.