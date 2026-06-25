class Solution {
    public int[] getConcatenation(int[] nums) {
        int length = nums.length * 2;
        List<Integer> newList = new ArrayList<>();
        int[] ans = new int[length];

        for(int i = 0; i < 2; i++){
            for(int num : nums){ 
                newList.add(num);
            }
        }

        for(int i = 0; i < length; i++){
            ans[i] = newList.get(i);
        }
        

        return ans;
    }
}