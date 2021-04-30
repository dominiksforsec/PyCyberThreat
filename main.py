from taxii2client.v20 import Server, Collection
from stix2 import TAXIICollectionSource, Filter
import urllib3

urllib3.disable_warnings() #band aid to avoid warning spam in the output for as long as TLS band-aid exists
#assigns server internet locations to variables
TAXII_mitre_srv = Server("https://cti-taxii.mitre.org/taxii/", user = 'invalid', password = 'fixme', verify = False) #band-aid; need to implement proper TLS for production version
#variable for easier access to root of API
TAXII_api_root = TAXII_mitre_srv.api_roots[0]
#example function of the API
# for collection in TAXII_api_root.collections:
    # print(collection.title + ": " + collection.id)

#initialise dictionary to store STIX object
enterprise_atck = {}
#collects 
ent_atck_collection = Collection("https://cti-taxii.mitre.org/stix/collections/95ecc380-afe9-11e4-9b6c-751b66dd541e/", user = 'invalid', password = 'fixme', verify = False) #like above, to fix
TAXII_collection_src = TAXIICollectionSource(ent_atck_collection)
filtered_objects = {"whoisthis": Filter("type", "=", "identity"),
    "mitigations": Filter("type", "=", "course-of-action"),
    #"malware": Filter("type", "=", "malware"),
    #"tools": Filter("type", "=", "tool"),
    }
#store values for every key that was in filtered_objects in enterprise_atck dict
for key in filtered_objects:
    enterprise_atck[key] = TAXII_collection_src.query(filtered_objects[key])

i = 0
# for each_key in enterprise_atck:
#     if i < 2:
#         i += 1
#         print(enterprise_atck[each_key])

print(enterprise_atck["whoisthis"][0])

test_output = open("testjson.json", "w")
test_output.write(str(enterprise_atck["whoisthis"][0])) #this object has JSON structure and can be casted into the string for json output to process if necessary, otherwise work on object I guess
test_output.close()

i = None

