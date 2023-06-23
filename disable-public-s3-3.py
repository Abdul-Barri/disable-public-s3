import boto3

def disable_public_bucket_creation():
    """Disables public bucket creation on an AWS account."""

    client = boto3.client("s3")
    response = client.put_bucket_public_access_block(
        PublicAccessBlockConfiguration={
            "BlockPublicAcls": True,
            "BlockPublicPolicy": True,
            "IgnorePublicAcls": True,
            "RestrictPublicBucketPolicy": True,
        }
    )

    if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
        print("Public bucket creation has been disabled.")
    else:
        print("An error occurred.")

if __name__ == "__main__":
    disable_public_bucket_creation()
