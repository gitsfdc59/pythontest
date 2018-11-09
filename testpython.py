import beatbox
import pandas as pd
import numpy as np
from simple_salesforce import Salesforce
sf=Salesforce(username='kv@test.com',password='hyderabad999',security_token='')
sf.Account.insert({'Name':'its me'})
service=beatbox.pythonClient()
servcie.login('kv@test.com')
query_result=service.query("select id,name from account")
record=query_result['records']
df=pd.DataFrame(records)
print(df)
print("Records preview")
