import boto3


def get_s3_client(aws_id, aws_key, aws_region) -> boto3.client:
    """
    Generate S3 Client (It could also be implemented as a Singleton).
    :param aws_id: ID of the AWS user with permissions to download/upload files from S3.
    :param aws_key: KEY of the AWS user with permissions to download/upload files from S3.
    :param aws_region: Region of the AWS bucket from which the DB is going to be downloaded/uploaded.
    :return:
    """
    client = boto3.client(
        's3',
        aws_access_key_id=aws_id,
        aws_secret_access_key=aws_key,
        region_name=aws_region
    )
    return client


def get_db_from_s3(s3_bucket, db_name, db_local_path) -> bool:
    """
    Get SQLite DB from S3.
    :param s3_bucket: name of the S3 bucket from which the DB is going to be downloaded.
    :param db_name: name of the DB to download.
    :param db_local_path: local path in which the DB is going to be stored.
    :return: bool: True if download is successful, False if not.
    """
    client = get_s3_client()
    return client.download_file(s3_bucket, db_name, db_local_path)


def upload_db_to_s3(db_local_path, s3_bucket, db_name) -> bool:
    """
    Upload SQLite DB to S3.
    :param db_local_path: local path in which the DB is stored.
    :param s3_bucket: name of the S3 bucket to which DB is going to be uploaded the DB.
    :param db_name: (OPTIONAL) name of the DB in S3. If not specified, then db_local_path is used.
    :return: bool: True if upload is successful, False if not.
    """
    client = get_s3_client()
    return client.upload_file(db_local_path, s3_bucket, db_name)
