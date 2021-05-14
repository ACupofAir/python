#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;
#define N 1007

int c[N],w[N],dp[N];

int main()
{
    int t,i,n,V,v;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d",&n,&V);
        for(i=1;i<=n;i++)
            scanf("%d",&c[i]);
        for(i=1;i<=n;i++)
            scanf("%d",&w[i]);
        memset(dp,0,sizeof(dp));
        for(i=1;i<=n;i++)
        {
            for(v=V;v>=w[i];v--)
                dp[v] = max(dp[v],dp[v-w[i]]+c[i]);
        }
        int res = -1;
        for(i=0;i<=V;i++)
            res = max(res,dp[i]);
        printf("%d\n",res);
    }
    return 0;
}
