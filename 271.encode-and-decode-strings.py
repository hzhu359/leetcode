#
# @lc app=leetcode id=271 lang=python3
#
# [271] Encode and Decode Strings
#

# @lc code=start
class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        ret = strs[0] 
        for s in strs[1:]:
            ret += f'🤠{s}'
        return ret

        

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        return s.split('🤠')
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
# @lc code=end

