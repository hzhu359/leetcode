class ListNode {
    int val;
    ListNode next;

    ListNode(int val) {
        this.val = val;
        this.next = null;
    }
}

class Test {
    public static void main(String[] args) {
        ListNode head = new ListNode(-1);
        ListNode curr = head;
        addLast(curr, new ListNode(1));
        addLast(curr, new ListNode(2));
        addLast(curr, new ListNode(3));
        addLast(curr, new ListNode(4));

        while (head != null) {
            System.out.println(head.val);
            head = head.next;
        }
    }
    static void addLast(ListNode curr, ListNode newNode) {
        curr.next = newNode;
        curr = curr.next;
    }
}
