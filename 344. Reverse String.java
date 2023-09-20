class Solution {
    public void reverseString(char[] s) {
       int start_pointer=0;
       int end_pointer=s.length-1;
       while(start_pointer <end_pointer){
           char temp=s[start_pointer];
           s[start_pointer]=s[end_pointer];
           s[end_pointer]=temp;

           start_pointer +=1;
           end_pointer -=1;

           
       }
      
    }
}
