def solution(A):
    total_bricks = sum(A)
    num_boxes = len(A)
    target_bricks = total_bricks // num_boxes
    
    if total_bricks % num_boxes != 0:
        return -1
    
    moves = 0
    for i in range(num_boxes):
        diff = A[i] - target_bricks
        
        if diff > 0:  # If the box has excess bricks
            # Distribute excess bricks optimally to adjacent boxes
            for j in range(i + 1, num_boxes):
                if A[j] < target_bricks:
                    to_move = min(diff, target_bricks - A[j])
                    A[i] -= to_move
                    A[j] += to_move
                    moves += to_move * (j - i)  # Number of moves is proportional to the distance between boxes
                    diff -= to_move
                    if diff == 0:
                        break
            for j in range(i - 1, -1, -1):
                if A[j] < target_bricks:
                    to_move = min(diff, target_bricks - A[j])
                    A[i] -= to_move
                    A[j] += to_move
                    moves += to_move * (i - j)  # Number of moves is proportional to the distance between boxes
                    diff -= to_move
                    if diff == 0:
                        break
        elif diff < 0:  # If the box has deficient bricks
            # Distribute deficient bricks optimally to adjacent boxes
            for j in range(i + 1, num_boxes):
                if A[j] > target_bricks:
                    to_move = min(-diff, A[j] - target_bricks)
                    A[i] += to_move
                    A[j] -= to_move
                    moves += to_move * (j - i)  # Number of moves is proportional to the distance between boxes
                    diff += to_move
                    if diff == 0:
                        break
            for j in range(i - 1, -1, -1):
                if A[j] > target_bricks:
                    to_move = min(-diff, A[j] - target_bricks)
                    A[i] += to_move
                    A[j] -= to_move
                    moves += to_move * (i - j)  # Number of moves is proportional to the distance between boxes
                    diff += to_move
                    if diff == 0:
                        break
    
    return moves

# Test cases
print(solution([7, 15, 10, 8]))  # Output: 7
print(solution([11, 10, 8, 12, 8, 10, 11]))  # Output: 6
print(solution([7, 14, 10]))  # Output: -1
