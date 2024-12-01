class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hash_set = set(arr)
        for i in hash_set:
            if arr.count(0) >= 2:
                return True
            if i!=0 and 2*i in hash_set:
                return True
        return False