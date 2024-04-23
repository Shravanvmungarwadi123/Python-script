# Python-script

Log Monitor and Analyzer
This Python script provides functionalities for monitoring and analyzing a log file.

Prerequisites:
1) Python 3.x (Make sure you have Python installed by running python --version in your terminal)
Running the Script:

2) Replace log_file: Edit the script and update the log_file variable with the actual path to your log file.

3) Run the Script:
Open a terminal or command prompt and navigate to the directory containing the script.
Run the script using the following command:

python logging.py
Use code with caution.

Explanation:
The script offers two functionalities:

1) Log File Monitoring (tail_logs function):
This function continuously monitors the specified log file for new entries using the tail command.
When the script starts, it begins tailing the log file and displays any new lines that get added.
You can press Ctrl+C to stop the monitoring.

2) Log File Analysis (analyze_logs function):
This function analyzes the entire log file content (not just new entries) for lines containing the keyword "ERROR" (case-sensitive).
It then prints the total number of errors found in the log file.

Testing:
Verify Log File Path: Ensure the log_file variable points to a valid and existing log file.
Monitoring Test: Run the script and observe the terminal. If the log file has activity, you should see new lines being printed as they are added to the file. Press Ctrl+C to stop monitoring.

Analysis Test: Make sure your log file contains some errors (lines with "ERROR"). Run the script and check the output for the total number of errors reported. You can manually add or remove errors from your log file to test the analysis further.

Additional Notes:
This script provides a basic example of log monitoring and analysis. You can modify it to search for different keywords or patterns in the logs.
The script uses basic logging to provide informative messages during execution.
