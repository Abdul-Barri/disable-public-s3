import boto3

__all__ = ["S3Control"]


class S3Control:

    def __init__(self, role: boto3.Session): 
        self.client = role.client("s3control")

    def put_public_access_block(self, account_id: str) -> None:

        return self.client.put_public_access_block( 
            PublicAccessBlockConfiguration={
                "blockPublicAcIs": True, 
                "IgnorePublicácis": True,
                "BlockPublicPolicy": True,
                "Restrict PublicBuckets": True,
            },
            AccountId=account_id,
        )