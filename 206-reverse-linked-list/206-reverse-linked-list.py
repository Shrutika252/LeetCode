# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        list1=[]
       
        
        while head!=None:
            list1.append(head.val)
            head=head.next
            
        list1.reverse()
        
        
        
        firstnode=ListNode()
        current=firstnode
        
        for i in list1:
            temp=ListNode()
            temp.val=(i)
            current.next=temp
            current=current.next
            
        return firstnode.next

        
        
        
    