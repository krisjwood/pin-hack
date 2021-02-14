# Script that demostrates how quickly a PIN can be hacked with brute force

# Start
def start_test():
    import time
    start = time.time()
    return start

# End
def end_test(start):
    import time
    end = time.time()

    # Summary
    print(f"Start: {time.ctime(start)}")
    print(f"End: {time.ctime(end)}")

    execution = end - start
    rounded = round(execution, 4)
    print(f"Execution time: {rounded} seconds")

# Operation
start = start_test()
range_num = 10000
[print(i) for i in range(range_num)]
end_test(start)