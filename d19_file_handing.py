# Syntax
# > open('filename', mode)
# > mode(r,a,w,x,t,b) read, append, write, create, t, b
f = open('./README.md')
print(f)

# # read() read the whole text as string
txt = f.read()
print(txt)

# # readlines() read all text line by line and returns a list of lines
lines = f.readlines()
print(type(lines))
print(lines)
f.close()

# # open Files for writing and updating
# > with statement 
# >  It allows you to ensure that a resource is "cleaned up" when the code that uses it finishes running
with open('./README.md', 'a') as f:  # Using 'w' will recover it
    f.write('It is appended by python')
