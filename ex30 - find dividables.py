MAX_N = 10000
prime = [0] * (MAX_N + 5)

# # version 1 - find all none dividable number
# for i in range(2, MAX_N + 1): 
#     # print(f"\ni: {i}")
#     if (prime[i] == 0):
#         for j in range(i, MAX_N + 1, i):
#             # print(f"j: {j}")
#             prime[j] = 1;
        
# for i in range(2, MAX_N + 1):
#     if (prime[i] == 0):
#         print(f"{i}: {prime[i]}")

# # version 2 - using the idea from v1 to find smallest dividable value for all numbers 
# for i in range(2, MAX_N + 1): 
#     if (prime[i] == 0):
#         for j in range(i, MAX_N + 1, i):
#             if (prime[j] == 0): prime[j] = i

# for i in range(2, 20):
#     print(f"prime[{str(i).zfill(2)}]: {prime[i]}")

# version 3 - use the idea from v2 to find all the divide number, ie: 12 = 2 * 2 * 3, 10 = 2 * 5
for i in range(2, MAX_N + 1): 
    if (prime[i] == 0):
        for j in range(i, MAX_N + 1, i):
            if (prime[j] == 0): prime[j] = i

for i in range(2, 20):
    print(f"prime[{str(i).zfill(2)}]: {prime[i]}")

while True:
    val = input("Enter your value: ")
    n, result = int(val), []
    while n > 1:
        result.append(prime[n])
        n = int(n / prime[n])
        # print(f"n -> {n}, prime[n] -> {prime[n]}")
    print(f"{val}: {' '.join(map(str, result))}")