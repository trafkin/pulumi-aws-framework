create a file called `instances_data.py`, the file has to be like this:
```
import pulumi_aws as aws

instances = [
    {
        "name": "ServerOne",
        "ami": "ami-09e67e426f25ce0d7",
        "instance_type": "t2.micro",
        "subnet_id": "subnet-xxx",
        "security_group_ids": ["sg-xxx"],
        "tags": {
            "Name": "ServerOne",
        },
        "key_name": "example-key"
    },
    {
        "name": "ServerTwo",
        "ami": "ami-09e67e426f25ce0d7",
        "instance_type": "t2.micro",
        "subnet_id": "subnet-xxx",
        "security_group_ids": ["sg-xxx"],
        "tags": {
            "Name": "ServerOne",
        },
        "key_name": "example-key"
    }
]
```
you can insert any `dict` you want with instances info.