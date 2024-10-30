class Solution:
    def longestCommonPrefix(self, strs):
        self.strs = strs
        coincidencias = ""
        max_len = len(min(self.strs, key=len))
        primera_palabra= self.strs[0]
        for i in range(max_len):
            coef = True
            for palabra in self.strs:
                if palabra[i] != primera_palabra[i]:
                    coef = False
            if coef == True:
                coincidencias += palabra[i]
            else:
                return coincidencias

x = ["bola", "bolita", "boliche"]
sol = Solution()
print(sol.longestCommonPrefix(x))