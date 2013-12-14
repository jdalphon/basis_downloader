import urllib2
import simplejson

def xstr(s):
    if s is None:
        return ''
    return str(s)

def floatify(s):
    if s is None:
        return ''
    return str("%.6f" % float(s))

startdate = '[YYYY-MM-DD]'
user= '[YOUR USER ID HERE]'
req = urllib2.Request('https://app.mybasis.com/api/v1/chart/'+user+'.json?summary=true&interval=60&units=s&start_date='+startdate+'&start_offset=0&end_offset=0&heartrate=true&steps=true&calories=true&gsr=true&skin_temp=true&air_temp=true&bodystates=true')
opener = urllib2.build_opener()
f = opener.open(req)
results = simplejson.load(f)

headers = 'timestamp,heartrate,steps,galvanic,skintemp,airtemp\n'

time = int(results['starttime'])

file = open('data/basis_'+startdate+'.csv','w')
file.write(headers)

for x in range(0,1439):
    heartrate = xstr(results['metrics']['heartrate']['values'][x])
    steps = xstr(results['metrics']['steps']['values'][x])
    skinresponse = floatify(results['metrics']['gsr']['values'][x])
    skintemp = xstr(results['metrics']['skin_temp']['values'][x])
    airtemp = xstr(results['metrics']['air_temp']['values'][x])
    file.write(str(time) + ',' + heartrate + ',' + steps + ',' + skinresponse + ',' + skintemp + ',' + airtemp + '\n')
    time += 60

file.close()


