# (py)GetMe

(py)GetMe is a simple python script that will print system information to the console. Similar to neofetch but without the excitement of your OS' logo. **Built and tested on MacOS Sequoia 15.1.**

**NOTE: This (probably) does not work on your linux box. I may extend the script to be compatible with some flavors in the future but don't get your hopes up. This most definitely does not work on your Windows box. Nor will it. I have no intentions of porting this to be Windows compatible.**

This was written to fit my specific needs and may not have the functionality you require. Fork it and move on.

## Installation & Usage

Clone the repository into any directory you'd like. For reference, I keep all my tools in a directory located at `~/MyTools`.

Run the script.

`python3 ~/MyTools/pygetme/main.py`

## Optional

### Make the script directly executable

You can make the `main.py` script executable by setting execution permissions on the file. Enter the following into your terminal.

`chmod a+x ~/MyTools/pygetme/main.py`

**NOTE: This command is the same as running `chmod 755`**

Now you can simply call the script via its path.

`$ ~/MyTools/pygetme/main.py`

**NOTE: If you get some sort of permissions error attempting to `chmod` the file, sudo it and the problem should go away. If you're not allowed to sudo... you're SOL.**

### Set an alias

Typing the full path each time sucks. Let's fix that. Edit your `~/.zshrc` file and append the following:

`alias getme="~/MyTools/pygetme/main.py"`

This assumes you've applied execute permissions to the script. If not, please append the following instead:

`alias getme="python3 ~/MyTools/pygetme/main.py"`

Now you may call the script from anywhere using `getme`. Please make sure you've either reloaded your `~/.zshrc` with the `source` command, or opened a fresh terminal window.
