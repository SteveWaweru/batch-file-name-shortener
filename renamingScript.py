__author__ = 'steve_w'
import os


def change_file_name(path_to_file, string_to_remove):
    """
    Function to remove part of name of file in a folder with many files.
    :param path_to_file:
    :param string_to_remove:
    :return:
    """
    # TODO: exception handling for unknown file names, file paths etc
    files = os.listdir(path_to_file)
    change = []
    for f in files:
        if f.startswith(string_to_remove):
            os.rename(path_to_file + f, path_to_file + f[len(string_to_remove):])
            change.append((f, f[len(string_to_remove):]))
    for c in change:
        print(c[0] + " => " + c[1])
    print("files successfully renamed")

# TODO: Option for user to enter input than the current manual way
# TODO: File path to be compatible with all platforms. os.path?

# REMEMBER TO ADD THE SLASH AT THE END OF THE FILE PATH!!!! ie: /path/to/file/
path_to_file = "/home/user/path/to/file/"
string_to_remove = "string to remove"
# Excecute function
change_file_name(path_to_file, string_to_remove)
