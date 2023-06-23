import boto3

def disable_public_bucket_creation():
    # Create an S3 client
    s3_client = boto3.client('s3')

    # Update the S3 Block Public Access configuration
    response = s3_client.put_public_access_block(
        # Bucket='*',  # Apply the configuration to all buckets
        PublicAccessBlockConfiguration={
            'BlockPublicAcls': True,
            'IgnorePublicAcls': True,
            'BlockPublicPolicy': True,
            'RestrictPublicBuckets': True
        }
    )

    # Check if the update was successful
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print("Public bucket creation disabled successfully.")
    else:
        print("Error disabling public bucket creation.")

# Call the function to disable public bucket creation
disable_public_bucket_creation()
