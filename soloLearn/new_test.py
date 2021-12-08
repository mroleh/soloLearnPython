from itertools import permutations, combinations

unique_combinations = []

column_list = ['id', 'organization_name', 'contract_id', 'uploaded', 'run_date', 'status']
sort_by = ['asc', 'desc']
comb = combinations(column_list, len(sort_by))

print(column_list)
print(sort_by)

for comb in comb:
    zipped = zip(comb, sort_by)
    unique_combinations.append(list(zipped))

print(unique_combinations)
