set_a=set()
set_b=set()

set_a_size=int(input("Enter the size of the set a\n"))
for i in range(set_a_size):
    set_a.add(int(input(f"Enter the {i}th element\n")))

set_b_size=int(input("Enter the size of the set b\n"))
for i in range(set_b_size):
    set_b.add(int(input(f"Enter the {i}the element\n")))

print("set a:",set_a)
print("set b:",set_b)

union_of_sets=set_a.union(set_b)
intersection_of_sets=set_a.intersection(set_b)
difference_of_sets=set_a.difference(set_b)


print(f"the uniof of the sets:{union_of_sets}")
print(f"the intersection of the sets:{intersection_of_sets}")
print(f"The difference of the sets:{difference_of_sets}")
