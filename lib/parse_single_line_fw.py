from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("file", help = "Path to file to parse")
parser.add_argument("widths", help = "comma-separated list of field widths")
parser.add_argument("--out" , help = "specify file name")
parser.add_argument("--length" , help = "specify line length")
parser.add_argument("--txt", help = "1/0; If 1, export text file with lines of specified length")


args = parser.parse_args()

in_file = open(args.file, 'r')
if args.out is None:
	o_file = open('fw_parse.csv', 'w')
#	end = in_file.rfind(".")
#	o_file_name = in_file[0:end] + "_parsed.csv"
#	o_file = open(o_file_name, 'w')
else:
	o_file = open(args.out, 'w')
widths = args.widths.split(",")
line_len = int(args.length)
txt_out = int(args.txt)

line = in_file.readline()
while len(line) >= line_len:
	parse = line[0:line_len]
	line = line[line_len:]
	if txt_out == 1:
		o_file.write(parse + "\n")
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
		o_file.write(out_line)
