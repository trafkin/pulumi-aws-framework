import pulumi
import pulumi_aws as aws

from instances_data import instances


instances

for instance in instances:

    web = aws.ec2.Instance(instance["name"],
        ami=instance["ami"],
        instance_type=instance["instance_type"],
        tags=instance["tags"],
        vpc_security_group_ids=instance["security_group_ids"],
        subnet_id=instance["subnet_id"],
        key_name=instance["key_name"]
    )
