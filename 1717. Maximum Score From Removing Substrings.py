1717. Maximum Score From Removing Substrings

You are given a string s and two integers x and y. You can perform two types of operations any number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.

 

Example 1:

Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.
Example 2:

Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_substring(text, sub, points):
            stack = []
            score = 0
            for char in text:
                if stack and stack[-1] == sub[0] and char == sub[1]:
                    stack.pop()
                    score += points
                else:
                    stack.append(char)
            return ''.join(stack), score

    # Remove the substring with higher points first
        if x > y:
            s, score1 = remove_substring(s, "ab", x)
            s, score2 = remove_substring(s, "ba", y)
        else:
            s, score1 = remove_substring(s, "ba", y)
            s, score2 = remove_substring(s, "ab", x)

        return score1 + score2
