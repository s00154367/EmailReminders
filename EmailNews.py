from idna import unicode
from newsapi import NewsApiClient
import json
from datetime import date, timedelta
import smtplib, ssl
#from django.utils.encoding import smart_str, smart_unicode


newsapi = NewsApiClient(api_key='94454bdacf3247a2957f23c8de7f597f')

todaydate = date.today()
yestdate = todaydate - timedelta(days=1)

# Top Tech headlines
tech_headlines = newsapi.get_top_headlines(sources='mashable,techcrunch.com')

# Top Irish headlines    

irish_headlines = newsapi.get_top_headlines(country='ie')

#  Top World headlines



#all_articles = newsapi.get_top_headlines(q='bitcoin',
 #                                     sources='bbc-news,the-verge',
  #                                     domains= 'bbc.co.uk,techcrunch.com',
   #                                    from_param='2017-12-01',
    #                                   to='2017-12-12',
     #                                  language='en',
      #                                 sort_by='relevancy',
       #                                page=2)
  #sources = newsapi.get_sources()

#news = json.loads(top_headlines)
emailstr = ""





########  Irish Headlines
emailstr += "Irish Headlines - "
emailstr += str(irish_headlines['totalResults'])
emailstr += " Stories\r\n\r\n"
for items in irish_headlines:
    if(items == 'articles'):
        for articles in irish_headlines[items]:
            #print(articles)
            #if (articles == 'source'):
                #for source in articles:
                    #emailstr += source['name']
            emailstr += articles['title']
            emailstr += "\r\n\r\n"
            emailstr += articles['content']
            emailstr += "\r\n"
            emailstr += articles['url']
            emailstr += "\r\n___________________________________________________________________________________\r\n"






########  Tech Headlines
emailstr += "======================================================================================\r\n\r\n"
emailstr += "Tech Headlines - "
emailstr += str(tech_headlines['totalResults'])
emailstr += " Stories\r\n\r\n"
for items in tech_headlines:
     #print(items)
     if(items == 'articles'):
         for articles in tech_headlines[items]:
             #print(articles)

             emailstr += articles['title']
             emailstr += "\r\n"
             emailstr += articles['content']
             emailstr += "\r\n"
             emailstr += articles['url']
             emailstr += "\r\n_______________________________\r\n"



#print(emailstr)
#print(json.dumps(irish_headlines, indent = 4))

sender_email = ""
receiver_email = ""
message = """\
Subject: News Headlines 

"""

message += emailstr
#message.encode("ascii", errors="ignore")
#rest_array = [text.encode("utf8") for text in message]

port = 587  # For starttls
context = ssl.create_default_context()
with smtplib.SMTP("smtp.gmail.com", port) as server:
     server.ehlo()  # Can be omitted
     server.starttls(context=context)
     server.ehlo()  # Can be omitted
     server.login(sender_email, "") #Input PW
     server.sendmail(sender_email, receiver_email, message.encode("utf-8"))

