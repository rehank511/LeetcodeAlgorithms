# Coverting Romans to Integers using Ifs and Elifs
# def romanToInt(self, s: str) -> int:
#         res = 0
#         size = len(s)
        
#         for x in range(size):
#             if s[x] == "M":
#                 res += 1000
#             elif s[x] == "D":
#                 res += 500
#             elif s[x] == "C":
#                 if x < (size-1):
#                     if s[x+1] == "M" or s[x+1] == "D":
#                         res -= 100
#                     else:
#                         res += 100
#                 else:
#                     res += 100
#             elif s[x] == "L":
#                 res += 50
#             elif s[x] == "X":
#                 if x < (size-1):
#                     if s[x+1] == "L" or s[x+1] == "C":
#                         res -= 10
#                     else:
#                         res += 10
#                 else:
#                     res += 10
#             elif s[x] == "V":
#                 res += 5
#             elif s[x] == "I":
#                 if x < (size-1):
#                     if s[x+1] == "V" or s[x+1] == "X":
#                         res -= 1
#                     else:
#                         res += 1
#                 else:
#                     res+=1
    
#         return res
