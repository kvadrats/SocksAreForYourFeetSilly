PAYMENT_GET = {
    "health": [
        {
            "service": None,  # string
            "status": None,  # string
            "time": None  # string
        }
    ]
}

PAYMENT_POST = {
    "authorised": None  # boolean
}

ORDERS_GET = {
    "_embedded": {
        "customerOrders": [
            {}
        ]
    },
    "_links": {
        "self": {
            "href": None  # STRING
        },
        "profile": {
            "href": None  # STRING
        },
        "search": {
            "href": None  # string
        }
    },
    "page": {
        "size": None,  # integer
        "totalElements": None,  # integer
        "totalPages": None,  # integer
        "number": None  # integer
    }
}

ORDERS_POST = {
    "id": None,  # STRING
    "customerId": None,  # STRING
    "customer": {
        "firstName": None,  # STRING
        "lastName": None,  # STRING
        "username": None,  # STRING
        "addresses": [
            {
                "id": None,  # STRING
                "number": None,  # STRING
                "street": None,  # STRING
                "city": None,  # STRING
                "postcode": None,  # STRING
                "country": None  # STRING
            }
        ],
        "cards": [
            {
                "id": None,  # STRING
                "longNum": None,  # STRING
                "expires": None,  # STRING
                "ccv": None  # STRING
            }
        ]
    },
    "address": {
        "number": None,  # STRING
        "street": None,  # STRING
        "city": None,  # STRING
        "postcode": None,  # STRING
        "country": None  # STRING
    },
    "card": {
        "longNum": None,  # STRING
        "expires": None,  # STRING
        "ccv": None  # STRING
    },
    "items": [
        {
            "id": None,  # STRING
            "itemId": None,  # STRING
            "quantity": None,  # INT
            "unitPrice": None  # INT
        }
    ],
    "shipment": {
        "id": None,  # STRING
        "name": None,  # STRING
    },
    "date": None,  # STRING
    "total": None  # INT
}

# CARTS?

CATALOGUE_GET = [
    {
        "id": None,  # STRING
        "name": None,  # STRING
        "description": None,  # STRING
        "imageUrl": [
            None  # STRING
        ],
        "price": None,  # INT
        "count": None,  # INT
        "tag": [
            None  # STRING
        ]
    }
]

CATALOGUE_GET_SIZE = {
    "size": None  # INT
}

CATALOGUE_GET_TAGS = {
    "tags": []  # list of strings
}

REGISTRATION_FORM = {
    "username": None,
    "password": None,
    "email": None
}

USER_LOGIN = CUSTOMERS = {
    "_embedded": {
        "customer": [
            {
                "firstName": None,  # STRING
                "lastName": None,  # STRING
                "username": None,  # STRING
                "_links": {
                    "self": {
                        "href": None  # STRING
                    },
                    "customer": {
                        "href": None  # STRING
                    },
                    "addresses": {
                        "href": None  # STRING
                    },
                    "cards": {
                        "href": None  # STRING
                    }
                }
            }
        ]
    },
    "_links": {},
    "page": {}
}

USER_POST_REGISTER = USER_CARD = USER_ADDRESS = {
    "id": None  # STRING
}

USER_DELETE_CUSTOMER = USER_DELETE_CARD = USER_DELETE_ADDRESS = {
    "status": None  # BOOLEAN
}

USER_GET_CUSTOMERID = {
    "firstName": None,  # STRING
    "lastName": None,  # STRING
    "username": None,  # STRING
    "_links": {
        "self": {
            "href": None  # STRING
        },
        "customer": {
            "href": None  # STRING
        },
        "addresses": {
            "href": None  # STRING
        },
        "cards": {
            "href": None  # STRING
        }
    }
}

USER_GET_CARDS = {
    "_embedded": {
        "card": [
            {
                "longNum": None,  # STRING
                "expires": None,  # STRING
                "ccv": None,  # STRING
                "_links": {
                    "self": {
                        "href": None  # STRING
                    },
                    "card": {
                        "href": None  # STRING
                    }
                }
            }
        ]
    },
    "_links": {},
    "page": {}
}

USER_GET_ADDRESSES = {
    "_embedded": {
        "address": [
            {
                "number": None,  # STRING
                "street": None,  # STRING
                "city": None,  # STRING
                "postcode": None,  # STRING
                "country": None,  # STRING
                "_links": {
                    "self": {
                        "href": None  # STRING
                    },
                    "address": {
                        "href": None  # STRING
                    }
                }
            }
        ]
    },
    "_links": {},
    "page": {}
}

USER_GET_CARDID = {
    "longNum": None,  # STRING
    "expires": None,  # STRING
    "ccv": None,  # STRING
    "_links": {
        "self": {
            "href": None  # STRING
        },
        "card": {
            "href": None  # STRING
        }
    }
}

USER_GET_ADDRESSID = {
    "number": None,  # STRING
    "street": None,  # STRING
    "city": None,  # STRING
    "postcode": None,  # STRING
    "country": None,  # STRING
    "_links": {
        "self": {
            "href": None  # STRING
        },
        "address": {
            "href": None  # STRING
        }
    }
}
