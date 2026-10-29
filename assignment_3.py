def replace_value(values,index,new_value):
  values[index] = new_value
def find_first(values,target):
  for i in range(len(values)):
    if values[i] == target:
      return i
  return -1
def summarize(values):
  minimum = min(values)
  maximum=max(values)
  summary=sum(values)
  guli=(minimum,maximum,summary)
  return guli
a=int(input("Enter the number of days: "))
original = []
for i in range(a):
  b=int(input("Enter data use in megabytes: "))
  original.append(b)
updated = original[:]
index = int(input("Enter the index to correct: "))
new_value = int(input('Enter the new data use: '))
target = int(input('Enter the data use to search for: '))
replace_value(updated, index, new_value)
variable = find_first(updated, target)
r = updated.count(target)
guli = summarize(updated)
minimum, maximum, summary = guli
random = sorted(updated)
print(f'Original: {original}')
print(f'Updated: {updated}')
print(f'Sorted: {random}')
print(f'Minimum data use: {minimum} MB')
print(f'Maximum data use: {maximum} MB')
print(f'Total data use: {summary} MB')
print(f'First matching index: {variable}')
print(f'Matching values: {r}')
