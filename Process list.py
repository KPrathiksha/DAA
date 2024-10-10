def process_list(lst):
    if len(lst) == 0 or len(lst) == 1:
        return lst
    
    return sorted(lst)

test_cases = [
    [],                  
    [1],                 
    [7, 7, 7, 7],        
    [-5, -1, -3, -2, -4] 
]

for i, test in enumerate(test_cases):
    print("Test Case",i+1, "Input:",test)
    print("Expected Output:",process_list(test))
