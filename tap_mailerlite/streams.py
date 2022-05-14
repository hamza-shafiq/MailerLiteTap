"""Stream type classes for tap-mailerlite."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_mailerlite.client import MailerLiteStream


class SubscribersStream(MailerLiteStream):
    name = "subscribers"
    path = "/subscribers"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.IntegerType, description="The subscriber's ID"),
        th.Property("name", th.StringType, description="The subscriber's name"),
        th.Property("email", th.StringType, description="The subscriber's email address"),
        th.Property("sent", th.IntegerType),
        th.Property("opened", th.IntegerType),
        th.Property("type", th.StringType, description="account type"),
        th.Property("date_subscribe", th.StringType, description="Date when subscribed"),
    ).to_dict()


class SubscriberGroupStream(MailerLiteStream):
    name = "subscriber_group"
    path = "/groups"
    primary_keys = ["id"]
    replication_key = None

    schema = th.PropertiesList(
        th.Property("id", th.StringType, description="The subscriber group ID"),
        th.Property("name", th.StringType, description="The subscriber group name"),
        th.Property("total", th.IntegerType),
        th.Property("active", th.IntegerType),
        th.Property("unsubscribed", th.IntegerType),
        th.Property("bounced", th.IntegerType),
        th.Property("unconfirmed", th.IntegerType),
        th.Property("junk", th.IntegerType),
        th.Property("sent", th.IntegerType),
        th.Property("opened", th.IntegerType),
        th.Property("clicked", th.IntegerType),
        th.Property("date_created", th.DateTimeType),
    ).to_dict()
