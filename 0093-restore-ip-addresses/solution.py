from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        n = len(s)
        # 有効なIPv4アドレスは最大12文字 (4つのセグメント × 最大3文字) なので、
        # 12文字を超える場合は即座に空リストを返す（枝刈り）
        if n > 12:
            return []
            
        def backtrack(start: int, path: List[str]):
            # 4つのセグメントが決定した場合
            if len(path) == 4:
                # 文字列をすべて使い切っている場合のみ有効なIPアドレスとして追加
                if start == n:
                    res.append(".".join(path))
                return
                
            # 各セグメントは1文字から最大3文字まで
            for length in range(1, 4):
                if start + length > n:
                    break
                    
                segment = s[start:start+length]
                
                # 枝刈り：リーディングゼロのチェック（"0"は許容されるが、"01"などは無効）
                if len(segment) > 1 and segment[0] == '0':
                    continue
                # 枝刈り：値が255以下であることのチェック
                if int(segment) > 255:
                    continue
                    
                path.append(segment)
                backtrack(start + length, path)
                path.pop()
                
        backtrack(0, [])
        return res

