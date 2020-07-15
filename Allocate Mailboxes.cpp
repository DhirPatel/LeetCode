class Solution {
public:
    int minDistance(vector<int>& houses, int K) {
        int l = houses.size();
        if (K >= l){
            return 0;
        }
        sort(houses.begin(),houses.end());
        vector<int> pre(l+1);
        for(int i=0;i<l;i++){
            pre[i+1] = pre[i] + houses[i];
        }
        
        vector<vector<int>> dist(l, vector<int>(l,1e8));
        for(int i=0;i<l;i++){
            dist[i][i] = 0;
            for(int j=i+1;j<l;j++){
                int min_ = 1e8;
                for(int k=i;k<=j;k++){
                    int left = (k-i)*houses[k] - (pre[k]-pre[i]);
                    int right = (pre[j+1]-pre[k+1]) - (j+1-(k+1))*houses[k];
                    min_ = min(min_,left+right);
                }
                dist[i][j] = min_;
            }
        }
        vector<vector<int>> dp(l, vector<int>(K+1,1e8));
        for(int i=0;i<l;i++){
            dp[i][1] = dist[0][i];
        }
        for(int k=2;k<=K;k++){
            for(int i=0;i<l;i++){
                int min_ = 1e8;
                for(int j=k-1;j<=i;j++){
                    min_ = min(min_,dp[j-1][k-1]+dist[j][i]);
                }
                dp[i][k] = min_;
            }
        }
        return dp[l-1][K];
    }
};