A web scraper and analysis tool I built for Dota 2 using Steam's Web API, to detect some trends and possible toxic behavior.
This is no means represents how Valve does their analysis, just my take on it. I have replaced my own steam api key with the
string "ENTER_YOUR_KEY", and thus to use this code you will need to replace that string with your own 32-bit key, which you
can get from Valve if you have a steam account. Note that it will allow your to only make a limited number of calls to the
API per day, plus only a certain number of calls every second, hence the sleep statements. If you intend to use this code
please make sure you double-check the limits on the API's documentation and adhere to it, or your key may be banned from
making any more calls.