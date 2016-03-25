# Curse client for Mac/Linux/Others

This project was created to download the World of Warcraft addons in an automated way.
Without using curse client \o/

This project can be used to learn basic of [Scrapy Framework](http://scrapy.org/ "Scrapy-Framework") too!

## How i use?

Create an virtualenv (i prefer [virtualenv-wrapper](https://virtualenvwrapper.readthedocs.org/en/latest/ "virtualenv-wrapper")):

```
$ mkvirtualenv curse_spider
```

And install requirements:

```
$ make requirements
```

Then run!

```
$ make run
```

Addons will be on out directory.

## How i search my Addons to download?

On `curse_spider/my_addons.py` you can see the list of my preferred addons (im a rogue :P), add your addons in this file then `make run` again.

## Note

Addons can be downloaded in zip extension, you need extract and copy this addons on `World of Warcraft/Interface/Addons` directory.

## End

Good Game! See you on Azeroth!

Faôlin@Goldrinn or Vanuljin@Goldrinn
