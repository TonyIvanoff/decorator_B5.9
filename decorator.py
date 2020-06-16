import time

def time_this(NUM_RUNS=50):
    def decorator(function):
        def func(*args, **kwargs):
            avg_time = 0
            for _ in range(NUM_RUNS):
                t0 = time.time()
                function(*args, **kwargs)
                t1 = time.time()
                avg_time += (t1 - t0)
            avg_time /= NUM_RUNS
            fn = function.__name__
            print("Average time is %s for %s runs: %.5f " % (fn, NUM_RUNS, avg_time))
        return func

    return decorator