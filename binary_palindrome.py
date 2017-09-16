if __name__ == "__main__":
    x,orig = 5,5
    rev = 0
    while x:
        temp = x & 1
        x >>= 1
        rev <<= 1
        rev = rev | temp

    print rev
