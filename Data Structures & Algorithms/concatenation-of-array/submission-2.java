class Solution {
    public int[] getConcatenation(int[] nums) {

        int n = nums.length;
        int arrSize = n * 2;
        int[] ans = new int[arrSize];

        for (int i = 0; i < n; i++){
            ans[i] = ans[i + n] = nums[i];
        }
        

        return ans;
    }
}