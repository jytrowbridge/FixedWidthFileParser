import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import helper_functions as hf
import parse_fw_file as pf
import config as conf

class ParseFw:

    def __init__(self, master):
        self.master = master
        master.title("Jack's Fixed Width File Parser")

        # icon
        #self.master.iconbitmap(r'C:/Users/jack.trowbridge/Documents/Allied/parseFileGui/straw_hat.ico')
        #self.master.iconbitmap(r'C:/Users/jack.trowbridge/Documents/Allied/parseFileGui/jack.ico')
        icon_file_path = conf.ico_dir + "jack.ico"
        self.master.iconbitmap(icon_file_path)

        # create notebook for tabbing
        self.master_note = ttk.Notebook(self.master)

        # load configurations
        self.parser_conf(self.master_note)
        self.edit_conf(self.master_note)

        self.master_note.add(self.master_parser_frame, text = 'Parse File')
        self.master_note.add(self.master_edit_frame, text = "Edit File", compound=tk.TOP)
        self.master_note.pack()

    ##############
    # METHODS
    ############

    def edit_conf(self, parent):
        '''
        Tkinter configuration for the edit tab
        '''
        self.master_edit_frame = tk.Frame(parent)

        tk.Button(self.master_edit_frame, text='Exit', command=self.master.destroy).pack(padx=100, pady=100)
###########
        #----------
        # WIDGETS & FRAMES
        #----------
        # Configure frames
        self.master_edit_frame = tk.Frame(parent, relief=tk.SUNKEN,bd=2, padx=10, pady=10)#, bg='red')
        self.option_frame = tk.Frame(self.master_edit_frame, bd=2, padx=5, pady=5)#, bg='green')
        self.run_frame = tk.Frame(self.master_edit_frame, bd=2, padx=5, pady=5)#, bg='blue')
        self.log_frame = tk.Frame(self.master_edit_frame, relief=tk.SUNKEN, bd=2, padx=5, pady=5, bg='white')

        # Select file row
        self.f_in_label = tk.Label(self.option_frame, text = "Select File:")
        self.f_in = tk.StringVar()
        self.f_in.set("")
        self.f_in_box = tk.Entry(self.option_frame, width=50,textvariable=self.f_in)
        self.f_in_button = tk.Button(self.option_frame, text="Browse", command=self.get_filename)

        # Output file row
        self.f_out_label = tk.Label(self.option_frame, text = "Output File:")
        self.f_out = tk.StringVar()
        self.f_out.set("")
        self.f_out_box = tk.Entry(self.option_frame, width=50,textvariable=self.f_out)
        self.f_out_button = tk.Button(self.option_frame, text="Browse", command=self.set_out_file)

        # File widths row
        self.f_widths_label = tk.Label(self.option_frame, text = "File Widths:")
        self.widths = tk.StringVar()
        self.widths.set("")
        self.f_widths_box = tk.Entry(self.option_frame,width=50,textvariable=self.widths)

        # Run button
        self.run_btn = tk.Button(self.run_frame, text="Parse File", command=self.parse_file)

        # Log box:
        self.log_message = tk.StringVar()
        self.log_message.set("Parse a file!")
        self.log_box = tk.Label(self.log_frame, width=62, height=5, anchor=tk.NW, justify=tk.LEFT, textvariable=self.log_message, bg='white', wraplength=430)

        #------------
        # GRID SHIT
        #------------
        # widgets
        self.f_in_label.grid(row=0, column=0)
        self.f_in_box.grid(row=0, column=1, padx = 5)
        self.f_in_button.grid(row=0, column=2, padx = 5)

        self.f_out_label.grid(row=1, column=0)
        self.f_out_box.grid(row=1, column=1)
        self.f_out_button.grid(row=1, column=2)

        self.f_widths_label.grid(row=2, column=0)
        self.f_widths_box.grid(row=2, column=1)

        self.run_btn.pack()
        self.log_box.pack()

        # frames
        self.master_edit_frame.grid()
        self.option_frame.grid(row=0, column=1)
        self.run_frame.grid(row=1,column=1)
        self.log_frame.grid(row=2,column=1)

    def parser_conf(self, parent):
        '''
        Tkinter configuration for the parser tab
        '''
        #----------
        # WIDGETS & FRAMES
        #----------
        # Configure frames
        self.master_parser_frame = tk.Frame(parent, relief=tk.SUNKEN,bd=2, padx=10, pady=10)#, bg='red')
        self.option_frame = tk.Frame(self.master_parser_frame, bd=2, padx=5, pady=5)#, bg='green')
        self.run_frame = tk.Frame(self.master_parser_frame, bd=2, padx=5, pady=5)#, bg='blue')
        self.log_frame = tk.Frame(self.master_parser_frame, relief=tk.SUNKEN, bd=2, padx=5, pady=5, bg='white')

        # Select file row
        self.f_in_label = tk.Label(self.option_frame, text = "Select File:")
        self.f_in = tk.StringVar()
        self.f_in.set("")
        self.f_in_box = tk.Entry(self.option_frame, width=50,textvariable=self.f_in)
        self.f_in_button = tk.Button(self.option_frame, text="Browse", command=self.get_filename)

        # Output file row
        self.f_out_label = tk.Label(self.option_frame, text = "Output File:")
        self.f_out = tk.StringVar()
        self.f_out.set("")
        self.f_out_box = tk.Entry(self.option_frame, width=50,textvariable=self.f_out)
        self.f_out_button = tk.Button(self.option_frame, text="Browse", command=self.set_out_file)

        # File widths row
        self.f_widths_label = tk.Label(self.option_frame, text = "File Widths:")
        self.widths = tk.StringVar()
        self.widths.set("")
        self.f_widths_box = tk.Entry(self.option_frame,width=50,textvariable=self.widths)

        # Run button
        self.run_btn = tk.Button(self.run_frame, text="Parse File", command=self.parse_file)

        # Log box:
        self.log_message = tk.StringVar()
        self.log_message.set("Parse a file!")
        self.log_box = tk.Label(self.log_frame, width=62, height=5, anchor=tk.NW, justify=tk.LEFT, textvariable=self.log_message, bg='white', wraplength=430)

        #------------
        # GRID SHIT
        #------------
        # widgets
        self.f_in_label.grid(row=0, column=0)
        self.f_in_box.grid(row=0, column=1, padx = 5)
        self.f_in_button.grid(row=0, column=2, padx = 5)

        self.f_out_label.grid(row=1, column=0)
        self.f_out_box.grid(row=1, column=1)
        self.f_out_button.grid(row=1, column=2)

        self.f_widths_label.grid(row=2, column=0)
        self.f_widths_box.grid(row=2, column=1)

        self.run_btn.pack()
        self.log_box.pack()

        # frames
        self.master_parser_frame.grid()
        self.option_frame.grid(row=0, column=1)
        self.run_frame.grid(row=1,column=1)
        self.log_frame.grid(row=2,column=1)

    def print_exception(self, message):
        '''
        Sets log message to given message and font as red
        '''
        self.log_message.set(message)
        self.log_box.config(fg='red')

    def parse_file(self):
        '''
        Parses given file using given source, target, and widths
        '''
        message = ""

        # verify arguments:
        try:
            if not self.verify_args(): return
        except Exception as e:
            message = "Error validating arguemnts: " + str(e)
            self.print_exception(message)
            return

        # parse file:
        try:
            parse_result = pf.parse_fw_file(self.f_in.get(), self.f_out.get(), self.widths.get()) # returns tuple [result: boolean, message: str]
            if parse_result[0]:
                self.log_message.set("Parsed file successfully!")
                self.log_box.config(fg='green')
            else:
                self.print_exception(parse_result[1] + "\nParsed file successfully!")
                self.log_box.config(fg='blue')
        except Exception as e:
            message = "Error parsing file: " + str(e)
            self.print_exception(message)

    def verify_args(self):
        '''
        Verifies source file, target file, and widths.
        Files must have valid paths and widths must be string of comma-separated integers
        '''
        out_message, out = "", True

        # verify source file
        if self.f_in.get() =='':
            out_message += "Please enter source file path\n"
            out = False
        else:
            if not hf.verify_file(self.f_in.get(), exists=True):
                out = False
                out_message += "Source file doesn't exist or isn't writeable\n"

        # verify target file
        if self.f_out.get() =='':
            out_message +="Please enter target file path\n"
            out = False
        else:
            if not hf.verify_file(self.f_out.get(), exists=False):
                out = False
                out_message += "Target file directory does not exist\n"

        # verify widths
        if self.widths.get() =='':
            out_message += "Please enter file widths\n"
            out = False
        else:
            if not hf.verify_widths(self.widths.get()):
                out = False
                out_message += "Invalid widths; please supply string of comma-separated integers\n"

        if not out:
            self.log_message.set(out_message)
            self.log_box.config(fg='red')
        return out

    def get_filename(self):
        '''
        Set source file and target file parameters automatically
        '''
        try:
            self.f_in.set(fd.askopenfilename(title="Select File")) # get and set in file
            self.f_out.set(hf.get_out_fname(self.f_in.get())) # automatically set out file
        except Exception as e:
            message = "Error getting source file name: " + str(e)
            self.print_exception(message)

    def set_out_file(self):
        '''
        Set target file parameter
        '''
        try:
            self.f_out.set(fd.asksaveasfilename(title="Save As"))
        except Exception as e:
            message = "Error getting target file name: " + str(e)
            self.print_exception(message)

def main():
    root = tk.Tk()
    gui = ParseFw(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    # add radio buttons for single line
    # add logging :(
