# bracket_balancing.py

def is_balanced(expression: str) -> bool:
    """
    Check if all brackets in the expression are balanced.
    
    Supports: (), {}, []
    
    Parameters:
        expression (str): The input string to check.
    
    Returns:
        bool: True if brackets are balanced, False otherwise.
    """
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map:
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()

    return not stack


if __name__ == "__main__":
    # Example usage when running as a script
    test_input = input("Enter an expression to check for balanced brackets: ")
    if is_balanced(test_input):
        print("Brackets are balanced ✅")
    else:
        print("Brackets are NOT balanced ❌")
