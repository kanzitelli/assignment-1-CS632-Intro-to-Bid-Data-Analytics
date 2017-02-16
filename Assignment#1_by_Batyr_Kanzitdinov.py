
# coding: utf-8

# In[20]:

# (A)
# function for converting Celsius degrees to Fahrenheit degrees and vice versa.
# params: scale - input scale, temp - input temperature
# return: tuple with result scale and answer

def converter(scale='C', temp=0.0):
    if scale == 'C':
        return ('F', (temp * (9.0/5.0)) + 32.0)
    elif scale == 'F':
        return ('C', (temp - 32.0) * (5.0/9.0))
    else:
        print("Please, enter F or C")

scale = raw_input("Enter F or C: ")
temp = int(raw_input("Temperature: "))
s, t = converter(scale, temp)
print('{0}°{1} is {2} degrees {3}'.format(temp, scale, t, s))


# In[21]:

# (B)
# Write up a Python script that will copy the contents of one file into another

from os.path import exists

from_file = raw_input('Enter file name where we copy information from: ')
to_file = raw_input('Enter name of the new file: ')

print 'Does the output file exist? - {0}'.format(exists(to_file))
while exists(to_file):
    to_file = raw_input('Please, enter name of the new file: ')

print 'Copying from {0} to {1}'.format(from_file, to_file)

with open(from_file)as f: indata = f.read()
print 'The input file is {0} bytes long'.format(len(indata))
print 'Ready, hit RETURN to continue, CTRL- C to abort.' 
raw_input()

out_file = open(to_file, 'w') 
out_file.write(indata)

print "Alright, all done." 

out_file.close()


# In[22]:

# (C)
# Print an alphabetically sorted list of all functions in the re module, which contain the word find.

import re
all_functions = dir(re)
all_find_functions = []
for f in all_functions:
    if 'find' in f:
        all_find_functions.append(f)
print '{0}'.format(sorted(all_find_functions))
#print('{0}'.format(dir(re)))


# In[23]:

# (D)
# Probability Density Function of Normal Distribution

from IPython.display import Math
Math(r'P(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-(x-\mu)^2/(2\sigma^2)}')


# In[ ]:



