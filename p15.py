# p15 copy a file

import os
src_filename = input("enter source filename ")
if os.path.isfile(src_filename):
	dest_filename = input("enter dest filename ")
	fsrc = None
	fdest = None
	try:
		fsrc = open(src_filename, "r")
		fdest = open(dest_filename, "w") 
		data = fsrc.read()
		fdest.write(data)
		print("copy completed")
	except Exception as e:
		print("issue ", e)
	finally:
		if fsrc is None:
			fsrc.close()
		if fdest is not None:
			fdest.close()
else:
	print(src_filename," does not exists " )

# non text file copy krne ke liy rb and wb likhna --> since its a binary file
# rb and wb file sab files copy ho skte hain