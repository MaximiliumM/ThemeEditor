# Theme Editor for Twitterrific 6

Twitterrific 6 has support to custom themes by creating new plist files inside its iCloud Drive folder. This Theme Editor helps creating these files and modifying them.

## Getting Started

To get started creating custom themes, I recommend reading through [this awesome guide](https://www.ringgit.me/2019/06/how-to-change-twitterrific-v6-theme.html?m=1) that [@longfy](https://www.twitter.com/longfy) created to understand how Twitterrific's coloring system works.

## Prerequisites

- [Twitterrific 6](https://twitterrific.com/ios)
- [Pythonista](http://omz-software.com/pythonista/)

## Installing

### STEP 1
This editor can be easily installed via one line of python command:

```
import requests as r; exec(r.get('https://raw.githubusercontent.com/MaximiliumM/ThemeEditor/master/install.py').text)
```

Just copy the line above, paste into Pythonista interactive prompt (aka Console) and execute.

### STEP 2

Open Pythonista's side bar, tap **Open...** right below *EXTERNAL FILES*, find Twitterrific's folder and open it. Tap **Select** (if you can't find the Select button, just tap Cancel and open this window again), tap Themes folder and then tap **Open**. Now there should be a Themes folder below *EXTERNAL FILES* in Pythonista. If there is, you're good to go.

## Running

In order to launch the Theme Editor, you have to navigate to the **ThemeEditor-master** folder and run the **mainView.py** script.
I recommend running Pythonista in a Split View side by side with Twitterrific to be able to see changes happening in real time.

## Usage

- Create new themes by pressing the + button.
- Delete themes with swiping to delete gesture.
- *darkWindowStyle* and *thinLineStyle* have no colors. Use the toggle to set its value.
- Three different inputs to set the color: RGB sliders, HSV color picker or HEX color code; Tap the **Set Color** button to commit changes.

## Authors

* **Felipe Manoeli** - [MaximiliumM](https://www.twitter.com/MaximiliumM)

## Acknowledgments

* Hat tip to anyone whose code was used
* [@BigZaphod](https://www.twitter.com/BigZaphod) - Thanks :D
* Thanks [jsbain](https://github.com/jsbain) for the awesome color picker!
* [@longfy](https://www.twitter.com/longfy) - Thanks!
