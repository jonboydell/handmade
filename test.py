import json

def load_config():
    conditions = []
    values = []
    mapping = json.load('m1.json')
    for k in mapping.keys():
        search_terms = mapping[k]
        for s in search_terms:
            conditions.append(s)
            values.append(k)
    return conditions, values
      
      
  
