class Solution:
    def isValid(self, s: str) -> bool:
        parentheses={"(":")","[":"]","{":"}"}

        stack=[]

        for i in s:
            try:

                if i not in parentheses.values():
                    stack.append(i)
                
                elif i ==")":
                    if stack[-1]=="(":
                        stack.pop()
                    else:
                        return False
                
                elif i =="]":
                    if stack[-1]=="[":
                        stack.pop()
                    else:
                        return False
                
                elif i =="}":
                    if stack[-1]=="{":
                        stack.pop()
                    else:
                        return False
            except:
                return False
            
                
        
        if len(stack)>0:
            return False
        
        return True

            
