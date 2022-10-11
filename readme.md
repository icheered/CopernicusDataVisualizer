# Visualize data

- Install python3 (brew)
- Install poetry (https://python-poetry.org/)

Poetry is a virtual environment manager.
We need to install some dependencies (libraries), but we don't want to install it directly into our system. If in the future in a different project we need the same library as a previous project, you run the risk of updating the package which might break the previous project. A virtual environment is a container that holds the dependencies for a single project at a specific version.

- In this folder, execute command `$ poetry install` to download an install dependencies in the virtual environment
- Then run `$ poetry shell` to enter the virtual environment

Then to start the program, run `$ python main.py` from the terminal.
