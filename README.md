# Checkmarx_Home_Assignment

Our program is using the numpy library and then returning "Hello World!"

Build stage -
In this step we will set up the runtime environment by installing the relevant version of the python libraries to make sure our software has the correct environment to run.
This is why we use 'pip install -r requirements.txt'
In requirements.txt written 'numpy==1.21.0' - we will install this version of the numpy library because this is what the running environment need to run our program.

Test stage -
We command 'python -m unittest tests.py'.
The code in tests.py checks if our program's return is equal to what we want.
If our program returns an error, we set currentBuild.result to 'FAILURE' and at the end of the file we return 'Pipeline failed: Tests not passed.'.

Deploy stage  -
If all our tests complete and succeed, we'll clone our program(main.py) from https://github.com/GuyShemesh66/Checkmarx_Home_Assignment.git into a new local file named "tested_program" to make sure that the program is updated ,ready to work on and passes all the previous tests.