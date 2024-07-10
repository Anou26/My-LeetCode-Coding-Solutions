class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        def backtrack(index, path):
            if index == len(digits):
                combinations.append("".join(path))
                return

            possible_letters = phone[digits[index]]
            for letter in possible_letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()

        combinations = []
        backtrack(0, [])
        return combinations

# Example usage:
sol = Solution()
print(sol.letterCombinations("23"))  # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(sol.letterCombinations(""))    # Output: []
print(sol.letterCombinations("2"))   # Output: ["a","b","c"]
