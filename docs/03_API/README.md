```JSON
{
    "openapi":"3.0.2",
    "info":{
        "title":"FastAPI",
        "version":"0.1.0"
    },
    "paths":{
        "/{hashed_id}":{
            "get":{
                "summary":"Link",
                "operationId":"link__hashed_id__get",
                "parameters":[{
                    "required":true,
                    "schema":{
                        "title":"Hashed Id",
                        "type":"string"
                    },
                    "name":"hashed_id",
                    "in":"path"
                }],
                "responses":{
                    "200":{
                        "description":"Successful Response",
                        "content":{
                            "application/json":{
                                "schema":{}
                            }
                        }
                    },
                    "422":{
                        "description":"Validation Error",
                        "content":{
                            "application/json":{
                                "schema":{
                                    "$ref":"#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/api/exchange":{
            "post":{
                "summary":"Exchange",
                "operationId":"exchange_api_exchange_post",
                "requestBody":{
                    "content":{
                        "application/json":{
                            "schema":{
                                "$ref":"#/components/schemas/ORIGNITEM"
                            }
                        }
                    },
                    "required":true
                },
                "responses":{
                    "200":{
                        "description":"Successful Response",
                        "content":{
                            "application/json":{
                                "schema":{}
                            }
                        }
                    },
                    "422":{
                        "description":"Validation Error",
                        "content":{
                            "application/json":{
                                "schema":{
                                    "$ref":"#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/api/verify":{
            "post":{
                "summary":"Verify",
                "operationId":"verify_api_verify_post",
                "requestBody":{
                    "content":{
                        "application/json":{
                            "schema":{
                                "$ref":"#/components/schemas/ORIGNITEM"
                            }
                        }
                    },
                    "required":true
                },
                "responses":{
                    "200":{
                        "description":"Successful Response",
                        "content":{
                            "application/json":{
                                "schema":{}
                            }
                        }
                    },
                    "422":{
                        "description":"Validation Error",
                        "content":{
                            "application/json":{
                                "schema":{
                                    "$ref":"#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            }
        }
    },
    "components":{
        "schemas":{
            "HTTPValidationError":{
                "title":"HTTPValidationError",
                "type":"object",
                "properties":{
                    "detail":{
                        "title":"Detail",
                        "type":"array",
                        "items":{
                            "$ref":"#/components/schemas/ValidationError"
                        }
                    }
                }
            },
            "ORIGNITEM":{
                "title":"ORIGNITEM",
                "required":["origin_url"],
                "type":"object",
                "properties":{
                    "origin_url":{
                        "title":"Origin Url",
                        "type":"string"
                    }
                }
            },
            "ValidationError":{
                "title":"ValidationError",
                "required":["loc","msg","type"],
                "type":"object",
                "properties":{
                    "loc":{
                        "title":"Location",
                        "type":"array",
                        "items":{
                            "anyOf":[
                                {"type":"string"},
                                {"type":"integer"}
                            ]
                        }
                    },
                    "msg":{
                        "title":"Message",
                        "type":"string"
                    },
                    "type":{
                        "title":"Error Type","type":"string"
                    }
                }
            }
        }
    }
}
```