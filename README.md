# Theme Editor for Twitterrific 6

Twitterrific 6 has support to custom themes by creating new plist files inside its iCloud Drive folder. This Theme Editor helps creating these files and modifying them.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

- [Twitterrific 6](https://twitterrific.com/ios)
- [Pythonista](http://omz-software.com/pythonista/)

### Installing

This editor can be easily installed via one line of python command:

```
import requests as r; exec(r.get('https://raw.githubusercontent.com/MaximiliumM/ThemeEditor/master/install.py').text)
```

Just copy the line above, paste into Pythonista interactive prompt (aka Console) and execute.

### Running

In order to launch the Theme Editor, you have to navigate to the "ThemeEditor-master" folder and run the "mainView.py" script.
I recommend running Pythonista in a Split View side by side with Twitterrific to be able to see changes happening in real time.

### Usage

- Create new themes by pressing the + button.
- Delete themes with swiping to delete gesture.
- *darkWindowStyle* and *thinLineStyle* have no colors. Use the toggle to set its value.
- Set the color by using the sliders or by inserting the HEX color code in the textfield, then use the ***Set Color*** button to commit changes.

## Authors

* **Felipe Manoeli** - [MaximiliumM](https://www.twitter.com/MaximiliumM)

## Acknowledgments

* Hat tip to anyone whose code was used
* [@BigZaphod](https://www.twitter.com/BigZaphod) - Thanks :D
