import os
import boto3
from dotenv import load_dotenv
import json


if __name__ == "__main__":
    load_dotenv()
    with open("./secret.json") as f:
        d = json.load(f)
        aws_access_key_id = d["aws_access_key_id"]
        aws_secret_access_key = d["aws_secret_access_key"]

    # print("aws_access_key_id: ", aws_access_key_id)
    # print("aws_secret_access_key: ", aws_secret_access_key)

    session = boto3.session.Session()
    s3_client = session.client(
        service_name="s3",
        region_name="ru-msk",
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        endpoint_url="https://hb.ru-msk.vkcs.cloud",
    )

    s3_client.download_file(
        "mlopstest",
        "tests/sampled_preprocessed_train_50k.csv",
        "data/raw/sampled_preprocessed_train_50k.csv",
    )
