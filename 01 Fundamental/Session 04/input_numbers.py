sequence = input("Enter a sequence number, seperated by space: ")

sequence_list = sequence.split(" ")
for i in range(len(sequence_list)):
    sequence_list[i] = int(sequence_list[i])
print(sequence_list)
