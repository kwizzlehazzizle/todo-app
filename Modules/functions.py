FILE_PATH = 'todos.txt'
""" The File Path """
def get_todos(todosfilepath = FILE_PATH  ):
    """ Opens the file containing the to-do list for reading
    and returns a list of to-do items """
    with open(todosfilepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, todosfilepath = FILE_PATH ):
    """ Opens the file containing the to-do list for writing
       and write to it the list received as a parameter """
    with open(todosfilepath, 'w') as file_local:
        file_local.writelines(todos_arg)

print('**',__name__,'imported')
if __name__ == "__main__" :
    print("Hello!!!!")