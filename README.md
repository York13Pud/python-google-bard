# Google Bard AI Experiments

This repository contains some of my experiments that I put together using Google's Bard AI.

## Instructions

1. Sign-up at [https://bard.google.com]("https://bard.google.com"). 
2. Once that is done, you will then need to get the value of the `__Secure-1PSID` from your web browser. This is done by pressing `F12` on your keyboard and then going to the Storage tab and then going to `https://bard.google.com`.
3. Open Apple KeyChain access and then create a new password in the Login keychain. I called mine `Google Bard` with a username of `Google Bard`. The user name is not required for Bard to work but it is needed for keyring to work.
4. Open a terminal and 
5. Create a new folder for the project.
6. Create a new Python virtual environment and activate it.
7. Install the following python libraries: `pip install bardapi keyring`
8. Run the `main.py` file in a terminal.

You can modify the question that is sent to Bard by opening the `main.py` file and changing the text in the request variable.

The response will be output to the screen using the value of the `content` key that is returned from Google Bard.