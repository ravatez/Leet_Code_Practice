class Solution:
    def fractionAddition(self, expression: str) -> str:
        pattern = re.compile(r"(.*?)([0-9]+)/([0-9]+)")
        triplets = pattern.findall(expression)

        num = 0
        den = 1

        for triplet in triplets:
            sign, n, d = triplet
            n = int(n)
            d = int(d)

            if sign == "-":
                num = num * d - n * den
            else:
                num = num * d + n * den
            den *= d
        
        while math.gcd(num, den) > 1:
            gcd = math.gcd(num, den)
            num /= gcd
            num = int(num)
            den /= gcd
            den = int(den)
        
        res = ""
        res += str(num)
        res += "/"
        res += str(den)
        
        return res