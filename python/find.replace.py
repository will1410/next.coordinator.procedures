# Read in the file
with open('C:/Users/George/Documents/GitHub/next.coordinator.procedures/python/file.txt', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('<<branches.branchcode>>', '[% branch.branchcode %]')

# Write the file out again
with open('C:/Users/George/Documents/GitHub/next.coordinator.procedures/python/file.txt', 'w') as file:
  file.write(filedata)
