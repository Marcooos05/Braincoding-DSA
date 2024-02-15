

class Solution {
    public boolean isAnagram(String s, String t) {
        char[] sArray = s.toCharArray();
        char[] tArray = t.toCharArray();
        Arrays.sort(sArray);
        Arrays.sort(tArray);
        System.out.println(sArray);
        System.out.println(tArray);
        if (Arrays.equals(sArray,tArray)){
            return true;
        }
        return false;
    }
}
