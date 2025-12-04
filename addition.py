def make_upper(function):
    def wrapper(arg1):
        return_value = function(arg1)
        return return_value.upper()
    return wrapper

@make_upper

def get_name(name):
    return name
print(get_name("gopal"))
