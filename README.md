# OTP program
This is an OPT program that offers a randomly produced pad and can help the user encipher and decipher plain texts using this one-time pad.
Through the translation process, punctuations are ignored.

This program also includes several unit tests to make sure things are going well.
There are in total 6 tests for the 3 functions - 2 tests for each function.
The goal of each unit test is commented.

To run the main program, the user just needs to run the program using the syntax "python cipher.py".
The length of the OTP is set as 1200.
With the plain texts in the same directory, the program can encipher and decipher the texts using the OTP.
The length of the OTP can also be changed by the user.
The user can just replace 1200 with any number they want for the length of the OTP.

To run the unit tests, the user needs to have pytest installed. (Pytest can be installed with "pip install -U pytest")
Then the user needs to input "pytest cipher-test.py".
The unit tests will then work.
