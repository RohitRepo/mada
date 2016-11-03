from mada.core import get_data, headers

def users_profile_views(start, end, start_view, end_view):
    data = {
        "event_name": "App Launched",
        "from": start,
        "to": end,
        "advanced_query": {
            "did_any": {
                "any_events": [
                    {
                        "event_name": "land on merchant profile_137",
                        "from": start_view,
                        "to": end_view
                    },
                    {
                        "event_name": "land on user profile_137",
                        "from": start_view,
                        "to": end_view
                    },
                    {
                        "event_name": "land on post page_162",
                        "from": start_view,
                        "to": end_view
                    }
                ],
                "operator": "greater_than_equals",
                "value": 1
            }
        }
    }

    return get_data(data)

def new_users_profile_views(start, end, start_view, end_view):
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
                        "event_name": "land on merchant profile_137",
                        "from": start_view,
                        "to": end_view
                    },
                    {
                        "event_name": "land on user profile_137",
                        "from": start_view,
                        "to": end_view
                    },
                    {
                        "event_name": "land on post page_162",
                        "from": start_view,
                        "to": end_view
                    }
                ],
                "operator": "greater_than_equals",
                "value": 1
            }
        }
    }

    return get_data(data)

def new_users_likes(start, end, start_likes, end_likes):
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
                        "event_name": "like_137",
                        "from": start_likes,
                        "to": end_likes
                    },
                ],
                "operator": "greater_than_equals",
                "value": 1
            }
        }
    }

    return get_data(data)

def users_likes(start, end, start_likes, end_likes):
    data = {
        "event_name": "App Launched",
        "from": start,
        "to": end,
        "advanced_query": {
            "did_any": {
                "any_events": [
                    {
                        "event_name": "like_137",
                        "from": start_likes,
                        "to": end_likes
                    },
                ],
                "operator": "greater_than_equals",
                "value": 1
            }
        }
    }

    return get_data(data)

def new_users_shares(start, end, start_likes, end_likes):
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
                        "event_name": "share_162",
                        "from": start_likes,
                        "to": end_likes
                    },
                ],
                "operator": "greater_than_equals",
                "value": 1
            }
        }
    }

    return get_data(data)

def users_shares(start, end, start_likes, end_likes):
    data = {
        "event_name": "App Launched",
        "from": start,
        "to": end,
        "advanced_query": {
            "did_any": {
                "any_events": [
                    {
                        "event_name": "share_162",
                        "from": start_likes,
                        "to": end_likes
                    },
                ],
                "operator": "greater_than_equals",
                "value": 1
            }
        }
    }

    return get_data(data)

def new_users_comments(start, end, start_likes, end_likes):
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
                        "event_name": "comment_137",
                        "from": start_likes,
                        "to": end_likes
                    },
                ],
                "operator": "greater_than_equals",
                "value": 1
            }
        }
    }

    return get_data(data)

def users_comments(start, end, start_likes, end_likes):
    data = {
        "event_name": "App Launched",
        "from": start,
        "to": end,
        "advanced_query": {
            "did_any": {
                "any_events": [
                    {
                        "event_name": "comment_137",
                        "from": start_likes,
                        "to": end_likes
                    },
                ],
                "operator": "greater_than_equals",
                "value": 1
            }
        }
    }

    return get_data(data)

def new_user_profile_views_ret_day(start, end, start_view, end_view, ret_day):
    merchant_segment = set(new_user_merchant_views_ret_day(start, end, start_view, end_view, ret_day))
    user_segment = set(new_user_user_views_ret_day(start, end, start_view, end_view, ret_day))
    post_page_segment = set(new_user_post_page_views_ret_day(start, end, start_view, end_view, ret_day))

    return merchant_segment.union(user_segment).union(post_page_segment)

def new_user_merchant_views_ret_day(start, end, start_view, end_view, ret_day):
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
                    "event_name": "land on merchant profile_137",
                    "from": start_view,
                    "to": end_view
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

def new_user_user_views_ret_day(start, end, start_view, end_view, ret_day):
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
                    "event_name": "land on user profile_137",
                    "from": start_view,
                    "to": end_view
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

def new_user_post_page_views_ret_day(start, end, start_view, end_view, ret_day):
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
                    "event_name": "land on post page_162",
                    "from": start_view,
                    "to": end_view
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