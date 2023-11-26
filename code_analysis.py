import subprocess
import os

def run_pylint(directory):
    html_report_file = "pylint_report.html"

    # Get a list of Python files in the specified directory
    python_files = [f for f in os.listdir(directory) if f.endswith(".py")]

    # Run pylint and generate HTML report for each Python file
    for python_file in python_files:
        command = f"pylint-json2html -o {html_report_file} {os.path.join(directory, python_file)}"
        subprocess.run(command, shell=True)

def main():
    code_directory = "code_directory"
    run_pylint(code_directory)

if __name__ == "__main__":
    main()
