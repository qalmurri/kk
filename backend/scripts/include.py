def parse_include_param(param: str):
    if not param:
        return set()
    return {x.strip() for x in param.split(",") if x.strip()}
