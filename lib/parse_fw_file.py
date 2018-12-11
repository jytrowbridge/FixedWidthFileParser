# need to add error handling:
#	widths don't match up with file
# 	file is single line, but multi-line parser was run
# add some try/except blocks

# need to open the file
def parse_fw_file(in_file, out_file, widths):
	'''
	Returns tuple [result, message] where:
	Result is booelan value representing success or failure of script
	Message is string to be printed to user
	'''
	widths = widths.split(",")

	out_message = ""
	index = 0
	wider = False
	narrower = False
	widths = [int(x) for x in widths] # convert to integers
	widths_sum = sum(widths) + 1
	#print(widths_sum)

	# open files:
	with open(in_file, 'r') as in_file, open(out_file, 'w') as out_file:
		# loop through file:
		for line in in_file:
			index += 1

			# make sure widths line up with line length:
			if len(line) < widths_sum and not narrower:
				narrower = True
				out_message += "Warning: Line length less than expected (starting at line " + str(index) + ")\n"
			elif len(line) > widths_sum and not wider:
				wider = True
				out_message += "Warning: Line length greater than expected (starting at line " + str(index) + ")\n"
				# Note that this won't break the function; when line[end:] is called, will return ''

			out_line = ""
			start = 0
			count = 0
			for i in range(len(widths)):
				field_len = widths[i]
				end = start + field_len
				out_line += '"' + line[start:end].strip() + '"'
				start = end
				count += 1
				if count != len(widths):
					out_line += ","
			out_line += "\n"
			out_file.write(out_line)

	return [ not ( wider or narrower ), out_message ]
