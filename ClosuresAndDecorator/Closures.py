
def outer_func(message):
    outher_message = "Outer: " + message

    def Inner_func():
        print(outher_message)
    return Inner_func()


outer_func("Hello world")

