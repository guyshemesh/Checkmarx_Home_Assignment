# Checkmarx_Home_Assignment

the program - using numpy library and then and then return "Hello World!"

Build stage -
in this stage we will set up the running environment by install the relevant version of the python libraries to make sure that our program has the right environment to run.
this is why we use 'pip install -r requirements.txt'
In requirements.txt written 'numpy==1.21.0'- we will install this version of numpy library because that's what require to run our program.

Test stage -
we run 'python -m unittest tests.py'.
the code in tests.py is checking if the return of our program is equal to what we want.
if the our program return is a mistake, we set  currentBuild.result  as 'FAILURE' and at the end of the file we return 'Pipeline failed: Tests did not pass.'.

Deploy stage  -
if all our  test finish and succeed , we will clone our program(main.py) by using the command 'scp' to git@github.com:GuyShemesh66/-Checkmarx_Assignment_deploy.git.
