class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        i, j = len(a) - 1, len(b) - 1
        carry = 0 

        while i >= 0 or j >= 0 or carry > 0:
            an = int(a[i]) if i >= 0 else 0 
            bn = int(b[j]) if j >= 0 else 0 

            sum = an + bn + carry
            digit = sum % 2 
            carry = sum // 2

            res.append(digit)
            i -= 1
            j -= 1

        return ''.join(map(str ,res[::-1]))