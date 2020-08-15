import htcondor
import classad
import socket # We'll use this to automatically fill in our hostname

coll = htcondor.Collector()  # create the object representing the collector
schedd_ad = coll.locate(htcondor.DaemonTypes.Schedd) # locate the default schedd

print(schedd_ad)

schedd = htcondor.Schedd(schedd_ad)
print(schedd)
# 1: Idle (I)
# 2: Running (R)
# 3: Removed (X)
# 4: Completed (C)
# 5: Held (H)
# 6: Transferring Output
# 7: Suspended

for job in schedd.xquery(projection=['x509UserProxyVOName',
                                     'x509UserProxyEmail',
                                     'ClusterId',
                                     'JobStatus',]):
    print(repr(job))
#
# for job in schedd.xquery(
#         projection=['x509UserProxyVOName',
#                     'ClusterId',
#                     'JobStatus',]):
#         print(repr(job))

# results = schedd.query('JobStatus =?= "JobStatus = 4"', ["ClusterId", "ProcId"])
# len(results)

# for job in schedd.query(attr_list=['JobStatus']):
#     print(repr(job))
