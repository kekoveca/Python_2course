test_str = "ab650d"
ls = [ord(el) for el in test_str]
tmp1 = ''.join(str(e) for e in ls)
print(tmp1)