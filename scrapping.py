import twint
c = twint.Config()
c.Search = ['dehumanisation'] # topic
c.Limit = 500 # number of Tweets to scrape
c.Store_csv = True # store tweets in a csv file
c.Output = 'data/dehumanisation.csv' # path to csv file
twint.run.Search(c)