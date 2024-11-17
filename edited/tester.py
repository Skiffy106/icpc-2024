import a9
import os
import glob
import random
import io
import concurrent.futures

from time import time

SEED = "ICPC"
TEST_9 = True
RANDOM_NUMS = 10 ** 4
NUM_ITERS = 4
TIMEOUT_TIME = 10


def test_9():
    print("Testing Problem 9")
    print("-" * 20)
    print("Sample Input")
    print("-" * 20)

    edited_file_folder = os.path.dirname(os.path.abspath(__file__))
    icpc_folder = os.path.dirname(edited_file_folder)
    path = os.path.join(icpc_folder, "samples-09", "*.in")

    for input_path in glob.glob(path):
        with open(input_path, "r") as f:
            rel_name = os.path.basename(input_path)
            print(f"Test {rel_name}: ", end='')

            input_as_string = f.read().replace('\n', '')
            if len(input_as_string) > 10:
                print(f"{input_as_string[:10]}...")
            else:
                print(input_as_string)

            test_folder = os.path.dirname(input_path)
            base_name =  os.path.splitext(rel_name)[0]
            answer_file = open(os.path.join(test_folder, f"{base_name}.ans"), "r")
            answer = int(answer_file.read().replace('\n', ''))
            answer_file.close()

            print("Brute force:")
            start_time = time()
            result1 = a9.bf_solve(input_as_string)
            end_time = time()
            if result1 == answer:
                print("Correct!")
            else:
                print("Incorrect!")
                print(f"Answer: {answer}, got: {result1}")
            print(f"Time: {round((end_time - start_time) * 1_000)} ms\n")

            print("DP - simple:")
            start_time = time()
            result2 = a9.dp_simple_solve(input_as_string)
            end_time = time()
            if result2 == answer:
                print("Correct!")
            else:
                print("Incorrect!")
                print(f"Answer: {answer}, got: {result2}")
            print(f"Time: {round((end_time - start_time) * 1_000)} ms")

            print("-" * 20)

    print("Random Input")
    print("-" * 20)

    CHAR_OFFSET = ord("A")
    for _ in range(NUM_ITERS):
        string_buffer = io.StringIO()
        for _ in range(RANDOM_NUMS):
            string_buffer.write(chr(CHAR_OFFSET + random.randint(0, 25)))
        result = string_buffer.getvalue()

        print(f"Input: {result[:15]}...\n")
        print("Brute force:")
        start_time = time()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(a9.bf_solve, result)
            try:
                result1 = future.result(TIMEOUT_TIME)
            except TimeoutError:
                print(f"Function execution timed out after {TIMEOUT_TIME} seconds")
                future.cancel()
        end_time = time()
        print(f"Result: {result1}")
        print(f"Time: {round((end_time - start_time) * 1_000)} ms\n")

        print("DP - simple:")
        start_time = time()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(a9.dp_simple_solve, result)
            try:
                result1 = future.result(TIMEOUT_TIME)
            except TimeoutError:
                future.cancel()
                print(f"Function execution timed out after {TIMEOUT_TIME} seconds")
        end_time = time()
        print(f"Result: {result2}")
        print(f"Time: {round((end_time - start_time) * 1_000)} ms")
        print("-" * 20)



if __name__ == "__main__":
    random.seed("icpc")

    if TEST_9:
        test_9()
    