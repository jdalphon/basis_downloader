basis_downloader
================

The Basis B1 is a heath tracking watch that was a successful <a href="www.kickstarter.com">Kickstarter</a> project. It contains sensors for Air/Skin temperature, Galvanic skin resposne, Heart rate, and an extremely good pedometer. More information about basis can be found at www.mybasis.com. This project is somply a python script to download data for a specific date on your MyBasis account.  

<h2>Getting your User ID</h2>
I would like to give a special thanks to <a href="http://www.github.com/btroia">@btroia</a> for figuring out how to get your user id from the mybasis website. His instructions are excellent and can be found <a href="http://www.github.com/btroia/basis-data-export/blob/master/README.md"> HERE </a>

<h2>Running the script</h2>
Make the script executeable. 

*nix ```$ chmod +x basis_download.py```

This script requires simplejson. On my system (ubuntu) this came with python, but on OSX you will need to install it. The easiest way to do so would be to run
OSX ```$ easy_install simplejson```

After that simply run the python script. 
*nix ```$python basis_download.py```

<h2>Notes</h2>
I am not in any way affiliated with www.mybasis.com. They may change their api at any time. I created this project because I needed a way to quickly get data off my Basis to upload to my other project www.isenseproject.org as well as for a friends research. 
