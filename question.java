/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        Listnode res = new ListNode();
        int power = 0;
        while(true){
            boolean l1Null = l1 == null;
            boolean l2Null = l2 == null;
            if (l1Null && l2Null) return res;
            res.val +=(l1Null? 0 : l1.val + l2Null? 0 : l2.val) *  Math.pow(10, power);
            power ++;

            if (! l1Null)
                l1 = l1.next();
            if (!l2Null)
                l2 = l2.next();
        }
    }
}