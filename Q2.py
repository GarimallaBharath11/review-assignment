import cProfile
import numpy as np
from io import StringIO
import pstats

def perform_operations():
    # I. Create a list
    my_list = [1225, 4986, 6789, 7890, 2345, 6783, 987, 1234, 8765, 3456]

    # II. Iterate using a for loop
    print("Iterating using a for loop:")
    for item in my_list:
        print(item)

    # III. Iterate using for loop and range
    print("\nIterating using a for loop and range:")
    for i in range(len(my_list)):
        print(my_list[i])

    # IV. List comprehension
    print("\nList comprehension to create a new list with values doubled:")
    doubled_list = [x * 2 for x in my_list]
    print(doubled_list)

    # V. Enumerate
    print("\nUsing enumerate to get index and value:")
    for index, value in enumerate(my_list):
        print(f"Index {index}: Value {value}")

    # VI. Iter function and next function
    print("\nUsing iter and next functions:")
    list_iter = iter(my_list)
    for _ in range(len(my_list)):
        print(next(list_iter))

    # VII. Map function
    print("\nUsing map to create a new list with values squared:")
    squared_list = list(map(lambda x: x ** 2, my_list))
    print(squared_list)

    # VIII. Using zip
    print("\nUsing zip to combine lists:")
    another_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    zipped_list = list(zip(my_list, another_list))
    print(zipped_list)

    # IX. Using NumPy module
    np_array = np.array(my_list)
    print("\nUsing NumPy:")
    print("Original array:")
    print(np_array)

    doubled_np_array = np_array * 2
    print("\nDoubled array:")
    print(doubled_np_array)

    squared_np_array = np_array ** 2
    print("\nSquared array:")
    print(squared_np_array)

def profile_code():
    pr = cProfile.Profile()
    pr.enable()
    
    perform_operations()
    
    pr.disable()
    s = StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print("\nProfiling Results:")
    print(s.getvalue())

if __name__ == "__main__":
    profile_code()
