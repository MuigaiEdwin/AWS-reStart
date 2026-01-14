import argparse
import datetime
import json
import logging
import os
import sys
import time
from typing import List, Optional
import boto3
from botocore.exceptions import ClientError

#!/usr/bin/env python3
"""
aws_manager.py

Requirements:
    pip install boto3

Usage examples:
    python aws_manager.py list-ec2
    python aws_manager.py start-ec2 --id i-0123456789abcdef0
    python aws_manager.py list-s3
    python aws_manager.py create-s3 --name my-bucket-unique-12345 --region us-east-1
    python aws_manager.py fetch-logs --group /aws/lambda/my-func --start -3600 --limit 50
    python aws_manager.py analyze-logs --group /aws/lambda/my-func --start -3600
    python aws_manager.py deploy-s3 --bucket my-bucket --key releases/app.zip --file ./app.zip
    python aws_manager.py codedeploy --app MyApp --group MyGroup --bucket my-bucket --key releases/app.zip
"""



logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("aws_manager")


def get_client(service_name: str, region: Optional[str] = None):
        if region:
                return boto3.client(service_name, region_name=region)
        return boto3.client(service_name)


# EC2 Management
def list_ec2_instances(region: Optional[str] = None):
        ec2 = get_client("ec2", region)
        try:
                resp = ec2.describe_instances()
                instances = []
                for r in resp.get("Reservations", []):
                        for inst in r.get("Instances", []):
                                instances.append(
                                        {
                                                "InstanceId": inst.get("InstanceId"),
                                                "State": inst.get("State", {}).get("Name"),
                                                "InstanceType": inst.get("InstanceType"),
                                                "LaunchTime": str(inst.get("LaunchTime")),
                                                "Tags": inst.get("Tags", []),
                                        }
                                )
                return instances
        except ClientError as e:
                logger.error("Failed to list EC2 instances: %s", e)
                return []


def start_ec2_instance(instance_id: str, region: Optional[str] = None):
        ec2 = get_client("ec2", region)
        try:
                resp = ec2.start_instances(InstanceIds=[instance_id])
                return resp
        except ClientError as e:
                logger.error("Failed to start instance %s: %s", instance_id, e)
                raise


def stop_ec2_instance(instance_id: str, region: Optional[str] = None):
        ec2 = get_client("ec2", region)
        try:
                resp = ec2.stop_instances(InstanceIds=[instance_id])
                return resp
        except ClientError as e:
                logger.error("Failed to stop instance %s: %s", instance_id, e)
                raise


def get_console_output(instance_id: str, region: Optional[str] = None):
        ec2 = get_client("ec2", region)
        try:
                resp = ec2.get_console_output(InstanceId=instance_id, Latest=True)
                output = resp.get("Output", "")
                return output
        except ClientError as e:
                logger.error("Failed to get console output for %s: %s", instance_id, e)
                raise


# S3 Management & Deployment
def list_s3_buckets():
        s3 = get_client("s3")
        try:
                resp = s3.list_buckets()
                buckets = [b["Name"] for b in resp.get("Buckets", [])]
                return buckets
        except ClientError as e:
                logger.error("Failed to list S3 buckets: %s", e)
                return []


def create_s3_bucket(bucket_name: str, region: Optional[str] = None):
        s3 = get_client("s3", region)
        try:
                if region and region != "us-east-1":
                        s3.create_bucket(
                                Bucket=bucket_name,
                                CreateBucketConfiguration={"LocationConstraint": region},
                        )
                else:
                        s3.create_bucket(Bucket=bucket_name)
                logger.info("Created bucket %s", bucket_name)
                return True
        except ClientError as e:
                logger.error("Failed to create bucket %s: %s", bucket_name, e)
                return False


def upload_file_to_s3(bucket: str, key: str, file_path: str):
        s3 = get_client("s3")
        try:
                s3.upload_file(Filename=file_path, Bucket=bucket, Key=key)
                logger.info("Uploaded %s to s3://%s/%s", file_path, bucket, key)
                return True
        except ClientError as e:
                logger.error("Failed to upload file %s to %s/%s: %s", file_path, bucket, key, e)
                return False


def deploy_to_s3(bucket: str, key: str, file_path: str):
        return upload_file_to_s3(bucket, key, file_path)


def trigger_codedeploy_deployment(application_name: str, deployment_group: str, s3_bucket: str, s3_key: str, bundle_type: str = "zip"):
        codedeploy = get_client("codedeploy")
        revision = {
                "revisionType": "S3",
                "s3Location": {
                        "bucket": s3_bucket,
                        "key": s3_key,
                        "bundleType": bundle_type.upper(),
                },
        }
        try:
                resp = codedeploy.create_deployment(
                        applicationName=application_name,
                        deploymentGroupName=deployment_group,
                        revision=revision,
                        ignoreApplicationStopFailures=True,
                )
                deployment_id = resp.get("deploymentId")
                logger.info("Triggered CodeDeploy deployment %s", deployment_id)
                return deployment_id
        except ClientError as e:
                logger.error("Failed to create CodeDeploy deployment: %s", e)
                raise


# CloudWatch Logs
def fetch_cloudwatch_logs(log_group_name: str, start_time_seconds: Optional[int] = None, end_time_seconds: Optional[int] = None, filter_pattern: Optional[str] = None, limit: int = 100, region: Optional[str] = None):
        logs = get_client("logs", region)
        kwargs = {
                "logGroupName": log_group_name,
                "limit": limit,
        }
        if filter_pattern:
                kwargs["filterPattern"] = filter_pattern
        if start_time_seconds:
                kwargs["startTime"] = int(start_time_seconds * 1000)
        if end_time_seconds:
                kwargs["endTime"] = int(end_time_seconds * 1000)
        try:
                events = []
                resp = logs.filter_log_events(**kwargs)
                events.extend(resp.get("events", []))
                # handle pagination
                next_token = resp.get("nextToken")
                while next_token and len(events) < limit:
                        resp = logs.filter_log_events(logGroupName=log_group_name, nextToken=next_token, limit=limit)
                        events.extend(resp.get("events", []))
                        next_token = resp.get("nextToken")
                logger.info("Fetched %d log events from %s", len(events), log_group_name)
                return events[:limit]
        except ClientError as e:
                logger.error("Failed to fetch logs for %s: %s", log_group_name, e)
                return []


# Sentiment analysis using AWS Comprehend
def analyze_sentiment_texts(texts: List[str], language_code: str = "en", region: Optional[str] = None):
        if not texts:
                return []
        comprehend = get_client("comprehend", region)
        results = []
        # Comprehend batch_detect_sentiment supports up to 25 documents per call
        batch_size = 25
        for i in range(0, len(texts), batch_size):
                batch = texts[i : i + batch_size]
                try:
                        resp = comprehend.batch_detect_sentiment(TextList=batch, LanguageCode=language_code)
                        for idx, res in enumerate(resp.get("ResultList", [])):
                                results.append(
                                        {
                                                "Index": res.get("Index"),
                                                "Sentiment": res.get("Sentiment"),
                                                "SentimentScore": res.get("SentimentScore"),
                                                "Text": batch[res.get("Index")],
                                        }
                                )
                        for err in resp.get("ErrorList", []):
                                logger.warning("Comprehend error for index %s: %s", err.get("Index"), err.get("ErrorMessage"))
                except ClientError as e:
                        logger.error("Comprehend batch error: %s", e)
        return results


def analyze_logs_sentiment(log_group_name: str, start_seconds_ago: int = 3600, language_code: str = "en", region: Optional[str] = None, limit: int = 100):
        now = int(time.time())
        start_time = now - start_seconds_ago
        events = fetch_cloudwatch_logs(log_group_name, start_time_seconds=start_time, end_time_seconds=now, limit=limit, region=region)
        messages = []
        for ev in events:
                msg = ev.get("message", "")
                if msg:
                        # Trim long messages for Comprehend; try to keep to < 5000 bytes
                        if len(msg) > 4000:
                                msg = msg[:4000]
                        messages.append(msg)
        if not messages:
                logger.info("No messages to analyze")
                return []
        logger.info("Analyzing %d messages with Comprehend", len(messages))
        results = analyze_sentiment_texts(messages, language_code=language_code, region=region)
        return results


# Simple CLI
def parse_args():
        p = argparse.ArgumentParser(description="AWS resource & logs manager with sentiment and deployment helpers")
        sub = p.add_subparsers(dest="cmd")

        sub.add_parser("list-ec2", help="List EC2 instances")

        start_ec2 = sub.add_parser("start-ec2", help="Start an EC2 instance")
        start_ec2.add_argument("--id", required=True, help="Instance ID")

        stop_ec2 = sub.add_parser("stop-ec2", help="Stop an EC2 instance")
        stop_ec2.add_argument("--id", required=True, help="Instance ID")

        sub.add_parser("list-s3", help="List S3 buckets")
        create_s3 = sub.add_parser("create-s3", help="Create S3 bucket")
        create_s3.add_argument("--name", required=True, help="Bucket name")
        create_s3.add_argument("--region", required=False, help="Region")

        fetch_logs = sub.add_parser("fetch-logs", help="Fetch CloudWatch logs")
        fetch_logs.add_argument("--group", required=True, help="Log group name")
        fetch_logs.add_argument("--start", type=int, default=-3600, help="Start seconds relative to now (negative past)")
        fetch_logs.add_argument("--limit", type=int, default=100, help="Max events to return")
        fetch_logs.add_argument("--region", required=False, help="Region")

        analyze_logs = sub.add_parser("analyze-logs", help="Fetch logs and run sentiment analysis")
        analyze_logs.add_argument("--group", required=True, help="Log group name")
        analyze_logs.add_argument("--start", type=int, default=3600, help="Seconds ago to start (e.g. 3600)")
        analyze_logs.add_argument("--language", default="en", help="Language code for Comprehend")
        analyze_logs.add_argument("--region", required=False, help="Region")

        deploy = sub.add_parser("deploy-s3", help="Upload artifact to S3")
        deploy.add_argument("--bucket", required=True, help="S3 bucket")
        deploy.add_argument("--key", required=True, help="S3 key")
        deploy.add_argument("--file", required=True, help="Local file path")

        codedeploy = sub.add_parser("codedeploy", help="Trigger CodeDeploy with S3 revision")
        codedeploy.add_argument("--app", required=True, help="CodeDeploy application name")
        codedeploy.add_argument("--group", required=True, help="Deployment group name")
        codedeploy.add_argument("--bucket", required=True, help="S3 bucket")
        codedeploy.add_argument("--key", required=True, help="S3 key")
        codedeploy.add_argument("--bundle", default="zip", help="Bundle type (zip/tar)")

        return p.parse_args()


def main():
        args = parse_args()
        if args.cmd == "list-ec2":
                instances = list_ec2_instances()
                print(json.dumps(instances, indent=2, default=str))
                return

        if args.cmd == "start-ec2":
                resp = start_ec2_instance(args.id)
                print(json.dumps(resp, default=str, indent=2))
                return

        if args.cmd == "stop-ec2":
                resp = stop_ec2_instance(args.id)
                print(json.dumps(resp, default=str, indent=2))
                return

        if args.cmd == "list-s3":
                buckets = list_s3_buckets()
                print(json.dumps(buckets, indent=2))
                return

        if args.cmd == "create-s3":
                ok = create_s3_bucket(args.name, getattr(args, "region", None))
                print("OK" if ok else "FAILED")
                return

        if args.cmd == "fetch-logs":
                now = int(time.time())
                start = None
                if args.start is not None:
                        # if negative, treat as seconds relative to now
                        if args.start < 0:
                                start = now + args.start
                        else:
                                start = now - args.start
                events = fetch_cloudwatch_logs(args.group, start_time_seconds=start, end_time_seconds=now, limit=args.limit, region=getattr(args, "region", None))
                print(json.dumps(events, indent=2, default=str))
                return

        if args.cmd == "analyze-logs":
                results = analyze_logs_sentiment(args.group, start_seconds_ago=args.start, language_code=args.language, region=getattr(args, "region", None))
                print(json.dumps(results, indent=2, default=str))
                return

        if args.cmd == "deploy-s3":
                ok = deploy_to_s3(args.bucket, args.key, args.file)
                print("OK" if ok else "FAILED")
                return

        if args.cmd == "codedeploy":
                deployment_id = trigger_codedeploy_deployment(args.app, args.group, args.bucket, args.key, bundle_type=args.bundle)
                print(json.dumps({"deploymentId": deployment_id}))
                return

        print("No command provided. Use --help.")


if __name__ == "__main__":
        try:
                main()
        except Exception as e:
                logger.exception("Unhandled exception: %s", e)
                sys.exit(1)