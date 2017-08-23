# Sarahah Spam Bot

With this script, you can spam any user on Sarahah with a message of your choice.

### Compatibility

Python 2 or 3+

### Requirements

Requires a proxy to work successfully. I do not include any proxies with the script, so you will have to obtain these on your own from a third-party.

Once you obtain a proxy, fill in the proxy info in `proxies.json` then save the file.

### Installation and Usage

1. Install Python
    - Easiest way is to download and run the installer from the official  [Python](https://python.org) website. Please tick the box to add Python to your environment variables.

        If you don't tick the box, add Python to your PATH environment manually. Watch [this](https://youtu.be/Y2q_b4ugPWk) video if you need help with that.

3. Open Terminal on Mac or CMD on Windows

4. Run the following command to install the dependencies:

**Python 2**

```
pip install requests
```

**Python 3**

```
pip3 install requests
```

5. Run the script like this

**Python 2**

```
python SarahahBot.py URL OPTION COUNT
```

**Python 3**

```
python3 SarahahBot.py USERNAME TEXT COUNT
```

**EXAMPLE**
```
python SarahahBot.py croc "please dont spam me" 10
```

**KEY**
- USERNAME - the user you want to spam
- TEXT - the text you want to spam in quotation marks
- COUNT - the number of times you want to spam it