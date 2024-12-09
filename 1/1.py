from collections import Counter

def solve_query_1(l: list, r: list):
    result = 0

    for i in range(len(l)):
        result += abs(l[i] - r[i])
    
    return result

def solve_query_2(l: list, r: list):
    result = 0
    r_counter = Counter(r)

    for i in range(len(l)):
        result += l[i] * r_counter[l[i]]
    
    return result

def run_all(filename: str):
    l, r = [], []
    with open(filename) as inp:
        for x in inp.readlines():
            a, b = map(int, x.split())
            l.append(a)
            r.append(b)             

    l.sort()
    r.sort()

    print("RESULT 1: ", solve_query_1(l,r))
    print("RESULT 2: ", solve_query_2(l,r))

if __name__ == "__main__":
    run_all("1_input_test.txt")
    run_all("1_input.txt")
