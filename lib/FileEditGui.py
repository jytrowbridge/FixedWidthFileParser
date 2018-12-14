import tkinter as tk
import helper_functions as hf
import parse_fw_file as pf
import parse_single_line_fw as slpf
import field_value as fv
from tkinter import filedialog as fd

class FileEditGui:

    def __init__(self, parent, out=False):
        '''
        Instances have a Tkinter frame hierarchy consisting of:
            master_frame: top-level frame holding all other frames
            option_frame: holds file in box, widths box, and if out, out file box
            run_frame: empty frame in which the run button and other objects will go
            log_frame: frame holding the log box
        option_frame elements are gridded
        run_frame elements are not
        '''
        self.out = out
        #----------
        # WIDGETS & FRAMES
        #----------
        # Configure frames
        self.master_frame = tk.Frame(parent, relief=tk.SUNKEN,bd=2, padx=10, pady=10)#, bg='red')
        self.option_frame = tk.Frame(self.master_frame, bd=2, padx=5, pady=5)#, bg='green')
        self.run_frame = tk.Frame(self.master_frame, bd=2, padx=5, pady=5)#, bg='blue')
        self.log_frame = tk.Frame(self.master_frame, relief=tk.SUNKEN, bd=2, padx=5, pady=5, bg='white')

        # Select file row
        self.f_in_label = tk.Label(self.option_frame, text = "Select File:")
        self.f_in = tk.StringVar()
        self.f_in.set("")
        self.f_in_box = tk.Entry(self.option_frame, width=50,textvariable=self.f_in)
        self.f_in_button = tk.Button(self.option_frame, text="Browse", command=self.get_filename)

        # Output file row if flag is True
        if self.out:
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
        self.f_widths_button = tk.Button(self.option_frame, text="Browse", command=self.set_widths)


        # Log box:
        self.log_message = tk.StringVar()
        #self.log_message.set("Parse a file!")
        self.log_box = tk.Label(self.log_frame, width=62, height=5, anchor=tk.NW, justify=tk.LEFT, textvariable=self.log_message, bg='white', wraplength=430)

        #------------
        # GRID SHIT
        #------------
        # widgets
        self.f_in_label.grid(row=0, column=0)#, pady=3)
        self.f_in_box.grid(row=0, column=1, padx = 5)
        self.f_in_button.grid(row=0, column=2, padx = 5)

        if out:
            self.f_out_label.grid(row=1, column=0,pady=5)
            self.f_out_box.grid(row=1, column=1)
            self.f_out_button.grid(row=1, column=2)

            self.f_widths_label.grid(row=2, column=0)#,pady=3)
            self.f_widths_box.grid(row=2, column=1)
            self.f_widths_button.grid(row=2, column=2)
        else:
            self.f_widths_label.grid(row=1, column=0)#,pady=3)
            self.f_widths_box.grid(row=1, column=1)
            self.f_widths_button.grid(row=1, column=2)

        #self.run_btn.pack()
        self.log_box.pack()

        # frames
        self.master_frame.grid()
        self.option_frame.grid(row=0, column=1)
        #self.run_frame.grid(row=1,column=1)
        self.log_frame.grid(row=2,column=1)

    def get_filename(self):
        '''
        Set source file and target file parameters automatically
        '''
        try:
            self.f_in.set(fd.askopenfilename(title="Select File")) # get and set in file
            if self.out: self.f_out.set(hf.get_out_fname(self.f_in.get())) # automatically set out file
        except Exception as e:
            message = "Error getting source file name: " + str(e)
            hf.print_exception(self, message)

    def set_out_file(self):
        '''
        Set target file parameter
        '''
        try:
            self.f_out.set(fd.asksaveasfilename(title="Save As"))
        except Exception as e:
            message = "Error getting target file name: " + str(e)
            hf.print_exception(self, message)

    def set_widths(self):
        '''
        Set source file and target file parameters automatically
        '''
        try:
            with open(fd.askopenfilename(title="Select File") , 'r') as f:
                widths = f.readline().strip()
                print(widths)
                if hf.verify_widths(widths):
                    self.widths.set(widths)
                    self.log_message.set('Widths set from file')
                    self.log_box.config(fg='green')
                else:
                    self.log_message.set('Error reading widths file. Please make sure widths are on a single line and are comma-separated')
                    self.log_box.config(fg='red')
        except Exception as e:
            message = "Error reading widths file: " + str(e)
            hf.print_exception(self, message)

    def parse_file(self):
        '''
        Parses given file using given source, target, and widths
        '''
        message = ""

        # verify arguments:
        try:
            if not self.verify_args(): return
        except Exception as e:
            message = "Error validating arguments: " + str(e)
            hf.print_exception(self, message)
            return

        # parse file:
        try:
            if self.type.get() == 'MULTI':
                print("ran multi")
                parse_result = pf.parse_fw_file(self.f_in.get(), self.f_out.get(), self.widths.get()) # returns tuple [result: boolean, message: str]
            else:
                print("ran single")
                parse_result = slpf.parse_single_line_fw_file(self.f_in.get(), self.f_out.get(), self.widths.get()) # returns tuple [result: boolean, message: str]
                #print("success")
            if parse_result[0]:
                self.log_message.set("Parsed file successfully!")
                self.log_box.config(fg='green')
            else:
                message = parse_result[1] + "\nParsed file successfully!"
                hf.print_exception(self, message)
                self.log_box.config(fg='blue')
        except Exception as e:
            message = "Error parsing file: " + str(e)
            hf.print_exception(self, message)

    def verify_args(self):
        '''
        Verifies source file, widths, and target file if out=True
        Files must have valid paths and widths must be string of comma-separated integers
        '''

        # will need to add out file as a toggle
        # ah shit already used out to be boolean for valid out path?

        out_message, valid = "", True

        # verify source file
        if self.f_in.get() =='':
            out_message += "Please enter source file path\n"
            valid = False
        else:
            if not hf.verify_file(self.f_in.get(), exists=True):
                valid = False
                out_message += "Source file doesn't exist or isn't writeable\n"

        # verify target file
        if self.out:
            if self.f_out.get() =='':
                out_message +="Please enter target file path\n"
                valid = False
            else:
                if not hf.verify_file(self.f_out.get(), exists=False):
                    valid = False
                    out_message += "Target file directory does not exist\n"

        # verify widths
        if self.widths.get() =='':
            out_message += "Please enter file widths\n"
            valid = False
        else:
            if not hf.verify_widths(self.widths.get()):
                valid = False
                out_message += "Invalid widths; please supply string of comma-separated integers\n"

        if not valid:
            self.log_message.set(out_message)
            self.log_box.config(fg='red')
        return valid

    def get_value(self):
        #print('the function call to GET_VALUE worked')
        message = ""

        # verify arguments:
        try:
            # verify shared arguments:
            if not self.verify_args(): return

            # verify edit-specific args: caught by valueError
            row = int(self.row.get())
            field = int(self.field.get())
        except ValueError:
            hf.print_exception(self, 'Please make sure Row and Field are integers')
            return
        except Exception as e:
            message = "Error validating arguemnts: " + str(e)
            hf.print_exception(self, message)
            return
        try:
            success, message, value = fv.get_value(self.f_in.get(), self.row.get(), self.field.get(), self.widths.get())
            if success:
                self.field_value_var.set(value)
                self.log_box.config(fg='green')
            else:
                self.log_box.config(fg='red')
            self.log_message.set(message)
        except Exception as e:
            message = "Error getting field value: " + str(e)
            hf.print_exception(self, message)

    def update_value(self):
        #print('the function call to GET_VALUE worked')
        message = ""

        # verify arguments:
        try:
            # verify shared arguments:
            if not self.verify_args(): return

            # verify edit-specific args: caught by valueError
            row = int(self.row.get())
            field = int(self.field.get())

            # verify update-specific args:
            if len(self.pad_char.get()) != 1:
                hf.print_exception(self, 'Please pass only a single character as the pad character')
                return
        except ValueError:
            hf.print_exception(self, 'Please make sure Row and Field are integers')
            return
        except Exception as e:
            message = "Error validating arguments: " + str(e)
            hf.print_exception(self, message)
            return

        try:
            success, message = fv.update_value(self.f_in.get(), self.row.get(), self.field.get(), self.widths.get(), self.field_value_var.get(), self.pad_char.get(), self.pad_side.get())
            if success:
                self.log_box.config(fg='green')
            else:
                self.log_box.config(fg='red')
            self.log_message.set(message)
        except Exception as e:
            message = "Error updating field value: " + str(e)
            hf.print_exception(self, message)


###
# this needs major cleaning up oh well
