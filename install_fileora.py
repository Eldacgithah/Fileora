import os
import subprocess
import sys
import tempfile
import shutil

GIT_REPO = "https://github.com/Eldacgithah/Fileora.git"

def run_command(cmd, cwd=None):
    process = subprocess.Popen(cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    for line in process.stdout:
        print(line.strip())
    for line in process.stderr:
        print(line.strip(), file=sys.stderr)
    process.wait()
    if process.returncode != 0:
        print(f"Command failed: {cmd}")
        sys.exit(1)

def main():
    cwd = os.getcwd()
    project_dir = os.path.join(cwd, "Fileora_temp")
    if os.path.exists(project_dir):
        shutil.rmtree(project_dir)
    run_command(["git", "clone", GIT_REPO, project_dir])
    os.chdir(project_dir)
    run_command([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    run_command([sys.executable, "-m", "pip", "install", "."])
    hidden_dir = os.path.join(tempfile.gettempdir(), ".fileora_hidden")
    if os.path.exists(hidden_dir):
        shutil.rmtree(hidden_dir)
    shutil.move(project_dir, hidden_dir)
    print("Installation complete. The project folder has been moved to a hidden location.")
    print("You can now use the command 'fileora' from anywhere.")

if __name__ == "__main__":
    main()
