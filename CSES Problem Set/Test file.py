import subprocess
import os
import zipfile
import tempfile
import shutil

def run_tests_from_zip(zip_path, script_path):
    # Create a temporary directory to extract files
    with tempfile.TemporaryDirectory() as temp_dir:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)

        test_files = sorted(f for f in os.listdir(temp_dir) if f.endswith('.in'))

        for test_file in test_files:
            test_number = test_file.split('.')[0]
            input_path = os.path.join(temp_dir, f'{test_number}.in')
            output_path = os.path.join(temp_dir, f'{test_number}.out')

            if not os.path.exists(output_path):
                print(f"test#{test_number} : Missing output file")
                continue

            with open(input_path, 'r') as f:
                input_data = f.read()

            with open(output_path, 'r') as f:
                expected_output = f.read().strip().splitlines()

            # Run the script
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
run_tests_from_zip(zip_path='tests (5).zip', script_path='Creating Strings.py')
