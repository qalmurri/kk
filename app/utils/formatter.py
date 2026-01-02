def flatten_scripts(data: list) -> list:
    rows = []
    for item in data:
        rows.append({
            "id": item.get("id"),
            "title": item.get("title"),
            "entry_date": item.get("entry_date"),
            "created_at": item.get("created_at"),
            "institute": item.get("institute", {}).get("name"),
            "_raw": item
        })
    return rows
