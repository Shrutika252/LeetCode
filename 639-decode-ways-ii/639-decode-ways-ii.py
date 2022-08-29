class Solution:
    def numDecodings(self, s: str) -> int:
       
    # set default value is 1
        answer = 1
        prev_answer = 1
        # the prev value is 1, 2 or not
        one, two = False, False
        for i in s:
            if i == '*':
                new = answer*9
                if one:
                    new += 9*prev_answer
                if two:
                    new += 6*prev_answer
                one, two = True, True
            else:
                # drop it if meet 0
                new = answer if (i > '0') else 0
                if one:
                    new += prev_answer
                if (two and i <= '6'):
                    new += prev_answer
                one = (i == '1')
                two = (i == '2')
            prev_answer = answer
            answer = new % (10**9 + 7)
        return answer