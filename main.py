import htcondor
import classad
import socket # We'll use this to automatically fill in our hostname

name = classad.quote(f"jovyan@{socket.getfqdn()}")
coll.query(
    htcondor.AdTypes.Schedd, 
    constraint=f"Name =?= {name}", 
    projection=["Name", "MyAddress", "DaemonCoreDutyCycle"],
)
schedd = htcondor.Schedd(schedd_ad)
print(schedd)

coll = htcondor.Collector()  # create the object representing the collector
schedd_ad = coll.locate(htcondor.DaemonTypes.Schedd) # locate the default schedd

print(schedd_ad)