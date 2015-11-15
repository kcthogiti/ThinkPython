



def row_line(n, e):
	print "+",
	for i in range(1,n):
		print "-"*e,"+",
	return ""
	
def column_line(n, e):
	
	for j in range(0,e):
		print "|",
		for i in range(1,n):
			print " "*e, "|",
		if j!=(e-1):
			print ""
	return ""


def print_grid(n,e):
	print row_line(n, e)
	for i in range(1,n):
		print column_line(n, e)
		print row_line(n, e)
	return ""

nodes = raw_input("Enter the number of nodes")
edges = raw_input("Enter the number in edges")
print print_grid(int(nodes),int(edges))


