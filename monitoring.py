import boto3

html_page = "<html><body><h1>List of instances from the Private Subnet</h1>"

# GET SUBNET INFORMATION
def getPrivateSubnetId():
    ec2_client = boto3.client('ec2')
    subnets_info = ec2_client.describe_subnets()

    for subnet in subnets_info['Subnets']:
        if subnet["Tags"][0]["Value"] == "talent-academy-private-a":
            private_subnet = subnet["SubnetId"]
            return private_subnet

private_subnet = getPrivateSubnetId()

ec2 = boto3.resource('ec2')

for instance in ec2.instances.all():

    if instance.subnet_id == private_subnet:       
        html_page += "<p>Id: {0}<b>Type: {1}<b>AMI: {2}<b>State: {3}<b>Subnet:  {4}<br><br></p>".format(       
                        instance.id, instance.instance_type, instance.image.id, instance.state, instance.subnet_id
                    )

html_page += "</body></html>"

html_file = open("index.html", "w")
html_file.write(html_page)
html_file.close()