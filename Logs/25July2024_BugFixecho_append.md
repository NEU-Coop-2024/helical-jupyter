Fixed bug mentioned in the 7/24 log, replaced return with exec to correct the behavior.

```%%echo_append ```
```print('1')```

should output 

```1```
```Success!```

We speclated that using exec was the reason for the bugged cell count mentioned in the July15th log, but since 
I had reinstalled the Jupyter notebook, we were not able to conclude the precise reason for that bug. 

It is possible that using exec may result in a bugged cell count where it will skip certain numbers when notebook runs, however I have yet to 
see this behavior arise as of now. 
