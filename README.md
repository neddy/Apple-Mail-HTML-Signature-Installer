**As of 10.12 you no longer need this script to install an html signature, just copy and paste it in**

# Apple Mail HTML Signature Installer

A simple script written in Python to install HTML signatures in Apple Mail. There are two Python files, 'signature_installer.py' can be used in the command line, and 'signature_installer_automator' is the Python code used in the Automator app. There is also an Automator App included, this is simply an Automator app that asks for your HTML signature file and passes it to the Python script to install it.

## Warning!

Use at your own risk, it works fine on my system (Macos Sierra), but I'm very new to coding and I take no responsibility for anything that goes wrong on your system...

## Using it

First, you'll need an html file that you have created or been given. If you don't have this, you will need to figure that out first(Google...).

Once you have your HTML signature ready you'll need to follow a couple steps to get it installed.

Before you use the app, you need to create a blank signature in Apple Mail for the script to overwrite. To do this, open Apple Mail, go to Mail Preferences and then locate the 'Signatures' tab. Select the mail account on the left that you would like to add the signature to and then add a signature with the '+' button. After that, you don't need to do anything else, just leave the default information that it's populated with and make sure you 'Quit' Mail.

Next, either use teh automator app or python script...

To use the Automator app, simply double click the app and select your HTML signature file. That's it.

On the command line, it can be used with the '-i' option to pass you HTML file to the script as follows
```
python ./signature_installer.py -i signature_file.html
```

## Contributing

If anyone would like to improve it please go ahead, I'm not much of a coding guru...

Even better, if anyone has any idea how to use Kivy to make the app as opposed to Automator that would be great. I couldn't figure out how to get it going at all...


## License

This project is licensed under the MIT License.

## Acknowledgments

Lot's of Googling and tutorials have all been melded to get to where we are now.

## Issues or Suggestions

Feel free to submit an issues on GitHub if you have any trouble, or any suggestions.
