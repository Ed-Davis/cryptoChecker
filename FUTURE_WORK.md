### Future Possibilities 
## AKA If we want to actually make use of this...)

The interface is very ...er... 'MVP'. How might I want to use this tool? How often do 
I want this info and what am I going to do with it?

#### Interface Options
- Maybe I want a daily email?
- SMS alert for certain conditions (something you might want to 'buy, buy, buy'?)
- Local machine dashboard, surfacing more info? Standalone, or WebApp?
- Would I potentially want this to be part of my own API, essentially doing some ETL to meet my requirements?
- A hosting choice is dependent on the above choices


#### Code Improvements
- Abstract the simple adaptor method so there is a single point where the `requests` library is called, so you could change the dependency with minimal effort if needed (e.g. `urlib2`)
- Add a method that inherits the adaptor method for each RESTful verb needed (extend GET?)
- Make a decision on mocking and strip it out or create a lib of mocked data
- If going with mocked data, make it a parameter with a decision on the default behaviour
- Top3 could itself be a parameter so we could go for the top 5 or just the top changer

