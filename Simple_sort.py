#it's my first sort algorithm

def my_sort(l:list, reverse=False):
    for i in range(len(l)):
        max_index = i
        for a in range(i, len(l)):
            if l[a] > l[max_index]:
                max_index = a
        l[i], l[max_index] = l[max_index], l[i]
    
    if reverse:
        return l[::-1]
    return l


def main():
    l = list(map(int, input().split()))
    print(my_sort(l))


if __name__ == '__main__':
    main()

