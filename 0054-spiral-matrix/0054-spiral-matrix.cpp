#include <ostream>
using namespace std;
#include <vector>
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int top=0;
        int bottom=matrix.size()-1;
        int left=0;
        int right=matrix[0].size()-1;
        auto& m=matrix;
        vector<int> res={};
        while (left<=right && top<=bottom){
            for(int i=left;i<=right;i++){
                 cout<<m[top][i]<<" ";
                 res.push_back(m[top][i]);
            }
            top++;
            for(int i=top;i<=bottom;i++){
                cout<<m[i][right]<<" ";
                res.push_back(m[i][right]);
            }
            right--;
            if(top<=bottom){
                for(int i=right;i>=left;i--){
                    cout<<m[bottom][i]<<" ";
                    res.push_back(m[bottom][i]);
                }
            }
            bottom--;
            if(left<=right){
                for(int i=bottom;i>=top;i--){
                    cout<<m[i][left]<<" ";
                    res.push_back(m[i][left]);
                }
            }
            left++;
        }
        return res;
    };
    

};