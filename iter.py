tuple_ = (1,2,3)

for value in tuple_:
    print(value)
    tuple_ = tuple_ + (len(tuple_) + 1, )
print