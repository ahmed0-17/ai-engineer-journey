import time

start = time.perf_counter()


for i in range(1,101):
    print (i)

end = time.perf_counter()

print(f"Time taken: {end - start:.2f} seconds")