# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        num1=''
        num2=''
        res=[]
        result=''
        final=[]
        
        while l1!=None:
            num1=num1+str(l1.val)
            l1=l1.next
            
        while l2!=None:
            num2=num2+str(l2.val)
            l2=l2.next
            
        res=(int(num1)+int(num2))
        result=str(res)
        final=list(result)
        
        firstnode=ListNode()
        current=firstnode
        
        for i in final:
            temp=ListNode()
            temp.val=int(i)
            current.next=temp
            current=current.next
            
        return firstnode.next

        
        
       