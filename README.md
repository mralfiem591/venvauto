# Virtual Environment Manager

This Python script automates the creation and management of virtual environments, as well as the installation or uninstallation of Python packages using `pip`.

## Features

- Creates a new virtual environment or uses an existing one.
- Activates the virtual environment.
- Installs or uninstalls Python packages with optional pip parameters.
- Supports both Windows and Unix-based systems.

## Requirements

- Python 3.x installed on your system.
- `pip` must be available in your Python installation.

## How to Use

1. Clone or download this repository to your local machine.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script using Python:

    ```bash
        python main.py
    ```

4. Follow the prompts:
   - Enter the path to the repository directory.
   - Specify the pip command (`install` or `uninstall`).
   - Provide any additional pip parameters (optional).
   - List the package names to process.
   - Choose whether to create a new virtual environment or use an existing one.

## Example

```bash
Enter the path to the repository directory (Will append `.venv` to this, unless it ends in `.venv`): /path/to/repo
Enter the pip command to use (e.g., install, uninstall): install
Enter any pip parameters (e.g., --no-cache --verbose): --no-cache
Enter the names of the packages to process (e.g., requests pandas numpy): requests pandas
Create a new virtual environment? (y/n): y
```

## Logs

The script will display logs for each step, including:

- Virtual environment creation.
- Activation commands.
- Package installation/uninstallation status.

## Notes

- On Windows, the script uses `Scripts\activate` to activate the virtual environment.
- On Unix-based systems, it uses `bin/activate`.
- If a package installation fails with `pip`, the script will attempt to use `python -m pip`.

## Troubleshooting

- Ensure the provided repository path is valid.
- Check for Python and pip installation issues if errors occur.
- Review the error messages in the logs for more details.

## License

This project is licensed under the MIT License.
