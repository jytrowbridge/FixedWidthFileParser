def parse_single_line_fw_file(in_file, out_file, widths):
	widths = [int(x) for x in widths.split(",")]

	with open(in_file, 'r') as f_in, open(out_file, 'w') as f_out:
		line = f_in.readline()
		out_message = ""	# if function returns false, out_message will be printed to log box
		line_len = len(line)
		while len(line) >= line_len:
			parse = line[0:line_len]
			line = line[line_len:]

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
			f_out.write(out_line)

	return [ True , out_message ]
