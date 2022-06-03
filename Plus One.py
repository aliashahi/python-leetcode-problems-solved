class Solution:
    def plusOne(self, digits: list):
        i = 1
        digits[len(digits)-i] += 1
        while digits[len(digits) - i] > 9:
                x = digits[len(digits) - i] 
                digits[len(digits) - i] = x%10
                if i == len(digits):
                    digits = [int(x/10)] + digits
                    break
                digits[len(digits) - i - 1] += int(x/10)
                i+=1
        while digits[0] == 0:
            digits.pop(0)
        return digits
        

x = Solution()
print(x.plusOne([1,2,4]))
print(x.plusOne([1,2]))
print(x.plusOne([1]))
print(x.plusOne([9]))
print(x.plusOne([9,9,9]))