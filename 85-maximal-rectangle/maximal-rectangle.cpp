class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        if (matrix.empty()) return 0;
        int n = matrix.size(), m = matrix[0].size(), ans=0;
        vector<vector<int> > psa;
        for (vector<char>& i : matrix) {
            vector<int> l = {0};
            int cur = 0;
            for (int j : i) l.push_back(cur += j-'0');
            psa.push_back(l);
        }
        for (int i=0; i<m; i++) {
            for (int j=i; j<m; j++) {
                int cur = 0;
                for (int k=0; k<n; k++) {
                    if (psa[k][j+1]-psa[k][i] == j-i+1) ans = max(ans, (j-i+1)*(++cur));
                    else cur = 0;
                } 
                ans = max(ans, (j-i+1)*cur);
            }
        }
        return ans;
        
    }
};