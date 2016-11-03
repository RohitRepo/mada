import ast
import requests
import json
import operator

headers = {
    "X-CleverTap-Account-Id": "R57-6RW-844Z",
    "X-CleverTap-Passcode": "ETQ-SSE-CAAL",
    "Content-Type": "application/json"
}

def get_cursor(payload):
    req = requests.post(
        'https://api.clevertap.com/1/events.json?batch_size=5000', 
        headers=headers,
        data=json.dumps(payload)
    )

    response = ast.literal_eval(req.content)
    print response
    cursor = response['cursor']
    return cursor

def get_page_events(cursor):
    print "Requesting events for cursor: " + cursor
    result = []
    
    req = requests.get('https://api.clevertap.com/1/events.json?cursor=' + cursor, headers=headers)
    response = ast.literal_eval(req.content)

    if 'records' in response:
        result = response['records']
        print "Got total response: " + str(len(result))

        if len(result) < 5000:
            return result

        result = result + get_page_events(response['next_cursor'])
        return result
    

    print "Got no records"
    return []

def get_data(payload):
    records = get_records(payload)
    return get_unique_people(records)

def get_records(payload):
    cursor = get_cursor(payload)
    records = get_page_events(cursor)

    print "Got final records: " + str(len(records))

    return records

def get_unique_people(records):
    identities = []

    # for record in records:
    #     record_identities = record['profile']['identity']
    #     record_identities = record_identities[1:-1]
    #     for identity in record_identities.split():
    #         if "@" not in identity:
    #             identities.append(identity)
    #             break

    identities = [record['profile']['email'] for record in records if 'email' in record['profile']]
    identities_set = set(identities)
    return list(identities_set)

def get_segment_events(emails):
    result = {}
    counter = 1
    completion = 0

    for email in emails:
        req = requests.get('https://api.clevertap.com/1/profile.json?email='+email, headers=headers)
        response = ast.literal_eval(req.content)['record']
        events = response['events']

        for event in events:
            if event in result:
                result[event] = result[event] + events[event]['count']
            else:
                result[event] = events[event]['count']

        if (counter*100)/len(emails) > completion:
            completion = (counter*100)/len(emails)
            print str(completion) + "%"

        counter += 1

    sorted_result = sorted(result.items(), key=operator.itemgetter(1))
    return sorted_result

def new_users(start, end):

    data = {
        "event_name": "App Launched",
        "from": start,
        "to": end,
        "session_properties": [
            {
                "name": "first_time",
                "value": "True"
            },
        ],

    }

    return get_data(data)

def active_users(start, end):

    data = {
        "event_name": "App Launched",
        "from": start,
        "to": end,

    }

    return get_data(data)

def new_users_ret_day(start, end, date_ret):

    data = {
        "event_name": "App Launched",
        "from": start,
        "to": end,
        "session_properties": [
            {
                "name": "first_time",
                "value": "True"
            }],
        "advanced_query": {
        "did_any": {
            "any_events": [
                {
                    "event_name": "App Launched",
                    "from": date_ret,
                    "to": date_ret
                },
            ],
            "operator": "greater_than_equals",
            "value": 1
        }
        }
        ,

    }

    return get_data(data)

# segment = new_users_ret_day(20160413, 20160713, 20160718)
# records = get_unique_people(segment)

# print "Unique people: " + str(len(records))
# result = get_segment_events(segment)
# print "Event distribution: "
# print result