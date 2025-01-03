# Get the list of folders from the parent of this path except "Validate" folder
from os import listdir
from os.path import isdir, join
from datetime import datetime
import importlib.util
from time import time
import run_solution


# if command line argument is given then use that as the folder name or collect all the folders from the parent directory
import sys
if len(sys.argv) > 1:
    folders = [sys.argv[1]]
else:
    folders = [f for f in listdir('../') if isdir(join('../', f)) and f != 'Validate']
print(folders)

# open a data base file for sql and create table with Folder name, Program name, time executed, status and time taken to execute
import sqlite3
conn = sqlite3.connect('assignments_updated.db')
c = conn.cursor()

# Create table if not exists with Name as primary key column, program, time_executed, status and time_taken as columns in the table assignments
c.execute('''CREATE TABLE IF NOT EXISTS assignments
                (Name text PRIMARY KEY, program text, time_executed text, status text, time_taken text)''') 


# From each folder get files "program1.py", "program2.py", "program3.py" import those as modules and run solution function from each file
# and store the time taken to execute the function and status of the function in the database and time when it ran in the database
# write a function to accepts folders and run the programs in the folders
def run_programs(folders):
    for folder in folders:
        for i in range(1, 4):
            spec = importlib.util.spec_from_file_location(f'{folder}.program{i}', f'../{folder}/Assignment{i}.py')
            module = importlib.util.module_from_spec(spec)
            # what is module_from_spec and spec_from_file_location
            start = time()

            try:
                spec.loader.exec_module(module)
                # pass module to function test_solution which is there in run_solution.py in current directory and collect the result
                status = run_solution.test_solution(module)

            except Exception as e:
                status = 'Failed'
                print(e)
                print(f'Error in {folder} program{i}')

            end = time()
            time_taken = end - start
            # update the data if the folder text is already there or create a new row with folder name, program name, time executed, status and time taken
            c.execute("INSERT OR REPLACE INTO assignments (Name, program, time_executed, status, time_taken) VALUES (?, ?, ?, ?, ?)", (folder, f'program{i}', datetime.now(), status, time_taken))
            
            conn.commit()



# Write a function to get the table from the database and print the table
def get_table():
    conn = sqlite3.connect('assignments_updated.db')
    c = conn.cursor()
    c.execute("SELECT * FROM assignments")
    # fetch all the details and generate an image and save it in the current directory
    rows = c.fetchall()
    print(rows)
    # dump rows to a csv file 
    
    with open('assignments.csv', 'w') as f:
        for row in rows:
            f.write(','.join(map(str, row)) + '\n')

    print(rows)
    conn.close()

if __name__ == "__main__":
    run_programs(folders)
    conn.close()
    get_table()
