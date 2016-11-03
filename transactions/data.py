from mada.core import get_data

def users_started_transaction(start, end, start_txn, end_txn):
    data = {
        "event_name": "App Launched",
        "from": start,
        "to": end,
        "advanced_query": {
            "did_any": {
                "any_events": [
                    {
                        "event_name": "edit picture_137",
                        "from": start_txn,
                        "to": end_txn
                    }
                ],
                "operator": "greater_than_equals",
                "value": 1
            }
        }
    }

    return get_data(data)

def new_users_started_transaction(start, end, start_txn, end_txn):
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
            "did_any": {
                "any_events": [
                    {
                        "event_name": "edit picture_137",
                        "from": start_txn,
                        "to": end_txn
                    }
                ],
                "operator": "greater_than_equals",
                "value": 1
            }
        }
    }

    return get_data(data)

def new_user_started_transaction_ret_day(start, end, start_txn, end_txn, ret_day):
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
                    "event_name": "edit picture_137",
                    "from": start_txn,
                    "to": end_txn
                },
                {
                    "event_name": "App Launched",
                    "from": ret_day,
                    "to": ret_day
                },
            ]
        }
    }

    return get_data(data)

def users_completed_transaction(start, end, start_txn, end_txn):
    data = {
        "event_name": "App Launched",
        "from": start,
        "to": end,
        "advanced_query": {
            "did_any": {
                "any_events": [
                    {
                        "event_name": "submit transaction_137",
                        "from": start_txn,
                        "to": end_txn,
                        "event_properties": [
                            {
                                "name": "submit now_137",
                                "operator": "equals",
                                "value": 1
                            },
                        ]
                    }
                ],
                "operator": "greater_than_equals",
                "value": 1
            }
        }
    }

    return get_data(data)

def new_users_completed_transaction(start, end, start_txn, end_txn):
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
            "did_any": {
                "any_events": [
                    {
                        "event_name": "submit transaction_137",
                        "from": start_txn,
                        "to": end_txn,
                        "event_properties": [
                            {
                                "name": "submit now_137",
                                "operator": "equals",
                                "value": 1
                            },
                        ]
                    }
                ],
                "operator": "greater_than_equals",
                "value": 1
            }
        }
    }

    return get_data(data)

def new_user_completed_transaction_ret_day(start, end, start_txn, end_txn, ret_day):
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
                    "event_name": "submit transaction_137",
                    "from": start_txn,
                    "to": end_txn,
                    "event_properties": [
                        {
                            "name": "submit now_137",
                            "operator": "equals",
                            "value": "1"
                        }
                    ]
                },
                {
                    "event_name": "App Launched",
                    "from": ret_day,
                    "to": ret_day
                },
            ]
        }
    }

    return get_data(data)