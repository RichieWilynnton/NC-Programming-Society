class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        for (auto &m : matrix) {
            reverse(m.begin(), m.end());
        }
        int c = 0;
        for (int i=n-1; i>=0; i--) {
            for (int j=0; j < i; j++) {
                swap(matrix[c][j], matrix[n-1-j][n-1-c]);
            }
            c++;
        }
      
        
    }
};
