"""s3 target class."""

from __future__ import annotations

from singer_sdk.target_base import Target
from singer_sdk import typing as th

from target_s3.formats.format_base import DATE_GRAIN

from target_s3.sinks import (
    s3Sink,
)


class Targets3(Target):
    """Sample target for s3."""

    name = "target-s3"
    config_jsonschema = th.PropertiesList(
        th.Property(
            "format",
            th.ObjectType(
                th.Property(
                    "format_type",
                    th.StringType,
                    required=True,
                    allowed_values=[
                        "parquet",
                        "json",
                    ],  # TODO: configure this from class
                ),
                th.Property(
                    "format_parquet",
                    th.ObjectType(
                        th.Property(
                            "validate",
                            th.BooleanType,
                            required=False,
                            default=False,
                        ),
                    ),
                    required=False,
                ),
                th.Property(
                    "format_json",
                    th.ObjectType(),
                    required=False,
                ),
                th.Property(
                    "format_csv",
                    th.ObjectType(),
                    required=False,
                ),
            ),
        ),
        th.Property(
            "cloud_provider",
            th.ObjectType(
                th.Property(
                    "cloud_provider_type",
                    th.StringType,
                    required=True,
                    allowed_values=["aws"],  # TODO: configure this from class
                ),
                th.Property(
                    "aws",
                    th.ObjectType(
                        th.Property(
                            "aws_access_key_id",
                            th.StringType,
                            required=False,
                            secret=True,
                        ),
                        th.Property(
                            "aws_secret_access_key",
                            th.StringType,
                            required=False,
                            secret=True,
                        ),
                        th.Property(
                            "aws_session_token",
                            th.StringType,
                            required=False,
                            secret=True,
                        ),
                        th.Property(
                            "aws_region",
                            th.StringType,
                            required=True,
                        ),
                        th.Property(
                            "aws_profile_name",
                            th.StringType,
                            required=False,
                        ),
                        th.Property(
                            "aws_bucket",
                            th.StringType,
                            required=True,
                        ),
                        th.Property(
                            "aws_endpoint_override",
                            th.StringType,
                            required=False,
                        ),
                    ),
                    required=False,
                ),
            ),
        ),
        th.Property(
            "prefix",
            th.StringType,
            description="The prefix for the key.",
        ),
        th.Property(
            "stream_name_path_override",
            th.StringType,
            description="The S3 key stream name override.",
        ),
        th.Property(
            "include_process_date",
            th.BooleanType,
            description="A flag indicating whether to append _process_date to record.",
            default=False,
        ),
        th.Property(
            "append_date_to_prefix",
            th.BooleanType,
            description="A flag to append the date to the key prefix.",
            default=True,
        ),
        th.Property(
            "partition_name_enabled",
            th.BooleanType,
            description="A flag (only works if append_date_to_prefix is enabled) to have partitioning name formatted e.g. 'year=2023/month=01/day=01'.",
            default=False,
        ),
        th.Property(
            "append_date_to_prefix_grain",
            th.StringType,
            description="The grain of the date to append to the prefix.",
            allowed_values=DATE_GRAIN.keys(),
            default="day",
        ),
        th.Property(
            "append_date_to_filename",
            th.BooleanType,
            description="A flag to append the date to the key filename.",
            default=True,
        ),
        th.Property(
            "append_date_to_filename_grain",
            th.StringType,
            description="The grain of the date to append to the filename.",
            allowed_values=DATE_GRAIN.keys(),
            default="day",
        ),
        th.Property(
            "flatten_records",
            th.BooleanType,
            description="A flag indictating to flatten records.",
        ),
    ).to_dict()

    default_sink_class = s3Sink


if __name__ == "__main__":
    Targets3.cli()
