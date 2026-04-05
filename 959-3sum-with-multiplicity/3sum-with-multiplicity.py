import collections

class Solution(object):
    def threeSumMulti(self, arr, target):
        MOD = 10**9 + 7
        count = collections.Counter(arr)
        keys = sorted(count.keys())
        
        ans = 0
        
        for i in range(len(keys)):
            x = keys[i]
            T = target - x
            
            j, k = i, len(keys) - 1
            while j <= k:
                y, z = keys[j], keys[k]
                
                if y + z < T:
                    j += 1
                elif y + z > T:
                    k -= 1
                else:
                    if i == j == k:
                        n = count[x]
                        ans += n * (n - 1) * (n - 2) // 6
                    
                    elif i == j != k:
                        n, m = count[x], count[z]
                        ans += n * (n - 1) // 2 * m
                    
                    elif i != j == k:
                        n, m = count[x], count[y]
                        ans += n * m * (m - 1) // 2
                    
                    else:
                        ans += count[x] * count[y] * count[z]
                    
                    ans %= MOD
                    j += 1
                    k -= 1
                    
        return int(ans)