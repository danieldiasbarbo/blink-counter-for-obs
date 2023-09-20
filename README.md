## Blink counter

### Operating System
- Windows

### Language
- Python


## Creating the Virtual Environment

- Download and install Python:

    [Python 3.11.3](https://www.python.org/downloads/release/python-3113/) - Check ADD TO PATH if you're on a Windows machine

- Run the following command to create a virtual environment named venv:

      python -m venv venv

- Activate the virtual environment using the command:

      .\venv\Scripts\activate

## Installing Dependencies

- Install the dependencies listed in the `requirements.txt` file using the following command:

      pip install -r requirements.txt

## Running the server
- Run the server by executing the following command:

        uvicorn main:app --reload --port 56565
        