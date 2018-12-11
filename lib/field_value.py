# need to add error handling:
#	widths don't match up with file
# 	file is single line, but multi-line parser was run
# add some try/except blocks

# i have to just loop through every field
# ooh I'm going to need code from my add_lines script

def get_value(in_file, row, field, widths):
	'''
	Returns value at specified row and field number of file
	Assumes widths given as string of comma-separated integers
	'''

	# initialize variables
	index = 0
	out_message = ""
	row_found = False
	field_found = False
	field_value = ""
	row = int(row)
	field = int(field)

	# convert to integers
	widths = [ int(x) for x in widths.split(",") ]
	field = int(field)

	# open files:
	with open(in_file, 'r') as in_file:
		# loop through file:
		for line in in_file:
			index += 1

			if index != row:	# skip row if wrong row
				continue

			row_found = True

			try:
				start,end = get_indices(widths,field)
			except IndexError as e:
				field_found = False
				out_message = "Given field number out of range for provided widths"
				break

			# python is forgiving with substring indices, so added my own error handling
			if start >= len(line):
				field_found = False
				out_message = "Starting index out of range for field and row"
				break
			elif end >= len(line):
				field_value = line[start:end]
				out_message = "Line shorter than specified field length"
				break
			else:
				out_message = "Line found successfully"
				field_value = line[start:end]
				field_found = True
				break

	if not row_found:
		out_message = "Specified row out of index range"

	return [ row_found and field_found , out_message , field_value ]

def update_value(file, row, field, widths, new_value, pad_char, pad_side):
	'''
	Updates specified field in specified row in fixed width file
	'''
	# initialize variables
	index = 0
	out_message = ""
	row_found = False
	field_found = False
	valid = True
	row = int(row)
	field = int(field)

	# convert to integers
	widths = [ int(x) for x in widths.split(",") ]
	field = int(field)

	# open files:
	with open(file, 'r') as f:
		# get lines:
		lines = f.readlines()

	with open(file, 'w') as f:
		# truncate file:
		f.truncate()

		for line in lines:
			index += 1

			if index != row:	# skip row if wrong row
				f.write(line)	# write line back to file
				continue
			else:
				row_found = True

				# Get index values from index list
				try:
					start,end = get_indices(widths,field)
				except IndexError as e:
					out_message = "Given field number out of range for provided widths"
					valid = False

				# validate replacement value against field width:
				len_diff = end - start - len(new_value)
				if len_diff < 0 :
					out_message = "Replacement value is longer than field to be replaced"
					valid = False

				# Validate widths against line
				if start >= len(line):
					out_message = "Starting index out of range for field and row"
					valid = False
				elif end >= len(line):
					# could do some handling in this scenario but I'm going to be lazy and not
					out_message = "Line shorter than specified field length"
					valid = False

				if valid:
					# Replace value:
					field_found = True
					valid = True
					updated_line = replace_value(line, start, end, new_value, pad_char, pad_side) # this should not throw any errors, can add some later just to have them
					f.write(updated_line)
					out_message = "Field %s overwritten successfully" % str(field)
				else:
					# if arguments are invalid, write un-edited line back to file
					f.write(line)

	if not row_found:
		out_message = "Specified row out of index range"

	return [ row_found and field_found and valid , out_message ]

def replace_value(text, start, end, value, pad_char, pad_side):
	'''
	Replaces value between the given indices in text with value;
	Pads with pad char on left or right for pad_side values of LEFT and RIGHT
	'''
	len_diff = end - start - len(value)
	if pad_side == 'RIGHT' :
		value = value + pad_char * len_diff
	elif pad_side == 'LEFT' :
		value = pad_char * len_diff + value

	if end >= len(text): # need to add line break if replacing the end of a line
		lb = '\n'
	else:
		lb = ''

	return text[0:start] + value + text[end : ] + lb

def get_indices(widths, field):
	'''
	Returns the starting and ending indices for given field
	Assumes field is given as int and widths is given as list of ints
	Field assumed to be indexed from 1 (first field index = 1; last field index =len(widths))
	'''
	field -= 1 # change index starting from 0
	prev_sum = sum(widths[:field])
	return [ prev_sum , prev_sum + widths[field]]
