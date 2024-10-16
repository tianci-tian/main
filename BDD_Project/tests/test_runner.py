import os
import subprocess

def run_behave_tests():
    result = subprocess.run(['behave'], cwd=os.path.join(os.path.dirname(__file__), '../features'))

if __name__ == "__main__":
    run_behave_tests()



