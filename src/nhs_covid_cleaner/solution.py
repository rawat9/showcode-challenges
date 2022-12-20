class Solution:
    def cleaner(self, data) -> list[int]:
        return []


sol = Solution()
sol.cleaner(["60", "36", "24", "22"])

"""
[ 
	"Cases" : Isolating + In Care else 0
	"Isolation": -
	"In Care": includes ICU
	"ICU": subset of In care
]
"""
