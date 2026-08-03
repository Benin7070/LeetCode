class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int ttl=0,res=0;
        unordered_map<int ,int> hashmap;
        hashmap[0]=1;
        for(int i=0;i<nums.size();i++){
            ttl+=nums[i];
            if (hashmap.find(ttl-k)!=hashmap.end()){
                    res += hashmap[ttl - k];
                    cout<<hashmap[ttl-k]<<" ";
            }
            hashmap[ttl]++;
        }
        return res;
    }
};