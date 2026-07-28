#include <sstream>
#include <string>
#include <vector>
using namespace std;
class Solution {
public:
    string reverseWords(string s) {
        stringstream ss(s);
        string token;
        vector<string> tokens;
        string res;

        while (ss >>token){
            tokens.push_back(token);
        }

        for (int i=tokens.size()-1;i>=0;i--){
            res+=tokens[i];
            if (i>0){
                res+=" ";
            }
        }
        return res;
    }
};