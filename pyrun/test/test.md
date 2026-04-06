
### cppiostream
```cpp
#inlcude <iostream>
int main() {

    return 0;
}

```


### pythonlcs
```python
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i: int):
            vis[i] = True
            for j, x in enumerate(isConnected[i]):
                if not vis[j] and x:
                    dfs(j)

        n = len(isConnected)
        vis = [False] * n
        ans = 0
        for i in range(n):
            if not vis[i]:
                dfs(i)
                ans += 1
        return ans

```

### javalcs 
```java 
class Solution {
    public int kConcatenationMaxSum(int[] arr, int k) {
        long s = 0, mxPre = 0, miPre = 0, mxSub = 0;
        for (int x : arr) {
            s += x;
            mxPre = Math.max(mxPre, s);
            miPre = Math.min(miPre, s);
            mxSub = Math.max(mxSub, s - miPre);
        }
        long ans = mxSub;
        final int mod = (int) 1e9 + 7;
        if (k == 1) {
            return (int) (ans % mod);
        }
        long mxSuf = s - miPre;
        ans = Math.max(ans, mxPre + mxSuf);
        if (s > 0) {
            ans = Math.max(ans, (k - 2) * s + mxPre + mxSuf);
        }
        return (int) (ans % mod);
    }
}

```
