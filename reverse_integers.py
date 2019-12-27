
#solution 1
class Solution:
    def reverse(self, x):
        neg=False
        rev=0
        if "-" in str(x):
            x=str(x)
            neg=True
            x=int(x.replace("-",""))
        while(x>0):
            dig=x%10
            rev=rev*10+dig
            x=x//10
        if neg:
            ans="-"
            ans+=str(rev)
            rev=int(ans)
        if (rev > (2**31)-1) or (rev < -(2**31)):
            return 0
        else:
            return rev 

#alternate way
class AlternateSolution:
    def reverse(self, x):
        int_to_string_x=str(x)
        if "-" in int_to_string_x:
            ans="-"
            ans+=int_to_string_x[:0:-1]
            fin_ans=int(ans)
        else:
            ans=int_to_string_x[::-1]
            fin_ans=int(ans)
        if (fin_ans > (2**31)-1) or (fin_ans < -(2**31)):
            return 0
        else:
            return fin_ans