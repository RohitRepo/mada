from mada.core import get_data

def users_total_notifications(start, end, start_not, end_not):
    data = {
        "event_name": "App Launched",
        "from": start,
        "to": end,
        "advanced_query": {
            "did_all": [
                {
                    "event_name": "notification_137",
                    "from": start_not,
                    "to": end_not
                }
            ]
        }
    }

    return get_data(data)

def new_users_total_notifications(start, end, start_not, end_not):
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
        "advanced_query": {
            "did_all": [
                {
                    "event_name": "notification_137",
                    "from": start_not,
                    "to": end_not
                }
            ]
        }
    }

    return get_data(data)

def new_users_accepted_notifications(start, end, start_not, end_not):
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
        "advanced_query": {
            "did_all": [
                {
                    "event_name": "notification_137",
                    "from": start_not,
                    "to": end_not,
                    "event_properties": [ 
                        {
                            "name": "notification click_137",
                            "operator": "equals",
                            "value": 1
                        }
                    ]
                }
            ]
        }
    }

    return get_data(data)

def users_accepted_notifications(start, end, start_not, end_not):
    data = {
        "event_name": "App Launched",
        "from": start,
        "to": end,
        "advanced_query": {
            "did_all": [
                {
                    "event_name": "notification_137",
                    "from": start_not,
                    "to": end_not,
                    "event_properties": [ 
                        {
                            "name": "notification click_137",
                            "operator": "equals",
                            "value": 1
                        }
                    ]
                }
            ]
        }
    }

    return get_data(data)

def new_users_rejected_notifications(start, end, start_not, end_not):
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
        "advanced_query": {
            "did_all": [
                {
                    "event_name": "notification_137",
                    "from": start_not,
                    "to": end_not,
                    "event_properties": [ 
                        {
                            "name": "notification click_137",
                            "operator": "equals",
                            "value": 0
                        }
                    ]
                }
            ]
        }
    }

    return get_data(data)

def users_rejected_notifications(start, end, start_not, end_not):
    data = {
        "event_name": "App Launched",
        "from": start,
        "to": end,
        "advanced_query": {
            "did_all": [
                {
                    "event_name": "notification_137",
                    "from": start_not,
                    "to": end_not,
                    "event_properties": [ 
                        {
                            "name": "notification click_137",
                            "operator": "equals",
                            "value": 0
                        }
                    ]
                }
            ]
        }
    }

    return get_data(data)

def new_users_social_notifications(start, end, start_not, end_not):
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
        "advanced_query": {
            "did_all": [
                {
                    "event_name": "notification_137",
                    "from": start_not,
                    "to": end_not,
                    "event_properties": [
                        {
                            "name": "notification deeplink",
                            "operator": "contains",
                            "value": "postTransaction,userprofile,profileuser,profilemerchant"
                        }
                    ]
                }
            ]
        }
    }

    return get_data(data)

def users_social_notifications(start, end, start_not, end_not):
    data = {
        "event_name": "App Launched",
        "from": start,
        "to": end,
        "advanced_query": {
            "did_all": [
                {
                    "event_name": "notification_137",
                    "from": start_not,
                    "to": end_not,
                    "event_properties": [
                        {
                            "name": "notification deeplink",
                            "operator": "contains",
                            "value": "postTransaction,userprofile,profileuser,profilemerchant"
                        }
                    ]
                }
            ]
        }
    }

    return get_data(data)

def new_users_accepted_social_notifications(start, end, start_not, end_not):
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
        "advanced_query": {
            "did_all": [
                {
                    "event_name": "notification_137",
                    "from": start_not,
                    "to": end_not,
                    "event_properties": [
                        {
                            "name": "notification click_137",
                            "operator": "equals",
                            "value": 1
                        },
                        {
                            "name": "notification deeplink",
                            "operator": "contains",
                            "value": "postTransaction,userprofile,profileuser,profilemerchant"
                        }
                    ]
                }
            ]
        }
    }

    return get_data(data)

def users_accepted_social_notifications(start, end, start_not, end_not):
    data = {
        "event_name": "App Launched",
        "from": start,
        "to": end,
        "advanced_query": {
            "did_all": [
                {
                    "event_name": "notification_137",
                    "from": start_not,
                    "to": end_not,
                    "event_properties": [
                        {
                            "name": "notification click_137",
                            "operator": "equals",
                            "value": 1
                        },
                        {
                            "name": "notification deeplink",
                            "operator": "contains",
                            "value": "postTransaction,userprofile,profileuser,profilemerchant"
                        }
                    ]
                }
            ]
        }
    }

    return get_data(data)

def new_users_rejected_social_notifications(start, end, start_not, end_not):
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
        "advanced_query": {
            "did_all": [
                {
                    "event_name": "notification_137",
                    "from": start_not,
                    "to": end_not,
                    "event_properties": [
                        {
                            "name": "notification click_137",
                            "operator": "equals",
                            "value": 0
                        },
                        {
                            "name": "notification deeplink",
                            "operator": "contains",
                            "value": "postTransaction,userprofile,profileuser,profilemerchant"
                        }
                    ]
                }
            ]
        }
    }

    return get_data(data)

def users_rejected_social_notifications(start, end, start_not, end_not):
    data = {
        "event_name": "App Launched",
        "from": start,
        "to": end,
        "advanced_query": {
            "did_all": [
                {
                    "event_name": "notification_137",
                    "from": start_not,
                    "to": end_not,
                    "event_properties": [
                        {
                            "name": "notification click_137",
                            "operator": "equals",
                            "value": 0
                        },
                        {
                            "name": "notification deeplink",
                            "operator": "contains",
                            "value": "postTransaction,userprofile,profileuser,profilemerchant"
                        }
                    ]
                }
            ]
        }
    }

    return get_data(data)

def new_users_commerce_notifications(start, end, start_not, end_not):
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
        "advanced_query": {
            "did_all": [
                {
                    "event_name": "notification_137",
                    "from": start_not,
                    "to": end_not,
                    "event_properties": [
                        {
                            "name": "notification deeplink",
                            "operator": "contains",
                            "value": "deal,search,wallet,notification"
                        }
                    ]
                }
            ]
        }
    }

    return get_data(data)

def users_commerce_notifications(start, end, start_not, end_not):
    data = {
        "event_name": "App Launched",
        "from": start,
        "to": end,
        "advanced_query": {
            "did_all": [
                {
                    "event_name": "notification_137",
                    "from": start_not,
                    "to": end_not,
                    "event_properties": [
                        {
                            "name": "notification deeplink",
                            "operator": "contains",
                            "value": "deal,search,wallet,notification"
                        }
                    ]
                }
            ]
        }
    }

    return get_data(data)

def new_users_accepted_commerce_notifications(start, end, start_not, end_not):
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
        "advanced_query": {
            "did_all": [
                {
                    "event_name": "notification_137",
                    "from": start_not,
                    "to": end_not,
                    "event_properties": [
                        {
                            "name": "notification click_137",
                            "operator": "equals",
                            "value": 1
                        },
                        {
                            "name": "notification deeplink",
                            "operator": "contains",
                            "value": "deal,search,wallet,notification"
                        }
                    ]
                }
            ]
        }
    }

    return get_data(data)

def users_accepted_commerce_notifications(start, end, start_not, end_not):
    data = {
        "event_name": "App Launched",
        "from": start,
        "to": end,
        "advanced_query": {
            "did_all": [
                {
                    "event_name": "notification_137",
                    "from": start_not,
                    "to": end_not,
                    "event_properties": [
                        {
                            "name": "notification click_137",
                            "operator": "equals",
                            "value": 1
                        },
                        {
                            "name": "notification deeplink",
                            "operator": "contains",
                            "value": "deal,search,wallet,notification"
                        }
                    ]
                }
            ]
        }
    }

    return get_data(data)

def new_users_rejected_commerce_notifications(start, end, start_not, end_not):
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
        "advanced_query": {
            "did_all": [
                {
                    "event_name": "notification_137",
                    "from": start_not,
                    "to": end_not,
                    "event_properties": [
                        {
                            "name": "notification click_137",
                            "operator": "equals",
                            "value": 0
                        },
                        {
                            "name": "notification deeplink",
                            "operator": "contains",
                            "value": "deal,search,wallet,notification"
                        }
                    ]
                }
            ]
        }
    }

    return get_data(data)

def users_rejected_commerce_notifications(start, end, start_not, end_not):
    data = {
        "event_name": "App Launched",
        "from": start,
        "to": end,
        "advanced_query": {
            "did_all": [
                {
                    "event_name": "notification_137",
                    "from": start_not,
                    "to": end_not,
                    "event_properties": [
                        {
                            "name": "notification click_137",
                            "operator": "equals",
                            "value": 0
                        },
                        {
                            "name": "notification deeplink",
                            "operator": "contains",
                            "value": "deal,search,wallet,notification"
                        }
                    ]
                }
            ]
        }
    }

    return get_data(data)
