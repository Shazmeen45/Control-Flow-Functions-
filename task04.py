global_variable = "I am a global variable"


def show_variables():
    local_variable = "I am a local variable"

    print("Inside function:")
    print("Global variable:", global_variable)
    print("Local variable:", local_variable)


show_variables()

print("Outside function:")
print("Global variable:", global_variable)