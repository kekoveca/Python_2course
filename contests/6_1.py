with open(input(), 'r') as f:
    print(max(f.read().split(), key= len))