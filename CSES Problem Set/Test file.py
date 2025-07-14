import subprocess
import os

def run_tests(folder_path, script_path):
    test_files = sorted(f for f in os.listdir(folder_path) if f.endswith('.in'))

    for test_file in test_files:
        test_number = test_file.split('.')[0]
        input_path = os.path.join(folder_path, f'{test_number}.in')
        output_path = os.path.join(folder_path, f'{test_number}.out')

        with open(input_path, 'r') as f:
            input_data = f.read()

        with open(output_path, 'r') as f:
            expected_output = f.read().strip().splitlines()

        # Run the solution script
        result = subprocess.run(
            ['python', script_path],
            input=input_data.encode(),
            capture_output=True
        )

        actual_output = result.stdout.decode().strip().splitlines()

        if actual_output == expected_output:
            print(f"test#{test_number} : Passed")
        else:
            print(f"test#{test_number} : Failed")
            print(f"Expected = {expected_output}")
            print(f"Output   = {actual_output}")

# Example usage
run_tests(folder_path='./tests', script_path='Weird Algorithm.py')
