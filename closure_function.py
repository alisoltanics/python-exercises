def print_msg(msg):
    # This is the outer enclosing function

    def printer():
        # This is the nested function
        print(msg)

    return printer  # returns the nested function


# Now let's try calling this function.
# Output: Hello
another = print_msg("Hello")
another()

Output:
Hello


"""
The print_msg() function was called with the string "Hello" and the returned function was bound to the name another. On calling another(), the message was still remembered although we had already finished executing the print_msg() function.

This technique by which some data ("Hello in this case) gets attached to the code is called closure in Python.

https://www.programiz.com/python-programming/closure#:~:text=Defining%20a%20Closure%20Function&text=This%20technique%20by%20which%20some,removed%20from%20the%20current%20namespace.
"""