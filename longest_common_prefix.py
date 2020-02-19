
def longestCommonPrefix(strs):
    ans = ""

    if (len(strs) > 1) and (len(strs[0]) > 0):
        
        cond = True

        for i in range(len(strs)): 
            ini = 1

            while cond:

                for j in range(i+1,len(strs)):

                    if (strs[i][0:ini] == strs[j][0:ini]) and (len(strs[i]) >= ini):

                        pass
                    
                    else:
                        return ans

                ans = strs[i][0:ini]

                ini += 1
            break
            
    elif len(strs) == 1 and len(strs[0]) > 0:
        return strs[0]

    return ans

# print(longestCommonPrefix(["cdd","cdd","cfe"]))