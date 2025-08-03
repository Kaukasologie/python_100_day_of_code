import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

print()
# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    print(f"key: {key}, value: {value}\n")

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame, "\n")

# Loop through rows of a pandas data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    print(f"index: {index}, row: {row}\n")
    # Access row.student or row.score
    print(f"student: {row.student}, score: {row.score}\n")

# Keyword Method with iterrows()
"Sample: {new_key:new_value for (index, row) in df.iterrows()}"
new_format_student_dictionary = {row.student:row.score for (index, row) in student_data_frame.iterrows()}
print(f"New format:\n{new_format_student_dictionary}")
