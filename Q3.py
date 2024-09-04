import cProfile
import itertools
from io import StringIO
import pstats

def compute_combinations_permutations():
    # Define lists
    A = [1, 2, 3]
    B = [4, 5]
    C = [6, 7]
    D = [8, 9]
    E = [10]

    # Compute all combinations
    print("Combinations of A with length 2:")
    comb_A = list(itertools.combinations(A, 2))
    print(comb_A)

    print("\nCombinations of B with length 2:")
    comb_B = list(itertools.combinations(B, 2))
    print(comb_B)

    print("\nCombinations of A, B with length 2:")
    comb_AB = list(itertools.combinations(A + B, 2))
    print(comb_AB)

    # Compute all permutations
    print("\nPermutations of A with length 2:")
    perm_A = list(itertools.permutations(A, 2))
    print(perm_A)

    print("\nPermutations of B with length 2:")
    perm_B = list(itertools.permutations(B, 2))
    print(perm_B)

    print("\nPermutations of A, B with length 2:")
    perm_AB = list(itertools.permutations(A + B, 2))
    print(perm_AB)

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
