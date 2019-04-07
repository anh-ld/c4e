sequence = input("Enter a sequence number, seperated by space: ")

sequence_list = sequence.strip().split() #strip cut space at the beginning/end of string
for i in range(len(sequence_list)):
    sequence_list[i] = int(sequence_list[i])

is_sorted = True
for i in range(len(sequence_list) - 1):
    if sequence_list[i + 1] < sequence_list[i]:
        is_sorted = False
        break

if is_sorted:
    print("Your sequence is sorted.")
else:
    print("Your sequence is not sorted yet.")
    y = []
    while len(sequence_list) != 0:
        y.append(min(sequence_list))
        sequence_list.remove(min(sequence_list))
    print("Here is a sorted list.")
    print(*y)
