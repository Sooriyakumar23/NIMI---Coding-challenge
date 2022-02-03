### How to run me ?
      I. Create a new folder
     II. Create new environment for this application
        * open anaconda terminal in this folder path
        * run this command: conda create -n {Environment Name} python=3.7
        * Press y & Enter to install all necessary dependancies
        * run this command: conda activate {Environment Name} - to activate the environment
    III. Git clone this repo into the new folder: https://github.com/Sooriyakumar23/NIMI-Coding-challenge.git
     IV. Install requirements using pip command: pip install -r requirements.txt
                - This will install all the modules that are necessary to run this backend application
      V. Run directly the backend application bank.py: python bank.py in command prompt or open this python file in any your preferred IDE & run from there
     VI. Now can communicate using API methodologies to do the things that we need

* Eventhough usually bank accounts contains several information of the users, I used some necessary information only (NIC number, Name, Place, Occupation, Contact phone number, Amount in account) - Detailed information presented in "Input_details.md"

### How to use API ?
    - Once the bank.py code get started to run we can call API functions
    - I set port to 2305. You can change to whatever you wish by modifying last line of code in bank.py file)
    - Open a web browser(Chrome) to call apis
    - run particular url for the particular need
    - input your value in between angular brackets ; e.g: {nic} = 971234567
*       Create a new bank account
                http://127.0.0.1:2305/create/{nic}/{name}/{place}/{work}/{contact}/{amount}
        - New account creates with nic(National Identity Card number), name, place, occupation/work, contact number and amount
*       Delete an existing account
                http://127.0.0.1:2305/delete/{nic}
        - National Identity Card number is unique to all accounts so this is used to detect and delete the account
        
*       Update an existing account
                http://127.0.0.1:2305/update/{nic}/{field}/{value}
        - Field should be name/ place/ occupation/ contact number/ amount and value is the value that we want to update for the field of particular nic(National Identity Card number)

*       Reading an account
                http://127.0.0.1:2305/read/{nic}
        - National Identity Card number is unique to all accounts so this is used to detect and read the account
        
*       Archive an unarchived account / Unarchive and archived account
                http://127.0.0.1:2305/status/{nic}/{status}
        - status = archive / unarchive -> archive / unarchive particular account under nic
        
*       List all the archived accounts / unarchived accounts
                http://127.0.0.1:2305/accounts/{status}
        - List down all the accounts where status = archive / unarchive

### Test cases
*       All the possible test cases also written, tested and and printed the received response
- 1_test_create.py - Create 10 new accounts
- 2_test_delete.py - Delete 4 existing accounts
- 3_test_update.py - Update 5 existing accounts
- 4_test_read.py - Read 6 existing accounts
- 5_test_status.py - Switch 6 accounts between archive <-> unarchive
- 6_test_accounts.py - Print down all the unarchived and archived accounts

### Technologies used
* Used technologies -> REST Api + Python
1. Sublime Text - Source code editor
    - Natively supports many languages and markup languages
    - Light weight
    - Easy to use
    - Free software
2. Flask - Micro web framework in python 
    - Light weight
    - Easier to use for simple usecase (single/lower page application)
    - Routing url is easy
    - I have little prior familiarity
3. Anaconda environment
    - To isolate this application from general use
4. pandas -> to write list elements into a csv file
5. csv -> to read csv files
    - Bank account details stored in a csv file 
           * Easy to use 
           * Human readable
           * Permanent (Memory storage is temporary)
          
### Future improvements
      I. SQL database can be used instead of CSV for storing bank account details
     II. Increasing security using asymmetric key encryption methodologies 
        - Now it is vulnerable to cyber attack (Easy to get NIC from API & Account details exposable when creating a new account)
    III. Deploying the app in cloud for remote access, scaling and safety
     IV. Fraud detection system can be developed using machine learning approaches
      V. Data analysis for bank customer segmentation
    VI. Virutal environment is better for this application since it deals with front end and not needed complex system
                https://dataaspirant.com/anaconda-python-virtualenv/