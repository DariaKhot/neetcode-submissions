class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict={}
        t_dict={}
        if len(s)!=len(t):
            return False
        for char in s:
            if char not in s_dict:
                s_dict[char]=1
            elif char in s_dict:
                s_dict[char]+=1
        for char in t:
            if char not in t_dict:
                t_dict[char]=1
            elif char in t_dict:
                t_dict[char]+=1
        if s_dict==t_dict:
            return True
        else:
            return False