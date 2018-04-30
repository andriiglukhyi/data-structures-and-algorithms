from hash_table import HashTable

def repeated_word(st):
    """fucntion will accept string as an argument"""
    st = st.lower()
    if len(st) == 0:
        return False
    if len(list(st)) == 1:
        return list(st)[0]
    table = HashTable()
    for item in st.split(' '):
        if type(table.buckets[table.hash_key(item)]) == dict:
            return item
        table.set(item, item)
    
    return False


