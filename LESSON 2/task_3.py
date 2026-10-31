group_a = ["oleg", "ira", "maks"]
group_b = ["anna", "dmytro"]


backup_a = group_a.copy()
print(backup_a)

group_a.extend(group_b)
print(group_a)

print(group_a)