import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import helper_functions as hf
import config as conf
import FileEditGui as feg

class ParseFw:

    def __init__(self, master):
        self.master = master
        master.title("Jack's Fixed Width File Parser")

        # icon
        #self.master.iconbitmap(r'C:/Users/jack.trowbridge/Documents/Allied/parseFileGui/straw_hat.ico')
        #self.master.iconbitmap(r'C:/Users/jack.trowbridge/Documents/Allied/parseFileGui/jack.ico')
        #icon_file_path = conf.ico_dir + "jack.ico"
        #self.master.iconbitmap(icon_file_path)

        # create notebook for tabbing
        self.master_note = ttk.Notebook(self.master)

        # load configurations
        self.parser_conf(self.master_note)
        self.edit_conf(self.master_note)

        self.master_note.add(self.master_parser_frame, text = 'Parse File')
        self.master_note.add(self.master_edit_frame, text = "Edit File", compound=tk.TOP)
        self.master_note.grid()

    ##############
    # METHODS
    ############

    def edit_conf(self, parent):
        '''
        Tkinter configuration for the edit tab
        '''

        # initialize the object
        self.master_edit_obj = feg.FileEditGui(parent)
        self.master_edit_frame = self.master_edit_obj.master_frame
        self.master_edit_obj.log_message.set("Select a file!")

        #######
        # field value box
        self.master_edit_obj.field_value_var = tk.StringVar()
        self.master_edit_obj.field_value_label = tk.Label(self.master_edit_obj.option_frame,text='Field Value:')
        self.master_edit_obj.field_value_box = tk.Entry(self.master_edit_obj.option_frame,width=50, textvariable=self.master_edit_obj.field_value_var)

        # grid
        self.master_edit_obj.field_value_label.grid(row=2,column=0,pady=5)
        self.master_edit_obj.field_value_box.grid(row=2,column=1)

        #######
        # arguments frame
        self.master_edit_obj.edit_args_frame = tk.Frame(self.master_edit_obj.option_frame)
        self.master_edit_obj.row = tk.StringVar()
        self.master_edit_obj.field = tk.StringVar()
        self.master_edit_obj.v_pad_lbl = tk.StringVar()
        self.master_edit_obj.row_lbl = tk.Label(self.master_edit_obj.edit_args_frame, text="Row Number:")
        self.master_edit_obj.row_box = tk.Entry(self.master_edit_obj.edit_args_frame,width=5, textvariable=self.master_edit_obj.row)
        self.master_edit_obj.field_lbl = tk.Label(self.master_edit_obj.edit_args_frame, text="Field Number:")
        self.master_edit_obj.field_box = tk.Entry(self.master_edit_obj.edit_args_frame, width=5, textvariable=self.master_edit_obj.field)
        #self.master_edit_obj.pad_hide = tk.Button(self.master_edit_obj.edit_args_frame, text="Show Pad Options", command=self.hide_pad_options)
        self.master_edit_obj.pad_hide = tk.Button(self.master_edit_obj.edit_args_frame, textvariable=self.master_edit_obj.v_pad_lbl, command=self.hide_pad_options, width=14)

        # grid
        self.master_edit_obj.edit_args_frame.grid(row=3, column = 0, padx=5, pady=5, columnspan=3)
        self.master_edit_obj.row_lbl.grid(row=0,column=0,padx=5,pady=5)
        self.master_edit_obj.row_box.grid(row=0,column=1,padx=5)
        self.master_edit_obj.field_lbl.grid(row=0,column=2,padx=5)
        self.master_edit_obj.field_box.grid(row=0,column=3,padx=5)
        self.master_edit_obj.pad_hide.grid(row=0,column=4,padx=5)

        #######
        # Pad options
        self.pad_hidden = False
        self.master_edit_obj.pad_char = tk.StringVar()
        self.master_edit_obj.pad_side = tk.StringVar()
        self.master_edit_obj.pad_frame = tk.Frame(self.master_edit_obj.option_frame,bd=2,relief=tk.SUNKEN)
        self.master_edit_obj.pad_lbl = tk.Label(self.master_edit_obj.pad_frame, text="Pad Char:")
        self.master_edit_obj.pad_box = tk.Entry(self.master_edit_obj.pad_frame, width=3, textvariable=self.master_edit_obj.pad_char)
        self.master_edit_obj.pad_left = tk.Radiobutton(self.master_edit_obj.pad_frame, text="Pad Left", variable = self.master_edit_obj.pad_side, value='LEFT')
        self.master_edit_obj.pad_right = tk.Radiobutton(self.master_edit_obj.pad_frame, text="Pad Right", variable = self.master_edit_obj.pad_side, value='RIGHT')

        # pad grid
        self.master_edit_obj.pad_frame.grid(row=4,column=1,padx=5,pady=5)
        self.master_edit_obj.pad_lbl.grid(row=0,column=1,padx=5)
        self.master_edit_obj.pad_box.grid(row=0,column=2,padx=5)
        self.master_edit_obj.pad_left.grid(row=0,column=3,padx=5)
        self.master_edit_obj.pad_right.grid(row=0,column=4,padx=5)

        #######
        # run buttons
        self.master_edit_obj.run_button_frame = tk.Frame(self.master_edit_obj.option_frame)
        self.master_edit_obj.update_value = tk.Button(self.master_edit_obj.run_button_frame,text="Update Value",command=self.master_edit_obj.update_value,width=10)
        self.master_edit_obj.get_value = tk.Button(self.master_edit_obj.run_button_frame,text="Get Value",command=self.master_edit_obj.get_value,width=10)

        # run button grid
        self.master_edit_obj.run_button_frame.grid(row=5,column=1)
        self.master_edit_obj.update_value.grid(row=0,column=0,padx=5)
        self.master_edit_obj.get_value.grid(row=0,column=1,padx=5)

        #######
        # initialize variables:
        self.master_edit_obj.pad_side.set("LEFT")
        self.master_edit_obj.pad_char.set(" ")
        self.master_edit_obj.pad_left.select()
        self.hide_pad_options()

        # maybe makes more sense to put this in the class file? as methods?... would reduce the number of calls to shit

    def parser_conf(self, parent):
        '''
        Tkinter configuration for the parser tab
        '''

        # initialize the object
        self.master_parser_obj = feg.FileEditGui(parent, out=True)
        self.master_parser_frame = self.master_parser_obj.master_frame
        self.master_parser_obj.log_message.set("Parse a file!")

        # add run button
        self.master_parser_obj.run_btn = tk.Button(self.master_parser_obj.run_frame, text="Parse File", command=self.master_parser_obj.parse_file)
        self.master_parser_obj.run_btn.grid(row=0, column=1, padx = 5)
        self.master_parser_obj.run_frame.grid(row=1,column=1)

        # Radio button
        self.master_parser_obj.type_rad = tk.Label(self.master_parser_obj.option_frame, text="File Type:")
        self.master_parser_obj.rad_frame = tk.Frame(self.master_parser_obj.option_frame)
        self.master_parser_obj.type = tk.StringVar()
        self.master_parser_obj.multi_rad = tk.Radiobutton(self.master_parser_obj.rad_frame, text="Multi Line", variable = self.master_parser_obj.type, value='MULTI')
        self.master_parser_obj.single_rad = tk.Radiobutton(self.master_parser_obj.rad_frame, text="Single Line", variable = self.master_parser_obj.type, value='SINGLE')

        self.master_parser_obj.type_rad.grid(row=3, column=0)
        self.master_parser_obj.multi_rad.grid(row=0, column=0,padx=5)
        self.master_parser_obj.single_rad.grid(row=0, column=1,padx=5)
        self.master_parser_obj.rad_frame.grid(row=3,column=1)

        self.master_parser_obj.type.set("MULTI")
        self.master_parser_obj.multi_rad.select()

    def hide_pad_options(self):
        if self.pad_hidden:
            self.master_edit_obj.pad_frame.grid()
            self.master_edit_obj.v_pad_lbl.set("Hide Pad Options")
        else:
            self.master_edit_obj.pad_frame.grid_remove()
            self.master_edit_obj.v_pad_lbl.set("Show Pad Options")
        self.pad_hidden = not self.pad_hidden

def main():
    root = tk.Tk()
    gui = ParseFw(root)
    root.mainloop()

if __name__ == "__main__":
    main()
