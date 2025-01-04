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
    if solution.solution("()") != True:
        print("Test case 1 failed")
        failed += 1
    if solution.solution("())") != False:
        print("Test case 2 failed")
        failed += 1
    if solution.solution("(())") != True:
        print("Test case 3 failed")
        failed += 1
    
    if failed == 0:
        print("All test cases passed")
    return failed

def test_assignment2(solution):
    # Test all the possibliities of the function and print if test case failed
    # Before returning print how many are failed
    failed = 0
    if solution.solution(1) != 1:
        print("Test case 1 failed")
        failed += 1
    if solution.solution(2) != 1:
        print("Test case 2 failed")
        failed += 1
    if solution.solution(3) != 2:
        print("Test case 3 failed")
        failed += 1
    
    if failed == 0:
        print("All test cases passed")
    return failed

def test_assignment3(solution):
    # Test all the possibliities of the function and print if test case failed
    # Before returning print how many are failed
    failed = 0
    if solution.solution(1) != 1:
        print("Test case 1 failed")
        failed += 1
    if solution.solution(2) != 1:
        print("Test case 2 failed")
        failed += 1
    if solution.solution(3) != 2:
        print("Test case 3 failed")
        failed += 1
    
    if failed == 0:
        print("All test cases passed")
    return failed

def test_assignment4(solution):
    # Test all the possibliities of the function and print if test case failed
    # Before returning print how many are failed
    failed = 0
    if solution.solution(1) != 1:
        print("Test case 1 failed")
        failed += 1
    if solution.solution(2) != 1:
        print("Test case 2 failed")
        failed += 1
    if solution.solution(3) != 2:
        print("Test case 3 failed")
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
    print('Testing solution', soultion)
    prob_statement = re.findall(r".*/(.*)\.py'\>$", str(soultion))
    try:
        print(">>> Testing solution for ", prob_statement[0])
    except IndexError:
        print### Issue in parsing Testing solution for ", soultion)
        exit(1)
    # measure the time taken to run the test cases
    start = time()
    failed = test_solutions[prob_statement[0]](soultion)
    end = time()
    print(f"Time taken to test the solution: {end - start} seconds")
    return failed