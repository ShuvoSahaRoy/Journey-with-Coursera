# The parent_directory function returns the name of the directory that's
# located just above the current working directory. Remember that '..' is a relative
# path alias that means "go up to the parent directory". Fill in the gaps to complete this function.
import os.path
def parent_directory():
    return os.path.abspath(os.path.join(os.getcwd(), os.pardir))

print(parent_directory())

