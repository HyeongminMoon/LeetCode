# 1. str.split과 stack을 활용하여 풀이
# time: O(n)
# space: O(n)

from collections import deque 

class Solution:
    def simplifyPath(self, path: str) -> str:
        routes = path.split('/')
        
        result = deque() # stack은 효율적인 deque 사용
        for route in routes:
            if not route: # 빈 route는 // 같은 경우를 의미한다. 이를 스킵하여 단일 /로 변환하는 효과 + 마지막 /는 무시됨
                continue
            
            # '.' 패턴 처리
            if route == '.':
                continue
            
            # '..' 패턴 처리
            if route == '..':
                # 앞의 route가 있다면, stack에서 pop하는 형태
                if result:
                    result.pop()
                continue 
            
            # 위 두 패턴에 해당하지 않는 경우, append
            result.append(route)
        
        return '/' + '/'.join(result)