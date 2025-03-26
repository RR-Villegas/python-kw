def check_values(x, y):
    """
    Demonstrates the 'and' and 'else' keywords.

    Args:
        x: The first value to check.
        y: The second value to check.

    Returns:
        True if both x and y are True, False otherwise.
    """
    if x and y:  # 'and' keyword: Logical AND operation
        return True
    else:  # 'else' keyword:  Alternative block of code
        return False

def handle_error(value):
    """
    Demonstrates the 'assert', 'try', 'except', and 'as' keywords.

    Args:
        value: The value to check for positivity.

    Returns:
        The value if it's positive, None otherwise.  Prints an error message if the assertion fails.
    """
    try:  # 'try' keyword:  Block of code where exceptions might occur
        assert value > 0, "Value must be positive"  # 'assert' keyword: Checks if a condition is true
        return value
    except AssertionError as e:  # 'except' keyword: Handles a specific exception (AssertionError)
        # 'as' keyword:  Assigns the exception object to the variable 'e'
        print(f"Error: {e}")
        return None

def process_list(data):
    """
    Demonstrates the 'for', 'in', 'continue', 'break', and 'yield' keywords.

    Args:
        data: A list of numbers.

    Yields:
        Numbers from the list that are greater than 0 and less than or equal to 5.
    """
    for item in data:  # 'for' keyword:  Iterates through the 'data' list
        if item == 0:
            continue  # 'continue' keyword: Skips the rest of the current iteration
        elif item > 5:
            break  # 'break' keyword: Exits the loop
        else:
            yield item  # 'yield' keyword:  Returns a generator object

class MyClass:
    """
    Demonstrates the 'class' keyword.

    Defines a simple class with a constructor and a method.
    """
    class_variable = True # Class variable

    def __init__(self, value):
        """
        Constructor of the class.

        Args:
            value: The initial value of the object.
        """
        self.value = value  # Instance variable

    def get_value(self):
        """
        Returns the value of the object.

        Returns:
            The value of the object.
        """
        return self.value

def modify_global():
    """
    Demonstrates the 'global' keyword.

    Modifies the value of a global variable.
    """
    global global_var  # 'global' keyword:  Declares that 'global_var' is a global variable
    global_var = 20

global_var = 10  # Define a global variable

def modify_nonlocal():
    """
    Demonstrates the 'nonlocal' keyword.

    Modifies a variable in an enclosing function's scope.

    Returns:
        The modified value of the nonlocal variable.
    """
    outer_var = 5

    def inner_function():
        nonlocal outer_var  # 'nonlocal' keyword: Declares 'outer_var' is from an enclosing scope
        outer_var = 15

    inner_function()
    return outer_var

def create_lambda(n):
    """
    Demonstrates the 'lambda' keyword.

    Creates an anonymous function (lambda function).

    Args:
        n: The number to multiply with.

    Returns:
        A lambda function that multiplies its argument by n.
    """
    return lambda x: x * n  # 'lambda' keyword: Creates an anonymous function

def handle_with(filename):
    """
    Demonstrates the 'with' keyword.

    Opens a file, writes to it, and ensures it's closed properly using a context manager.

    Args:
        filename: The name of the file to open.

    Returns:
        True if the file operation was successful, False otherwise.
    """
    try:
        with open(filename, 'w') as f:  # 'with' keyword:  Creates a context manager for file handling
            f.write("Test data")
        return True
    except FileNotFoundError:
        return False
    finally:  # 'finally' keyword:  Block of code that always executes
        print("File operation attempted.")

def use_del(my_dict):
    """
    Demonstrates the 'del' keyword.
    Deletes an item from a dictionary

    Args:
        my_dict: The dictionary

    Returns:
       The dictionary after deletion
    """
    try:
        del my_dict["key1"] # 'del' keyword: Delete item from dictionary
        return my_dict
    except KeyError:
        return None

def use_raise():
  """
  Demonstrates the 'raise' keyword.
  Raises a ValueError exception.
  """
  raise ValueError("This is a raised error.") # 'raise' keyword: Raise an exception

def use_pass():
  """
  Demonstrates the 'pass' keyword.
  Does nothing.  Placeholder.
  """
  pass # 'pass' keyword: Does nothing

def use_import():
  """
  Demonstrates the 'import' keyword.
  Imports the math module.
  """
  import math # 'import' keyword: Import a module
  return math.sqrt(16)

def use_from():
  """
  Demonstrates the 'from' keyword.
  Imports pi from the math module
  """
  from math import pi # 'from' keyword: Import specific item from a module
  return pi

def use_is(a, b):
    """
    Demonstrates the 'is' keyword.

    Checks if two variables refer to the same object.

    Args:
        a: The first variable.
        b: The second variable.

    Returns:
        True if a and b refer to the same object, False otherwise.
    """
    return a is b  # 'is' keyword:  Checks for object identity

def use_in(a, b):
    """
    Demonstrates the 'in' keyword.
    Checks if a value is present in a sequence.

    Args:
        a: The value to check.
        b: The sequence (e.g., list, string).

    Returns:
        True if a is in b, False otherwise.
    """
    return a in b # 'in' keyword: Check for membership

def use_none():
    """
    Demonstrates the 'None' keyword.
    Returns the None object.
    """
    return None # 'None' keyword: Represents null value

def use_try_except_else(a):
    """
    Demonstrates 'try', 'except', and 'else'

    Args:
      a: A number.

    Returns:
      Result of 10/a, "Division by zero" if a is zero.
    """
    try:
        result = 10/a
    except ZeroDivisionError:
        return "Division by zero"
    else: # 'else' keyword: only executed if no exception
        return result

def use_not(a):
  """
  Demonstrates 'not'

  Args:
    a: boolean

  Returns:
    Negation of a
  """
  return not a # 'not' keyword: negation

def use_or(a, b):
  """
  Demonstrates 'or'

  Args:
    a: boolean
    b: boolean

  Returns:
    a or b
  """
  return a or b # 'or' keyword: logical or

def use_while(a):
  """
  Demonstrates 'while'

  Args:
    a: number

  Returns:
    a after incrementing until it is 5
  """
  while a < 5: # 'while' keyword: loop
    a+=1
  return a

def use_return():
  """
  Demonstrates 'return'
  Returns True
  """
  return True # 'return' keyword: return a value

def use_false():
  """
  Demonstrates 'False'
  Returns False
  """
  return False # 'False' keyword: boolean false

def use_true():
  """
  Demonstrates 'True'
  Returns True
  """
  return True # 'True' keyword: boolean true

def use_elif(a):
  """
  Demonstrates 'elif'

  Args:
    a: number

  Returns:
    string describing where a is in relation to 5 and 10
  """
  if a > 10: # 'if' keyword: first condition
    return "Greater than 10"
  elif a > 5: # 'elif' keyword: alternative condition
    return "Greater than 5"
  else:
    return "Less than or equal to 5"

def use_def():
  """
  Demonstrates 'def'
  Defines a function and calls it
  """
  def my_function(): # 'def' keyword: function definition
    return "Hello"
  return my_function()

def use_class():
  """
  Demonstrates 'class'
  Defines a class and returns an instance of it
  """
  class MyClass2: # 'class' keyword: class definition
    pass
  return MyClass2()

# The following section executes the functions and prints the results to demonstrate the keywords in action.
print(check_values(True, True))
print(handle_error(5))
print(list(process_list([1, 2, 3, 6, 4])))
my_instance = MyClass(20)
print(my_instance.get_value())
modify_global()
print(global_var)
print(modify_nonlocal())
double = create_lambda(2)
print(double(5))
print(handle_with("test.txt"))
print(use_del({"key1":1, "key2":2}))
try:
  use_raise()
except ValueError as e:
  print(e)
use_pass()
print(use_import())
print(use_from())
print(use_is(5,5))
print(use_in(2,[1,2,3]))
print(use_none())
print(use_try_except_else(0))
print(use_try_except_else(2))
print(use_not(False))
print(use_or(True, False))
print(use_while(0))
print(use_return())
print(use_false())
print(use_true())
print(use_elif(6))
print(use_def())
print(use_class())
