def is_duplicate(category_name: str, region: str, type_: str, categories: []):
    for category in categories:
        if category.name == category_name \
                and category.region == region\
                and category.type_ == type_:
            return True
        else:
            return False
    return False
