# This was changed from the code of Overclock
* I added e-mail notification of new download via a MailerListener added to a EventDispacher
witch allow's me to add new features easily over time. *(Also I wanted to test Python)*

* Details can be seen in the CHANGELOG

## More recent changes listed here:

1. obtain script directory and use that has the working path
2. tvshow_downloader.cfg moved to ./config directory when it's the default file name
3. using the self.conf_file after the variable conf_file is tested
4. using self.conf_file for interactions with the file
5. moved self.parser = parser to inside the try statement
6. **EventDispatcher** and EventListeners file (the last to load the listeners) allows to easy add a funtionality
7. **MailerListener Mailer .py** files to send alert e-mails when a new version is available online

### What the Hell is this?
Maybe you're a guy a bit like me -- who watch a *lot* of series -- so I guess you already know that downloading the latest episodes of all your favorites TV Shows is absolutely PAINFUL. I mean it, really.

Each serie is released always the same day each week ; but obviously it's hard to remember the release day of all your shows (by the way, sometimes they make a little break, so you won't have episode during 2/3 months).

Thus, TVShow Downloader is a set of basic scripts (crontab + python script + bash script) designed
to simplify my whole existence on this earth: I haven't to think about downloading my serie anymore \o/.

# How it works ?
The idea behind this "project" is very, very, (really.) very simple:

* The python script checks if a new episode is released by the eztv team (btw, thank you guys)

    * if a new one is available, the script writes its magnet URI somewhere and add it to the database

    * if the latest released is already in the TVShow Downloader, it does nothing
    
* With a bash script you can add the magnets into your favorite torrent manager (I personaly use transmission, I've planned to fully integrate this one in my script... one day.)

* Last part, the crontab runs the whole process one time per day for example!

Anyway I hope you'll enjoy the thing as much as I do (at least).

##Example sections for Tv Shows:


    [Good Wife, The]
    	hd = False


	[Greys Anatomy]
		hd = False


# Requirements
Currently, it only uses the feedparser library ; you can find it here:
    http://code.google.com/p/feedparser/

NB: Maybe, I will replace the feedparser library by basics python regex
