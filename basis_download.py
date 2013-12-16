import urllib2
import simplejson
import datetime

def xstr(s):
    if s is None:
        return ''
    return str(s)

def floatify(s):
    if s is None:
        return ''
    return str("%.6f" % float(s))

def time_fmt(s):
    return datetime.datetime.fromtimestamp(int(s)).strftime('%Y-%m-%d %H:%M:%S')

#These should match your informations
startdate = 'YYYY-MM-DD'
user= '[YOUR USER ID HERE]'

try:
    #Make the request
    req = urllib2.Request('https://app.mybasis.com/api/v1/chart/'+user+'.json?summary=true&interval=60&units=s&start_date='+startdate+'&start_offset=0&end_offset=0&heartrate=true&steps=true&calories=true&gsr=true&skin_temp=true&air_temp=true&bodystates=true')
    opener = urllib2.build_opener()
    f = opener.open(req)

    #Decode the results as json
    results = simplejson.load(f)

    #Basis only provides the start time, all timestamps calculated off this.
    time = int(results['starttime'])

    #Open the file
    file = open('data/basis_'+startdate+'.csv','w')

    #Write the headers
    headers = 'timestamp,heartrate,steps,galvanic,skintemp,airtemp,bodystate\n'
    file.write(headers)

    #Keep track of bodystates to mix into data
    i = 0
    results['bodystates'].reverse()
    cur_range = results['bodystates'][i]

    #Calculate the number of values(minutes) in case the response isnt a full day
    metrics = results['metrics']
    num_minutes = len(metrics['heartrate']['values'])

    for x in range(0,num_minutes-1):
        if time > int(cur_range[1]):
            i += 1
            cur_range = results['bodystates'][i]

        state = xstr(cur_range[2])
        heartrate = xstr(metrics['heartrate']['values'][x])
        steps = xstr(metrics['steps']['values'][x])
        skinresponse = floatify(metrics['gsr']['values'][x])
        skintemp = xstr(metrics['skin_temp']['values'][x])
        airtemp = xstr(metrics['air_temp']['values'][x])

        #Write the csv line. 
        file.write(time_fmt(time) + ',' + heartrate + ',' + steps + ',' + skinresponse + ',' + skintemp + ',' + airtemp + ',' + state +'\n')
        time += 60

    file.close()
except:
    print "There was a problem reading the data. Are you sure your data for the selected day were sync'd?"

