# fibonacci.py

def fib():
    fibs = [1, 2]

    for i in range(1,9):

        new_num = fibs[i-1]+fibs[i]
        fibs.append(new_num)
    return fibs

def main():
    print('OUTPUT', fib())

if __name__ == "__main__":
    main()
