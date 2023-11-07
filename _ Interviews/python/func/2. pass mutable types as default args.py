def fail_func(val: int, s=set()) -> None:
    print(hex(id(s)))
    s.add(val)
    print(s)


fail_func(1)
fail_func(2)
fail_func(3)

# 0x7f99b811f660
# {1}
# 0x7f99b811f660
# {1, 2}
# 0x7f99b811f660
# {1, 2, 3}
