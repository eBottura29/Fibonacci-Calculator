import time
import sys


def fibonacci(max_time):
    numbers = [0, 1]

    start = time.time()

    i = 0

    while time.time() - start < max_time:
        try:
            num = numbers[i] + numbers[i + 1]
            numbers.append(num)
            i += 1
        except OverflowError:
            return numbers, time.time() - start
        except MemoryError:
            return numbers, time.time() - start
        except KeyboardInterrupt:
            return numbers, time.time() - start

    return numbers, time.time() - start


if __name__ == "__main__":
    sys.set_int_max_str_digits(2147483647)  # max number possible (32 bits: 2^31-1)
    time_to_calculate = 10000
    fib_list, time_taken = fibonacci(time_to_calculate)

    print(fib_list[-1])
    print(f"Calculated {len(fib_list)} fibonacci numbers.")
    print(f"Largest number calculated has a length of {len(str(fib_list[-1]))} digits.")
    print(f"Took {time_taken:.2f} seconds.")
    print(f"Aimed for {time_to_calculate} seconds.")
    print("Saving to file...")

    with open("largest_num.txt", "w") as f:
        f.write(str(fib_list[-1]))

    sys.exit("Done saving to file.")
