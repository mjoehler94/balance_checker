# Balance Checker

##Description
> I work remotely for the most part, but on days where I go to the office I usually take public transit (UTA Frontrunner). 
To help me keep track of the balance on my public transit card, I wrote this code to scrape my card balance from 
the UTA website, and then send me updates via slack.

## Sample Output
![example](img/message_example.jpg) 

## Basic Instructions
- set up a virtual environment and install required packages with `pip install -r requirements.txt`
    - (on windows you can run the included `deploy.bat` file to do this for you)
- make sure that your credentials are stored in `secrets.py` 
    - the `secrets.py` file will excluded per the `.gitignore`
    - follow the pattern shown by `secrets_template.py`
- make sure you have the correct `chromedriver.exe` file included in the `driver` directory
    - the included file works for chrome version 94
    - other versions can be found [here](https://chromedriver.chromium.org/downloads)
- to run the code:
    - activate the virtual environment and run python `main.py`
    - if using windows, this can be done by executing the `run.bat` script (which can also be addd to task schedulers quite nicely)