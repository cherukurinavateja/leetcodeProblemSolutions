#Runtime: 32 ms, faster than 84.12% of Python3 online submissions for String to Integer (atoi).
class Solution:
    def myAtoi(self, st):
        nums=['-','0','1','2','3','4','5','6','7','8','9','+']
        if (st == "") or (st.strip() == "") :
            return 0
        else:
            string=st.strip()
            num=""
            for i in string:
                if i in nums:
                    if (i == '-') or (i =='+'):
                        if len(num) > 0:
                            break
                        else:
                            num+=i
                    else:
                        num+=i
                else:
                    break

            if len(num)==0:
                return 0
            else:
                try:
                    ans=int(num)
                except ValueError:
                    ans=0
                if (ans < -(2**31)):
                    return -(2**31)
                elif (ans > (2**31)-1):
                    return (2**31)-1
                else:
                    return ans