def star_pattern(n):
    for i in range(i, n+1):   # rows (reverse)
        for j in range(i, n+1):# columns
            if j<i:
                print("__", end="  ")
            else:
                print("* ", end=" ")
        print()

def main():
    n = int(input("Enter number: "))
    star_pattern(n)

main()
