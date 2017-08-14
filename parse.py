#!/Users/joeblue/anaconda/bin/python
import json
import sys
import re
reload(sys)
sys.setdefaultencoding('utf8')
import time
from textblob import TextBlob

 
def clean_tweet(tweet):
  '''
  Utility function to clean tweet text by removing links, special characters
  using simple regex statements.
  '''
  return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

### get tweets from stdout ###
for line in sys.stdin:
   t = json.loads(line)
   name = t['user']['screen_name'].strip('\t')
   ts = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(t['created_at'],'%a %b %d %H:%M:%S +0000 %Y'))
   location = t['user']['location']
   tweet = t['text'].strip('\t').replace('\n', ' ').replace('\r', '')
   analysis = TextBlob(clean_tweet(tweet))
   follow = t['user']['followers_count']
   #print name+'	'+ts+'	'+location+'	'+tweet+'	'+int(follow)+'	'+float(analysis.sentiment.polarity)+'	'+float(analysis.sentiment.subjectivity)
   output = [name,str(ts),str(location),tweet,str(follow),str(analysis.sentiment.polarity),str(analysis.sentiment.subjectivity)]
   print "	".join(output)
   #sys.stdout.write(name,'	',ts,'	',location,'	',tweet,'	',follow,'	',analysis.sentiment.polarity,'	',analysis.sentiment.subjectivity)


