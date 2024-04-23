# Log Analysis and Monitoring Script

import logging
import subprocess

# Configure logging. Set logging level and get logger for this script
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Log file to monitor (replace with your actual path)
log_file = "your_log_file_path.log"

def tail_logs(log_file):
    """
    Continuously monitor the specified log file for new entries.
    """
    try:
        # Run tail command with options: -F for following, log_file for path
        process = subprocess.Popen(['tail', '-F', log_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        for line in iter(process.stdout.readline, b''): # Read lines from stdout until empty byte string
            logger.info(line.decode().strip()) # Decode, strip whitespace, and log as info
    except KeyboardInterrupt:
        logger.info("Monitoring interrupted. Exiting.") # Log info on Ctrl+C interrupt
    finally:
        process.terminate() # Terminate the tail process

def analyze_logs(log_file):
    """
    Analyze log entries for specific keywords or patterns.
    """
    try:
        with open(log_file, 'r') as file: # Open log file in read mode
            log_data = file.readlines() # Read all lines into a list
            error_count = 0
            for line in log_data:
                if "ERROR" in line: # Check if line contains "ERROR" (case-sensitive)
                    error_count += 1
            logger.info(f"Total errors: {error_count}") # Log total errors found
    except FileNotFoundError:
        logger.error("Log file not found.") # Log error if file not found
    except Exception as e:
        logger.error(f"An error occurred: {e}") # Log any other exceptions

if __name__ == "__main__":
    try:
        # Start log file monitoring
        tail_logs(log_file)
    except Exception as e:
        logger.error(f"An error occurred during monitoring: {e}")

    try:
        # Analyze log file
        analyze_logs(log_file)
    except Exception as e:
        logger.error(f"An error occurred during log analysis: {e}")
