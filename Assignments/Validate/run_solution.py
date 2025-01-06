import re
import sys
from time import time

# Function to test the solution
# The function takes the solution as input and returns the number of test cases failed
def test_assignment1(solution):
    # Test all the possibliities of the function and print if test case failed
    # Before returning print how many are failed
    failed = 0
    print("In test_assignment1")
    if solution.Solution("()") != True:
        print("Test case 1 failed")
        failed += 1
    if solution.Solution("())") != False:
        print("Test case 2 failed")
        failed += 1
    if solution.Solution("(())") != True:
        print("Test case 3 failed")
        failed += 1
    
    if failed == 0:
        print("All test cases passed")
    return failed

def test_assignment2(solution):
    # Test all the possibliities of the function and print if test case failed
    # Before returning print how many are failed
    failed = 0
    if solution.Solution("11", "01") != "100":
        print("Test case 1 failed")
        failed += 1
    if solution.Solution("110011", "1100") != "111111":
        print("Test case 2 failed")
        failed += 1

    if failed == 0:
        print("All test cases passed")
    return failed

def test_assignment3(solution):
    # Test all the possibliities of the function and print if test case failed
    # Before returning print how many are failed
    failed = 0
    if solution.Solution(2) != 2:
        print("Test case 1 failed")
        failed += 1
    if solution.Solution(2) != 3:
        print("Test case 2 failed")
        failed += 1
    
    if failed == 0:
        print("All test cases passed")
    return failed


#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def test_assignment4(solution):
    # Test all the possibliities of the function and print if test case failed
    # Before returning print how many are failed
    failed = 0

    # Test case1
    l1 = ListNode(1)
    l2 = ListNode(2)
    l1.next = l2
    l3 = ListNode(1)
    l2.next = l3
    l4 = ListNode(2)
    l3.next = l4

    result = solution.Solution(l1)
    nums = []
    while result:
        nums.append(result.val)
        result = result.next
    if set(nums) - set(1,2) != set():
        print("Test case 1 failed")
        failed += 1



    # Test case2
    l1 = ListNode(1)
    l2 = ListNode(1)
    l1.next = l2
    l3 = ListNode(1)
    l2.next = l3

    result = solution.Solution(l1)
    nums = []
    while result:
        nums.append(result.val)
        result = result.next
    if set(nums) - set(1) != set():
        print("Test case 2 failed")
        failed += 1
    
    if failed == 0:
        print("All test cases passed")
    return failed

    


# Dictionary of all problem statements and its test cases function. The function returns number of test cases failed.
test_solutions = {
    'Assignment1': test_assignment1,
    'Assignment2': test_assignment2,
    'Assignment3': test_assignment3,
    'Assignment4': test_assignment4
}

def test_solution(soultion):
    prob_statement = re.findall(r".*/(.*)\.py'\>$", str(soultion))
    # measure the time taken to run the test cases
    start = time()
    failed = test_solutions[prob_statement[0]](soultion)
    end = time()
    return failed