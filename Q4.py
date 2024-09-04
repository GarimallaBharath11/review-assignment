import cProfile
import itertools
from io import StringIO
import pstats

def compute_combinations_permutations():
    # Define the list
    my_list = [1, 2, 3]

    # Compute combinations
    print("Combinations of my_list with length 2:")
    comb_2 = list(itertools.combinations(my_list, 2))
    print(comb_2)

    print("\nCombinations of my_list with length 3:")
    comb_3 = list(itertools.combinations(my_list, 3))
    print(comb_3)

    # Compute permutations
    print("\nPermutations of my_list with length 2:")
    perm_2 = list(itertools.permutations(my_list, 2))
    print(perm_2)

    print("\nPermutations of my_list with length 3:")
    perm_3 = list(itertools.permutations(my_list, 3))
    print(perm_3)

def profile_code():
    pr = cProfile.Profile()
    pr.enable()
    
    # Run combination and permutation calculations
    compute_combinations_permutations()
    
    pr.disable()
    s = StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print("\nProfiling Results:")
    print(s.getvalue())

if __name__ == "__main__":
    profile_code()
