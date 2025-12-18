# description/notes jadikan seperti status

### JSON MEMAKAI COMPACT
```json
[
    {
        "id": 1,
        "f": true,
        "o": "Values of Life",
        "orderers": [
            {
                "id": 1,
                "l": {
                    "id": 1,
                    "k": "Prof. Anjar",
                    "j": 12345678,
                    "g": {
                        "id": 1,
                        "k": "Fakultas Teknik",
                        "a": 1766036390
                    },
                    "a": 1766036390
                },
                "a": 1766036390
            },
            {
                "id": 2,
                "l": {
                    "id": 3,
                    "k": "Prof. Sukiman",
                    "j": 32122244,
                    "g": {
                        "id": 3,
                        "k": "Fakultas Matematika dan Ilmu Pengetahuan Alam (FMIPA)",
                        "a": 1766036390
                    },
                    "a": 1766036390
                },
                "a": 1766036390
            }
        ],
        "status": [
            {
                "id": 1,
                "b": {
                    "id": 1,
                    "k": "Belum"
                },
                "i": 1,
                "a": 1766036390
            },
            {
                "id": 2,
                "b": {
                    "id": 2,
                    "k": "Proses"
                },
                "i": 1,
                "a": 1766036390
            }
        ],
        "flag": [
            {
                "id": 1,
                "f": false,
                "i": 1,
                "a": 1766036390
            },
            {
                "id": 2,
                "f": true,
                "i": 3,
                "a": 1766036390
            }
        ],
        "descriptions": [
            {
                "id": 1,
                "items": [
                    {
                        "id": 1,
                        "z": "testinggggggg",
                        "a": 1766036391
                    },
                    {
                        "id": 2,
                        "z": "aku anak remaja",
                        "a": 1766036391
                    },
                    {
                        "id": 3,
                        "z": "aku anak ibuk",
                        "a": 1766036391
                    },
                    {
                        "id": 4,
                        "z": "aku anak bapak",
                        "a": 1766036391
                    }
                ],
                "i": 1,
                "a": 1766036390
            },
            {
                "id": 2,
                "i": 2,
                "a": 1766036390
            }
        ],
        "notes": [
            {
                "id": 1,
                "items": [
                    {
                        "id": 1,
                        "x": "testinggggggg",
                        "a": 1766036391
                    },
                    {
                        "id": 2,
                        "x": "aku anak remaja",
                        "a": 1766036391
                    },
                    {
                        "id": 3,
                        "x": "aku anak ibuk",
                        "a": 1766036391
                    },
                    {
                        "id": 4,
                        "x": "aku anak bapak",
                        "a": 1766036391
                    }
                ],
                "i": 1,
                "a": 1766036391
            },
            {
                "id": 2,
                "i": 2,
                "a": 1766036391
            }
        ],
        "identification": [
            {
                "id": 1,
                "h": "32123123",
                "n": 1,
                "a": 1766036390
            },
            {
                "id": 2,
                "h": "3212312323",
                "n": 2,
                "a": 1766036390
            }
        ],
        "process": [
            {
                "id": 1,
                "by": [
                    {
                        "id": 1,
                        "q": {
                            "id": 1,
                            "username": "qodri"
                        },
                        "a": 1766036390
                    },
                    {
                        "id": 2,
                        "q": {
                            "id": 2,
                            "username": "sarah"
                        },
                        "a": 1766036390
                    },
                    {
                        "id": 3,
                        "q": {
                            "id": 3,
                            "username": "menik"
                        },
                        "a": 1766036390
                    }
                ],
                "i": 1,
                "a": 1766036390
            },
            {
                "id": 2,
                "i": 2,
                "a": 1766036390
            }
        ],
        "g": {
            "id": 1,
            "k": "Fakultas Teknik",
            "a": 1766036390
        },
        "m": {
            "id": 1,
            "k": "160x250 (buku teks)",
            "a": 1766036390
        },
        "a": 1766036390
    },
    {
        "id": 2,
        "f": true,
        "o": "The Power of Core Values",
        "g": {
            "id": 1,
            "k": "Fakultas Teknik",
            "a": 1766036390
        },
        "m": {
            "id": 2,
            "k": "A5",
            "a": 1766036390
        },
        "a": 1766036390
    }
]
```

### JSON TANPA COMPACT
```json
[
    {
        "id": 1,
        "is_active": true,
        "title": "Values of Life",
        "alias": null,
        "entry_date": null,
        "finish_date": null,
        "orderers": [
            {
                "id": 1,
                "orderer": {
                    "id": 1,
                    "name": "Prof. Anjar",
                    "no": 12345678,
                    "institute": {
                        "id": 1,
                        "name": "Fakultas Teknik",
                        "created_at": 1766039042,
                        "updated_at": null
                    },
                    "created_at": 1766039042,
                    "updated_at": null
                },
                "created_at": 1766039043,
                "updated_at": null
            },
            {
                "id": 2,
                "orderer": {
                    "id": 3,
                    "name": "Prof. Sukiman",
                    "no": 32122244,
                    "institute": {
                        "id": 3,
                        "name": "Fakultas Matematika dan Ilmu Pengetahuan Alam (FMIPA)",
                        "created_at": 1766039042,
                        "updated_at": null
                    },
                    "created_at": 1766039042,
                    "updated_at": null
                },
                "created_at": 1766039043,
                "updated_at": null
            }
        ],
        "status": [
            {
                "id": 1,
                "code": {
                    "id": 1,
                    "name": "Belum"
                },
                "label": {
                    "id": 1,
                    "name": "value1"
                },
                "created_at": 1766039043,
                "updated_at": null
            },
            {
                "id": 2,
                "code": {
                    "id": 2,
                    "name": "Proses"
                },
                "label": {
                    "id": 1,
                    "name": "value1"
                },
                "created_at": 1766039043,
                "updated_at": null
            }
        ],
        "flag": [
            {
                "id": 1,
                "is_active": false,
                "label": {
                    "id": 1,
                    "name": "value1"
                },
                "created_at": 1766039043,
                "updated_at": null
            },
            {
                "id": 2,
                "is_active": true,
                "label": {
                    "id": 3,
                    "name": "value3"
                },
                "created_at": 1766039043,
                "updated_at": null
            }
        ],
        "descriptions": [
            {
                "id": 1,
                "items": [
                    {
                        "id": 1,
                        "text": "testinggggggg",
                        "created_at": 1766039043,
                        "updated_at": null
                    },
                    {
                        "id": 2,
                        "text": "aku anak remaja",
                        "created_at": 1766039043,
                        "updated_at": null
                    },
                    {
                        "id": 3,
                        "text": "aku anak ibuk",
                        "created_at": 1766039043,
                        "updated_at": null
                    },
                    {
                        "id": 4,
                        "text": "aku anak bapak",
                        "created_at": 1766039043,
                        "updated_at": null
                    }
                ],
                "label": {
                    "id": 1,
                    "name": "value1"
                },
                "created_at": 1766039043,
                "updated_at": null
            },
            {
                "id": 2,
                "items": [],
                "label": {
                    "id": 2,
                    "name": "value2"
                },
                "created_at": 1766039043,
                "updated_at": null
            }
        ],
        "notes": [
            {
                "id": 1,
                "items": [
                    {
                        "id": 1,
                        "content": "testinggggggg",
                        "created_at": 1766039043,
                        "updated_at": null
                    },
                    {
                        "id": 2,
                        "content": "aku anak remaja",
                        "created_at": 1766039043,
                        "updated_at": null
                    },
                    {
                        "id": 3,
                        "content": "aku anak ibuk",
                        "created_at": 1766039043,
                        "updated_at": null
                    },
                    {
                        "id": 4,
                        "content": "aku anak bapak",
                        "created_at": 1766039043,
                        "updated_at": null
                    }
                ],
                "label": {
                    "id": 1,
                    "name": "value1"
                },
                "created_at": 1766039043,
                "updated_at": null
            },
            {
                "id": 2,
                "items": [],
                "label": {
                    "id": 2,
                    "name": "value2"
                },
                "created_at": 1766039043,
                "updated_at": null
            }
        ],
        "identification": [
            {
                "id": 1,
                "isbn": "32123123",
                "type": 1,
                "created_at": 1766039043,
                "updated_at": null
            },
            {
                "id": 2,
                "isbn": "3212312323",
                "type": 2,
                "created_at": 1766039043,
                "updated_at": null
            }
        ],
        "process": [
            {
                "id": 1,
                "by": [
                    {
                        "id": 1,
                        "user": {
                            "id": 1,
                            "username": "qodri"
                        },
                        "created_at": 1766039043,
                        "updated_at": null
                    },
                    {
                        "id": 2,
                        "user": {
                            "id": 2,
                            "username": "sarah"
                        },
                        "created_at": 1766039043,
                        "updated_at": null
                    },
                    {
                        "id": 3,
                        "user": {
                            "id": 3,
                            "username": "menik"
                        },
                        "created_at": 1766039043,
                        "updated_at": null
                    }
                ],
                "label": {
                    "id": 1,
                    "name": "value1"
                },
                "created_at": 1766039043,
                "updated_at": null
            },
            {
                "id": 2,
                "by": [],
                "label": {
                    "id": 2,
                    "name": "value2"
                },
                "created_at": 1766039043,
                "updated_at": null
            }
        ],
        "institute": {
            "id": 1,
            "name": "Fakultas Teknik",
            "created_at": 1766039042,
            "updated_at": null
        },
        "size": {
            "id": 1,
            "name": "160x250 (buku teks)",
            "created_at": 1766039043,
            "updated_at": null
        },
        "created_at": 1766039043,
        "updated_at": null
    },
    {
        "id": 2,
        "is_active": true,
        "title": "The Power of Core Values",
        "alias": null,
        "entry_date": null,
        "finish_date": null,
        "orderers": [],
        "status": [],
        "flag": [],
        "descriptions": [],
        "notes": [],
        "identification": [],
        "process": [],
        "institute": {
            "id": 1,
            "name": "Fakultas Teknik",
            "created_at": 1766039042,
            "updated_at": null
        },
        "size": {
            "id": 2,
            "name": "A5",
            "created_at": 1766039043,
            "updated_at": null
        },
        "created_at": 1766039043,
        "updated_at": null
    }
]
```