import re
import os

def get_out_fname(path):
    # given full path of file, return the directory
    out = re.sub(r'.txt', r'_parsed.csv',  path, flags=re.I)

    # if parsing failed, return directory name only:
    if out[out.rfind('.') + 1: ] != 'csv':
        out = out[ : out.rfind('/') + 1]

    return out

def verify_file(file_path, exists=False):
    # returns true if file has a valid path
    # If exists is true, returns false if file doesn't exist
    if not os.path.exists(file_path) and exists:
        #the file is there
        return False
    elif not os.path.exists(get_path_dir(file_path)):
        return False
    #elif os.access(os.path.dirname(file_path), os.W_OK):
        #the file does not exists but write privileges are given
    else:
        return True

def get_path_dir(path):
    return path[ : path.rfind('/')]

def verify_widths(widths):
    # returns fales if given widths is not a string of comma-separated integers
    widths_list = widths.split(",")
    for width in widths_list:
        try:
            int_width = int(width)
        except ValueError:
            return False
    return True

def print_exception(tk_obj, message):
    '''
    Sets log message to given message and font as red
    '''
    tk_obj.log_message.set(message)
    tk_obj.log_box.config(fg='red')


if __name__ == "__main__":
    path = 'C:/Users/jack.trowbridge/Documents/Allied/2910/nothere.666'
    verify_file(path)

    verify_widths('1,2')
