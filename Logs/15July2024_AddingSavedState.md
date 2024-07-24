Versions Used:
Python 3.11.9
Jupyter Notebook Version: 7.2.1
Python 3 kernel

Saving state across cells in Jupyter Notebook: 

I began by creating an instance string variable in a Python constructor class. This variable is used to accumulate the contents of a cell when %%echo_append is called. 
When %%echo_append is called, the cell's contents are appended to the string variable, which is then executed using exec().

While working on EchoPackage, I encountered an issue where the cell counter would not accumulate correctly. If I ran one cell, the cell count would read as [1], and if I ran another cell, the cell
count would read as [3]. It would essentially skip all even numbers. Upon closer inspection of the script, I determined that it was not a code-related issue; and that it was likely an issue with the environment.
I speculate that it was because of some unknown modification to a Jupyter dependency that I had made which caused the cell counter to increment incorrectly. Therefore, it is highly advisable to test your Python packages
in a virtual environment, isolated from other system dependencies to avoid such issues. 
