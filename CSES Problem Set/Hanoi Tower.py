def hanoi(n, source, target, auxiliary, moves):
    if n == 0:
        return
    hanoi(n - 1, source, auxiliary, target, moves)
    moves.append((source, target))
    hanoi(n - 1, auxiliary, target, source, moves)

# Read single integer input
n = int(input())

moves = []
hanoi(n, 1, 3, 2, moves)

print(len(moves))  # Total moves: 2^n - 1
for a, b in moves:
    print(a, b)
