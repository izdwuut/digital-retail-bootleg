# Digital Retail Bootleg
You are looking at the state of the art, hi-end, mumbo-jumbo tool intended to create bootleg executables containing some sort of a license key, ready to be burned on a disc. I created it with PC games in mind, but I imagine that it would wrap a World of Warcraft... no, according to my knowledge it's a PC game, too. I don't really have much hobbies outside of gaming. I also seriously doubt that there is any external world. At. All. 

Anyhow, I find it useful if you want to gift your friend with a retail copy of the game but the devs have released it on Steam only. Or if you'd like to put your safeword in there - no judging! The possibilities are endless. Just please don't try to break it too much, as I bet that it would inevitably fail to execute. I didn't care much about error handling. 2018, right? Oh, and I have tested it on Windows only. It works for me. 2018, right?

# Usage
For now configuring the script comes down to adjusting some variables contained in `config.ini`. If you are going to put the files on a media, there is also `Autorun.inf` that needs to be tweaked (more on both of them below). I _might_ decide on providing a real-deal installer. Well, maybe not as in _GUI and stuff_, but hopefully a bit more convenient than this. I was shamelessly aiming for an "as easy as it gets" approach.

Please keep in mind that some of the source files have `.dist` extension. It has to be removed first so the script run smoothly.

The `/example` folder is what you are looking for if your goal is to simply reuse the idea. There are a couple of files in there:

* `config.ini` - the aforementioned configuration file. See below for more details.
* `cd-key.txt` - an highly ambiguous file containing - lo and behold - the cd-key to be displayed on the screen (or any text for that matter, really. Just please, don't tell anyone that providing an invalid key was my idea). It also serves as a [fall-back](https://thecodinglove.com/adding-my-final-touch-to-a-gross-quickfix) if something goes wrong with the executable.
* `Autorun.inf` - I believe that it's self-explanatory.

I pre-configured the script to yield this gorgeous outcome:

![My image](https://i.imgur.com/MWl42JH.gif)

# Config
Ok, so here's where the idea gets rad. There are a couple of options that allows you to adjust how the window is drawn. It's virtually all that there is to do: put some keyboard characters in dedicated places! Additionally, here's a handy manual:

### [cd_key]
Everything that has something to do with adjusting how the cd-key is displayed. On the visual side, the options are as follows:

* `path` - the path to a text file containing the cd-key.
* `padding_x` & `padding_y` - text widget padding.
* `border` - text widget border width.
* `bg_color` - text widget border color.
* `label` - a text widget label text. Not displayed if empty.

I also provide options to position the widget quite freely. It can stick to the window edges and corners in (inter)cardinal directions. It can also be positioned absolutely by providing x and y axes offsets.

* `anchor` - anchors the cd-key widget to the window border in one of these pre-defined directions: `N`, `S`, `E`, `W` and `NE`, `SE`, `SW`, `NW`. It can be also set to `CENTER`. You can provide either lowercase or uppercase values, thanks to some intricate Python [wizardry](https://docs.python.org/2/library/stdtypes.html#str.lower). It takes precedence over absolute positioning, hence it's placed higher in the config file. Quite clever, huh?
* `x` and `y` - x and y axes offset (in pixels). It's perfectly okay to set only one of them - it would default the other one to 0.

If none of these was provided, the widget and the corresponding label will be placed in upper left corner, which equals to the `anchor` set to `NW`.

### [bg_image]

* `path` - the path to the window's background file. If you'd like to add some extra text, it's the right place to do this! When none is provided, only the widget with the cd-key will be displayed.  

### [title_bar]
Settings related to the title bar.

* `title` - the window title.
* `icon` - the (fav)icon. It defaults to none, which means that the default tkinter (which I have just fallen in love with!) icon will be used.

# Build

The executable was build with the awesome [PyInstaller](https://www.pyinstaller.org/) using the following command:

`pyinstaller --onefile --hidden-import tkinter --windowed bootleg.py`

Have fun [tkintering](https://docs.python.org/3/library/tk.html) with it!

# License
The script is licensed under a permissive [MIT License](https://github.com/izdwuut/digital-retail-bootleg/blob/master/LICENSE). Please no steal.