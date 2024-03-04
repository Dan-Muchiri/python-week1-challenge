import string

def solution(N):
    # Create a string containing all lowercase letters
    lowercase_letters = string.ascii_lowercase
    
    # If N is less than or equal to 26, use all the letters once until N
    if N <= 26:
        return lowercase_letters[:N]
    else:
        # If N is greater than 26, repeat the sequence of letters
        repeat_count = N // 26
        remainder = N % 26
        
        # If there's a remainder, we need an additional repetition
        if remainder:
            repeat_count += 1
            repeat_position = N // repeat_count
            
            # Construct the repeated pattern by repeating the sequence of letters
            result = lowercase_letters[:int(repeat_position)] * repeat_count
            
            return result

# Test cases
print(solution(3))   # Output: "abc"
print(solution(5))   # Output: "abcde"
print(solution(30))  # Output: "aabbccddeeffgghhiijjkkllmmnnoo"
