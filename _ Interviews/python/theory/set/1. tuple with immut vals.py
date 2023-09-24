# If there is a tuple in set, it must contain only immutable data types
a = {([])}  # TypeError: unhashable type: 'list'
