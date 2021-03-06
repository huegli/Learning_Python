def new(num_buckets=256):
    """Initialize a Map with the given number of buckets."""
    aMap = []
    for i in range(0, num_buckets):
        aMap.append([])
    return aMap
    
def hash_key(aMap, key):
    """Given a key, this will create a number and then convert it to
    an index for the aMap's buckets."""
    return hash(key) % len(aMap)
    
def get_bucket(aMap, key):
    """Given a key, find the bucket where it would go."""
    # this will generate the bucket id in which we should store a given key
    bucket_id = hash_key(aMap, key)
    # return the list that is stored at bucket_id
    return aMap[bucket_id]
    
def get_slot(aMap, key, default=None):
    """
    Returns the index, key, and value of a slot in a bucket.
    Returns -1, key, and default (None if none set) when not found.
    """
    # get a list representing the bucket in which the key is
    bucket = get_bucket(aMap, key)
    
    # iterate over all entries in the bucket list (:-) until we find the key
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            return i, k, v

    # this means we actually don't have the key in the bucket list
    return -1, key, default
    
def get(aMap, key, default=None):
    """Gets the value in a bucket for the given key, or the default."""
    # return what is in default if nothing found, otherwise value
    i, k, v = get_slot(aMap, key, default=default)
    return v
    
def set(aMap, key, value):
    """Sets the key to the value, replacing an existing value."""
    bucket = get_bucket(aMap, key)
    i, k, v = get_slot(aMap, key)
    
    if i >= 0:
        # the key exists, replace it
        bucket[i] = (key, value)
    else:
        # the key does not, append to create it
        bucket.append((key, value))
        
def delete(aMap, key):
    """Deletes the given key from the Map."""
    bucket = get_bucket(aMap, key)
    
    for i in xrange(len(bucket)):
        k, v = bucket[i]
        if key == k:
            del bucket[i]
            break
        
def list(aMap):
    """Print's out what's in the Map."""
    for bucket in aMap:
        if bucket:
            for k,v in bucket:
                print k, v
                
