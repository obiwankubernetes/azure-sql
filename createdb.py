# go to azure portal and open up cloud shell

# create resource group
# az group create --name <namerg> --location "westus"

# create sql server
# az sql server create --name <namesqlserver> --resource-group <namerg> --location "westus" --admin-user <username> --admin-password <userpassword>

# ensure creation of resource group and resources by finding them in the portal

# create firewall rule to allow accces
# az sql server firewall-rule create --resource-group <namerg> --server <servername> --name <nameofirewall> --start-ip-address 0.0.0.0 --end-ip-address 0.0.0.0

# also enable local ip under firewall section in azure portal

# go to sql server created and its firewal settings and ensure that it is now turned on to allow azure resources to access the server

# create sql db
# az sql db create --resource-group <namerg> --server <servername> --name <nameofdb> --service-objective S0

#  go to azure portal to ensure resource created 