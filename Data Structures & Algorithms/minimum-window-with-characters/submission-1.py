class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ''
        
        need = Counter(t)  # 记录 t 中字符的需求
        missing = len(t)  # 还缺少多少个 t 中的字符
        window = {}
        l = 0
        start = 0  # 记录最小窗口的起始位置
        length = float('inf')
        
        for r, char in enumerate(s):
            if need[char] > 0:  # 说明 char 是 t 需要的字符
                missing -= 1
            need[char] -= 1  # 记录当前窗口中的字符
            
            # 当窗口内已经包含 t 的所有字符
            while missing == 0:
                # 更新最小窗口
                if r - l + 1 < length:
                    length = r - l + 1
                    start = l
                
                # 试图收缩窗口
                need[s[l]] += 1  # 移除 s[l]，恢复需求
                if need[s[l]] > 0:
                    missing += 1  # 如果 s[l] 是 t 需要的字符，missing +1
                l += 1  # 左指针右移
        
        return s[start: start + length] if length != float('inf') else ''
                
                




