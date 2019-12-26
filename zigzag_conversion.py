#Runtime: 52 ms, faster than 92.76% of Python3 online submissions for ZigZag Conversion.

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        else:
            d={}
            count=1
            stop=numRows-2
            dec=numRows-1
            for i in s:
                if count < numRows+1:

                    if count not in d:
                        d[count]=i
                    else:
                        d[count]+=i
                    count+=1
                elif count == numRows+1:
                    if dec != 1:
                        d[dec]+=i
                        dec-=1
                    else:
                        d[1]+=i
                        dec=numRows-1
                        count=2   
            ans=""
            for i in d.values():
                ans+=i

            return ans