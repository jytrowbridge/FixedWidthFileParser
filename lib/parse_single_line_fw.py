def parse_single_line_fw_file(in_file, out_file, widths):
	line = in_file.readline()
	out_message = ""	# if function returns false, out_message will be printed to log box

	while len(line) >= line_len:
		parse = line[0:line_len]
		line = line[line_len:]
		if txt_out == 1:
			out_file.write(parse + "\n")
		else:
			out_line = ""
			start = 0
			count = 0
			for field_len in widths:
				end = start + int(field_len)
				out_line += '"' + parse[start:end].strip() + '"'
				start = end
				count += 1
				if count != len(widths):
					out_line += ","
			out_line += "\n"
			out_file.write(out_line)

	return [ True , out_message ]
