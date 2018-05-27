# pwnduino scripts

This directory contains a lot of the malicious scripts that can be carried out by pwnduino.

## Available Scripts

### `webbrowser.ino`

__TITLE:__ webbrowser.ino

__AUTHOR:__ Alan @ex0dus-0x

__TARGET-OS:__ Windows XP, Windows 7, Windows 8.x, Windows 10

__DEPENDENCIES:__ WebBrowserPassView.exe (stored in deps)

__DESCRIPTION:__ webbrowser.ino is a malicious script that obtains the WebBrowserPassView
to "recover" browser clearview passwords in a Window environment. This is
a quick and efficient hack, as it allows the attacker to steal credentials
just through quick physical access.



## Contribution Guidelines

If you would like to contribute to these, please adhere to the following guidelines when making a pull request:

* Ensure that the script has an `.ino` extension, such that it can be uploaded to an Arduino
* If you have any binary dependencies that the Arduino will be downloading through HTTP, store them in
`deps`.
* Test your code!
* In your script, please include the following as comments in the header:


    TITLE: [your-malicious-script-name.ino]
    AUTHOR: [your-name-here]
    TARGET-OS: [name-of-target-operating-system]
    DEPENDENCIES: [name-of-binaries-in-deps-or-packages-to-be-installed]
    DESCRIPTION: [brief-description-of-hack]

    ...
