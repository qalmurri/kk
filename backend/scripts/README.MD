# description/notes jadikan seperti status

### JSON MEMAKAI COMPACT
```json
[
    {
        "id": 1,
        "i": true,
        "e": "Values of Life",
        "orderers": [
            {
                "id": 1,
                "o": {
                    "id": 1,
                    "n": "Prof. Anjar",
                    "m": 12345678,
                    "j": {
                        "id": 1,
                        "n": "Fakultas Teknik",
                        "a": 1766068160
                    },
                    "a": 1766068160
                },
                "a": 1766068160
            },
            {
                "id": 2,
                "o": {
                    "id": 3,
                    "n": "Prof. Sukiman",
                    "m": 32122244,
                    "j": {
                        "id": 3,
                        "n": "Fakultas Matematika dan Ilmu Pengetahuan Alam (FMIPA)",
                        "a": 1766068160
                    },
                    "a": 1766068160
                },
                "a": 1766068160
            }
        ],
        "status": [
            {
                "id": 1,
                "l": {
                    "id": 1,
                    "n": "Layouter"
                },
                "h": {
                    "id": 1,
                    "n": "Belum"
                },
                "a": 1766068160
            },
            {
                "id": 2,
                "l": {
                    "id": 2,
                    "n": "Desainer"
                },
                "h": {
                    "id": 2,
                    "n": "Proses"
                },
                "a": 1766068160
            },
            {
                "id": 3,
                "l": {
                    "id": 3,
                    "n": "ISBN"
                },
                "h": {
                    "id": 4,
                    "n": "Sudah"
                },
                "a": 1766068160
            }
        ],
        "flag": [
            {
                "id": 1,
                "i": false,
                "l": {
                    "id": 1,
                    "n": "Layouter"
                },
                "a": 1766068160
            },
            {
                "id": 2,
                "i": true,
                "l": {
                    "id": 3,
                    "n": "ISBN"
                },
                "a": 1766068160
            }
        ],
        "descriptions": [
            {
                "id": 1,
                "items": [
                    {
                        "id": 1,
                        "c": "testinggggggg",
                        "a": 1766068160
                    },
                    {
                        "id": 2,
                        "c": "aku anak remaja",
                        "a": 1766068160
                    },
                    {
                        "id": 3,
                        "c": "aku anak ibuk",
                        "a": 1766068160
                    },
                    {
                        "id": 4,
                        "c": "aku anak bapak",
                        "a": 1766068160
                    }
                ],
                "l": {
                    "id": 1,
                    "n": "Layouter"
                },
                "a": 1766068160
            },
            {
                "id": 2,
                "l": {
                    "id": 2,
                    "n": "Desainer"
                },
                "a": 1766068160
            }
        ],
        "notes": [
            {
                "id": 1,
                "items": [
                    {
                        "id": 1,
                        "d": "testinggggggg",
                        "a": 1766068160
                    },
                    {
                        "id": 2,
                        "d": "aku anak remaja",
                        "a": 1766068160
                    },
                    {
                        "id": 3,
                        "d": "aku anak ibuk",
                        "a": 1766068160
                    },
                    {
                        "id": 4,
                        "d": "aku anak bapak",
                        "a": 1766068160
                    }
                ],
                "l": {
                    "id": 1,
                    "n": "Layouter"
                },
                "a": 1766068160
            },
            {
                "id": 2,
                "l": {
                    "id": 2,
                    "n": "Desainer"
                },
                "a": 1766068160
            }
        ],
        "identification": [
            {
                "id": 1,
                "k": "32123123",
                "q": {
                    "id": 1,
                    "n": "ISBN"
                },
                "a": 1766068160
            },
            {
                "id": 2,
                "k": "3212312323",
                "q": {
                    "id": 2,
                    "n": "E-ISBN"
                },
                "a": 1766068160
            }
        ],
        "process": [
            {
                "id": 1,
                "by": [
                    {
                        "id": 1,
                        "r": {
                            "id": 1,
                            "username": "qodri"
                        },
                        "a": 1766068160
                    },
                    {
                        "id": 2,
                        "r": {
                            "id": 2,
                            "username": "sarah"
                        },
                        "a": 1766068160
                    },
                    {
                        "id": 3,
                        "r": {
                            "id": 3,
                            "username": "menik"
                        },
                        "a": 1766068160
                    }
                ],
                "l": {
                    "id": 1,
                    "n": "Layouter"
                },
                "a": 1766068160
            },
            {
                "id": 2,
                "l": {
                    "id": 2,
                    "n": "Desainer"
                },
                "a": 1766068160
            }
        ],
        "cover": [
            {
                "id": 1,
                "t": "1",
                "u": 1,
                "s": 1,
                "v": 1,
                "w": 1,
                "x": 1
            }
        ],
        "j": {
            "id": 1,
            "n": "Fakultas Teknik",
            "a": 1766068160
        },
        "p": {
            "id": 1,
            "n": "160x250 (buku teks)",
            "a": 1766068160
        },
        "a": 1766068160
    },
    {
        "id": 2,
        "i": true,
        "e": "The Power of Core Values",
        "j": {
            "id": 1,
            "n": "Fakultas Teknik",
            "a": 1766068160
        },
        "p": {
            "id": 2,
            "n": "A5",
            "a": 1766068160
        },
        "a": 1766068160
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
                        "created_at": 1766133986,
                        "updated_at": null
                    },
                    "created_at": 1766133987,
                    "updated_at": null
                },
                "created_at": 1766133990,
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
                        "created_at": 1766133986,
                        "updated_at": null
                    },
                    "created_at": 1766133987,
                    "updated_at": null
                },
                "created_at": 1766133990,
                "updated_at": null
            }
        ],
        "status": [
            {
                "id": 1,
                "label": {
                    "id": 1,
                    "name": "Layouter"
                },
                "code": {
                    "id": 1,
                    "name": "Belum"
                },
                "created_at": 1766133989,
                "updated_at": null
            },
            {
                "id": 2,
                "label": {
                    "id": 2,
                    "name": "Desainer"
                },
                "code": {
                    "id": 2,
                    "name": "Proses"
                },
                "created_at": 1766133989,
                "updated_at": null
            },
            {
                "id": 3,
                "label": {
                    "id": 3,
                    "name": "ISBN"
                },
                "code": {
                    "id": 4,
                    "name": "Sudah"
                },
                "created_at": 1766133989,
                "updated_at": null
            }
        ],
        "flag": [
            {
                "id": 1,
                "is_active": false,
                "part": {
                    "id": 1,
                    "name": "File"
                },
                "created_at": 1766133990,
                "updated_at": null
            },
            {
                "id": 2,
                "is_active": true,
                "part": {
                    "id": 3,
                    "name": "CV"
                },
                "created_at": 1766133990,
                "updated_at": null
            }
        ],
        "descriptions": [
            {
                "id": 1,
                "items": [
                    {
                        "id": 1,
                        "text": "cover warna biru",
                        "created_at": 1766133991,
                        "updated_at": null
                    },
                    {
                        "id": 2,
                        "text": "minta alternatif cover",
                        "created_at": 1766133991,
                        "updated_at": null
                    },
                    {
                        "id": 3,
                        "text": "biru sama merah",
                        "created_at": 1766133991,
                        "updated_at": null
                    },
                    {
                        "id": 4,
                        "text": "warna fakultas",
                        "created_at": 1766133991,
                        "updated_at": null
                    }
                ],
                "descriptionpart": {
                    "id": 1,
                    "name": "Layouter"
                },
                "created_at": 1766133991,
                "updated_at": null
            },
            {
                "id": 2,
                "items": [],
                "descriptionpart": {
                    "id": 2,
                    "name": "Desainer"
                },
                "created_at": 1766133991,
                "updated_at": null
            }
        ],
        "notes": [
            {
                "id": 1,
                "items": [
                    {
                        "id": 1,
                        "content": "Cover ini proval",
                        "created_at": 1766133991,
                        "updated_at": null
                    },
                    {
                        "id": 2,
                        "content": "Cover revisi terus",
                        "created_at": 1766133991,
                        "updated_at": null
                    },
                    {
                        "id": 3,
                        "content": "cover e angeeel",
                        "created_at": 1766133991,
                        "updated_at": null
                    },
                    {
                        "id": 4,
                        "content": "Penulis e njauk revisi terus hmm",
                        "created_at": 1766133991,
                        "updated_at": null
                    }
                ],
                "notepart": {
                    "id": 1,
                    "name": "Cover"
                },
                "created_at": 1766133991,
                "updated_at": null
            },
            {
                "id": 2,
                "items": [],
                "notepart": {
                    "id": 2,
                    "name": "Isbn"
                },
                "created_at": 1766133991,
                "updated_at": null
            }
        ],
        "identification": [
            {
                "id": 1,
                "isbn": "32123123",
                "type": {
                    "id": 1,
                    "name": "ISBN"
                },
                "created_at": 1766133990,
                "updated_at": null
            },
            {
                "id": 2,
                "isbn": "3212312323",
                "type": {
                    "id": 2,
                    "name": "E-ISBN"
                },
                "created_at": 1766133990,
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
                        "created_at": 1766133990,
                        "updated_at": null
                    },
                    {
                        "id": 2,
                        "user": {
                            "id": 2,
                            "username": "sarah"
                        },
                        "created_at": 1766133991,
                        "updated_at": null
                    },
                    {
                        "id": 3,
                        "user": {
                            "id": 3,
                            "username": "menik"
                        },
                        "created_at": 1766133991,
                        "updated_at": null
                    }
                ],
                "section": {
                    "id": 1,
                    "name": "Layouter"
                },
                "created_at": 1766133990,
                "updated_at": null
            },
            {
                "id": 2,
                "by": [],
                "section": {
                    "id": 2,
                    "name": "Desainer"
                },
                "created_at": 1766133990,
                "updated_at": null
            }
        ],
        "cover": [
            {
                "id": 1,
                "thumbnail": "media/thumbnail/image001.jpeg",
                "length": 10,
                "height": 250,
                "width": 160,
                "x_axis": 1,
                "y_axis": 1
            }
        ],
        "institute": {
            "id": 1,
            "name": "Fakultas Teknik",
            "created_at": 1766133986,
            "updated_at": null
        },
        "size": {
            "id": 1,
            "name": "160x250 (buku teks)",
            "created_at": 1766133988,
            "updated_at": null
        },
        "created_at": 1766133989,
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
        "cover": [],
        "institute": {
            "id": 1,
            "name": "Fakultas Teknik",
            "created_at": 1766133986,
            "updated_at": null
        },
        "size": {
            "id": 2,
            "name": "A5",
            "created_at": 1766133988,
            "updated_at": null
        },
        "created_at": 1766133989,
        "updated_at": null
    }
]
```