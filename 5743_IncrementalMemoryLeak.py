from typing import List

class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        if memory1 == 0:
            isMem1Crash = True
        else:
            isMem1Crash = False

        if memory2 == 0:
            isMem2Crash = True
        else:
            isMem2Crash = False
        
        avMem1 = memory1
        avMem2 = memory2
        i = 1
        while not isMem1Crash or not isMem2Crash:
            if avMem1 >= avMem2 and not isMem1Crash:
                if avMem1 < i:
                    isMem1Crash = True
                else:
                    avMem1 -= i
            elif avMem1 < avMem2 and not isMem2Crash or isMem1Crash:
                if avMem2 < i:
                    isMem2Crash = True
                else:
                    avMem2 -= i
            i += 1
        
        return [i-2, avMem1, avMem2]

obj = Solution()
res = obj.memLeak(2,2)
print(res)