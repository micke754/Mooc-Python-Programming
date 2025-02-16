number_of_groups = int(input("How many students on the course? "))

group_size = int(input("Desired group size? "))

groups_formed = (number_of_groups + group_size - 1) // group_size

print(f"Number of groups formed: {groups_formed}")
