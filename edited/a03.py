import utils
import tester

DEBUG_03 = False

def coin_game(input_as_string_list):
    inp = utils.handle_input(input_as_string_list)
    assert len(input_as_string_list) >= 2
    num_coins, num_instructions = map(int, inp().split())
    coins = set(map(int, inp().split()))

    max_target = 10**5
    dp = [float('inf')] * (max_target + 1)
    dp[0] = 0
    dp_valid = False

    def recompute_dp():
        nonlocal dp, dp_valid
        dp = [float('inf')] * (max_target + 1)
        dp[0] = 0
        sorted_coins = sorted(coins)
        for x in range(1, max_target + 1):
            for coin in sorted_coins:
                if x >= coin:
                    dp[x] = min(dp[x], dp[x - coin] + 1)
                else:
                    break
        dp_valid = True

    def display_min_coins(target):
        nonlocal dp, dp_valid
        if not dp_valid:
            recompute_dp()
        return (dp[target] if dp[target] != float('inf') else -1)

    output = []
    for _ in range(num_instructions):
        tmp_line = inp().split()
        instruction, number = tmp_line[0], int(tmp_line[1])
        
        if DEBUG_03:
            print("instruction:", instruction)
            print("number:", number)
            print("coins:", coins)

        if instruction == "Q":
            output.append(str(display_min_coins(number)) + "\n")
        elif instruction == "X":
            coins.discard(number)
            dp_valid = False
        else:
            raise RuntimeError("Unreachable")
    return output

if __name__ == "__main__":
    tester.test_03()