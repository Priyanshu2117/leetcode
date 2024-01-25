class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if(x<0):
            return False
        
        if(x>=(-2**31) or x<=(2**31)-1):
            
            reverse =0 
            rem = 0
            original = x

            while(x>0):
                rem = x%10
                reverse = (reverse*10)+rem
                x = x//10

            if(reverse == original):
                return True
            else:
                return False
            
        else: 
            return False
        