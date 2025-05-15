
fn main() {
    let test = [2,4,3];
    let test_2 = [5,6,4];
    let node_object_1 = ListNode::create_node(&test);
    let node_object_2 = ListNode::create_node(&test_2);
    let mut wynik = Solution::add_two_numbers(node_object_1, node_object_2);

    while let Some(node) = wynik {
        println!("{}", node.val);
        wynik = node.next;
    }

}

struct Solution {}

impl Solution {
    pub fn add_two_numbers(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut result = Box::new(ListNode::new(0));
        let mut current = &mut result;
        let mut carry = 0;

        let mut p1 = l1.as_ref();
        let mut p2 = l2.as_ref();

        while p1.is_some() || p2.is_some() || carry != 0 {
            let val1 = p1.map_or(0, |node| node.val);
            let val2 = p2.map_or(0, |node| node.val);

            let total = val1 + val2 + carry;

            current.next = Some(Box::new(ListNode::new(total % 10)));
            current = current.next.as_mut().unwrap();
            carry = total / 10;

            if let Some(node) = p1 {
                p1 = node.next.as_ref();
            } else {
                p1 = None;
            }

            if let  Some(node) = p2 {
                p2 = node.next.as_ref();
            } else {
                p2 = None;
            }
        }
        result.next
    }
}



#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>
}

impl ListNode {
   #[inline]
    fn new(val: i32) -> Self {
    ListNode {
        next: None,
        val
        }
    }
    fn create_node(arr: &[i32])  -> Option<Box<ListNode>> {
        if arr.is_empty() {
            return None;
        }
        let mut head = Box::new(ListNode::new(arr[0]));
        let mut current = &mut head;

        for val in &arr[1..] {
            current.next = Some(Box::new(ListNode::new(*val)));
            current = current.next.as_mut().unwrap();
        }
        Some(head)
    }
}



/*




pub struct ListNode {
    val: i32,
    next: Option<Box<ListNode>>
}


impl ListNode {
    pub fn new(val: i32) -> Self {
       ListNode {val, next: None}
    }

    pub fn create_node(arr: &[i32]) -> Option<Box<ListNode>> {
        if arr.is_empty() {
            return None;
        }
        let mut head = Box::new(ListNode::new(arr[0]));
        let mut current = &mut head;

        for val in &arr[1..] {
            current.next = Some(Box::new(ListNode::new(*val)));
            current = current.next.as_mut().unwrap();
        }
        Some(head)
    }
}


*/
