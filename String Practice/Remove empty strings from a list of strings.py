str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
print("Original String is :",str_list)
new_str_list = list(filter(None, str_list))

print("After removing empty strings")
print(new_str_list)