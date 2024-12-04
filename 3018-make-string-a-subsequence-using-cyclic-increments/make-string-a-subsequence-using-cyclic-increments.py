class Solution:
    def canMakeSubsequence(self, source: str, target: str) -> bool:
        source_length = len(source)
        target_len = len(target)
        source_index = 0
        target_index = 0
        
        while source_index < source_length and target_index < target_len:
            if (source[source_index] == target[target_index] or 
                (source[source_index] == 'z' and target[target_index] == 'a') or 
                (ord(source[source_index]) + 1 == ord(target[target_index]))):
                source_index += 1
                target_index += 1
            else:
                source_index += 1
                
        return target_index == target_len