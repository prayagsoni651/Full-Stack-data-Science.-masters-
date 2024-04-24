#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''

1. Create a zoo.py file first. Define the hours() function, which prints the string 'Open 9-5 daily'.
Then, use the interactive interpreter to import the zoo module and call its hours() function.
'''

# zoo.py

def hours():
    print('Open 9-5 daily')


# In[ ]:


'''

2. In the interactive interpreter, import the zoo module as menagerie and call its hours() function.
'''

import zoo as menagerie
menagerie.hours()



# In[ ]:


'''
3. Using the interpreter, explicitly import and call the hours() function from zoo.

'''

from zoo import hours
hours()



# In[ ]:


'''
4. Import the hours() function as info and call it.

'''

>>> from zoo import hours as info
>>> info()
Open 9-5 daily



# In[ ]:


'''

5. Create a plain dictionary with the key-value pairs &#39;a&#39;: 1,
&#39;b&#39;: 2, and &#39;c&#39;: 3, and print it out.
'''

# Create a dictionary
plain_dict = {'a': 1, 'b': 2, 'c': 3}

# Print the dictionary
print(plain_dict)


# In[7]:


'''
6.Make an OrderedDict called fancy from the same pairs listed in 5 and print it. Did it print in the
same order as plain?

'''

from collections import OrderedDict

# Create an OrderedDict
fancy = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Print the OrderedDict
print(fancy)


# In[8]:


'''
7. Make a default dictionary called dict_of_lists and pass it the argument list. Make the list
dict_of_lists[&#39;a&#39;] and append the value &#39;something for a&#39; to it in one assignment. Print
dict_of_lists[&#39;a&#39;].

'''

from collections import defaultdict

# Create a defaultdict with default value type list
dict_of_lists = defaultdict(list)

# Append 'something for a' to the list associated with key 'a'
dict_of_lists['a'].append('something for a')

# Print the list associated with key 'a'
print(dict_of_lists['a'])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




