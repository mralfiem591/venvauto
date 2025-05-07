import os
import subprocess
import sys

def create_and_install_venv(repo_path, package_names, params=None, create_venv=True, pip_command="install"):
    """
    Creates a virtual environment (optional), activates it, and attempts to install/uninstall packages using pip.

    Args:
        repo_path (str): The path to the repository directory.
        package_names (list): A list of package names to install/uninstall.
        params (list, optional): A list of pip parameters (e.g., ['--no-cache', '--verbose']). Defaults to None.
        create_venv (bool, optional): Whether to create a new virtual environment. Defaults to True.
        pip_command (str, optional): The pip command to use (e.g., 'install', 'uninstall'). Defaults to 'install'.
    """
    if repo_path.endswith(".venv"):
        # If the path ends with .venv, use it as is
        venv_path = os.path.join(repo_path)
    else:
        # Append .venv to the path
        venv_path = os.path.join(repo_path, ".venv")

    # Create the virtual environment if requested
    if create_venv:
        print(f"Creating virtual environment in {venv_path}...")
        try:
            subprocess.run([sys.executable, "-m", "venv", venv_path], check=True, capture_output=True)
            print("Virtual environment created successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error creating virtual environment: {e.stderr.decode()}")
            return  # Stop if venv creation fails
    else:
        print(f"Using existing virtual environment in {venv_path}")

    # Construct the activation command.
    activate_script = ""
    if os.name == 'nt':  # Windows
        activate_script = os.path.join(venv_path, "Scripts", "activate")
    else:  # macOS and Linux
        activate_script = os.path.join(venv_path, "bin", "activate")

    # Install/uninstall the packages
    for package_name in package_names:
        print(f"Attempting to {pip_command} {package_name}...")
        pip_command_list = [os.path.join(venv_path, "bin", "pip"), pip_command]  # *nix
        python_m_pip_command_list = [sys.executable, "-m", "pip", pip_command]

        if os.name == 'nt':
            pip_command_list = [os.path.join(venv_path, "Scripts", "pip"), pip_command]  # windows
            python_m_pip_command_list = [sys.executable, "-m", "pip", pip_command]

        # Add parameters if provided
        if params:
            pip_command_list.extend(params)
            python_m_pip_command_list.extend(params)
        
        #add the package name
        pip_command_list.append(package_name)
        python_m_pip_command_list.append(package_name)

        try:
            subprocess.run(pip_command_list, check=True, capture_output=True)
            print(f"{package_name} {pip_command}ed successfully using pip.")
        except subprocess.CalledProcessError as e:
            print(f"Error {pip_command}ing {package_name} with pip: {e.stderr.decode()}")
            print("Trying with python -m pip...")
            try:
                subprocess.run(python_m_pip_command_list, check=True, capture_output=True)
                print(f"{package_name} {pip_command}ed successfully using python -m pip.")
            except subprocess.CalledProcessError as e2:
                error_message = e2.stderr.decode()
                print(f"Error {pip_command}ing {package_name} with python -m pip: {error_message}")
                print(f"Failed to {pip_command} {package_name}. Please check the error message and try again manually.")
                # Don't return here, continue to the next package
    print("Packages process completed.")



def main():
    """
    Main function to get user input and call the installation function.
    """
    clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
    clear()
    repo_path = input("Enter the path to the repository directory (Will append `.venv` to this, unless it ends in `.venv`): ")
    clear()
    pip_command = input("Enter the pip command to use (e.g., install, uninstall): ").lower()
    clear()
    print(f"LIVE COMMAND: pip {pip_command}")
    params_input = input("Enter any pip parameters (e.g., --no-cache --verbose -r): ")
    params = params_input.split() if params_input else []  # Split params, handle empty input
    clear()
    print(f"LIVE COMMAND: pip {pip_command} {params_input}")
    package_names_input = input("Enter the names of the packages to process (e.g., requests pandas numpy): ")
    package_names = package_names_input.split()  # Split the input string into a list
    clear()
    print(f"LIVE COMMAND: pip {pip_command} {params_input} {package_names_input}")
    create_venv_choice = input("Create a new virtual environment? (y/n): ").lower()
    create_venv = create_venv_choice == "y"
    clear()
    print("LOGS:")
    create_and_install_venv(repo_path, package_names, params, create_venv, pip_command)



if __name__ == "__main__":
    main()