class Solution {
    public String firstPalindrome(String[] words) {
        for(String word:words){
            boolean palin = true;
            int i = 0;
            int stop = word.length()/2;
            while ((palin == true) && (i < stop)){
                if(word.charAt(i) != word.charAt(word.length() - 1 - i)){
                    palin = false;
                }
                i++;
            }
            if(palin == true){
                return word;
            }
        }
        return "";
    }
}
