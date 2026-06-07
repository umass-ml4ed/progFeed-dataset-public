def max_recursive(lst):
    if not lst:
        return 0
    if len(lst) == 1:
        return lst[0]
    head = lst[0]
    tail_max = max_recursive(lst[1:])
    return head if head > tail_max else tail_max

def sum_lists_recursive(lst1, lst2):
    if not lst1:
        return 0
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])

def funky(n):
    if n == 0 or n == 1:
        return 1
    if n % 2 == 0:
        return 2 * funky(n // 2)
    return 1 + 2 * funky(n + 1)

def permutations(lis):
    if len(lis) == 1:
        return [lis[:]]
    retlis = []
    for i in range(len(lis)):
        front_item = lis[i]
        remaining = lis[:i] + lis[i+1:]
        for perm in permutations(remaining):
            retlis.append([front_item] + perm)
    return retlis

if __name__ == "__main__":
    print("max_recursive([3, 10, 2, 8, 6]) ->", max_recursive([3, 10, 2, 8, 6]))
    print("max_recursive([6]) ->", max_recursive([6]))
    print("max_recursive([]) ->", max_recursive([]))
    print("sum_lists_recursive([1,2,3],[4,5,6]) ->", sum_lists_recursive([1,2,3],[4,5,6]))
    print("sum_lists_recursive([],[]) ->", sum_lists_recursive([], []))
    print("funky(2), funky(10), funky(50), funky(-10), funky(-50) ->",
          funky(2), funky(10), funky(50), funky(-10), funky(-50))
    print("permutations(['AA','BB','CC']) ->", permutations(['AA','BB','CC']))
