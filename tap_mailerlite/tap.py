"""MailerLite tap class."""

from typing import List
from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_mailerlite.streams import (
    MailerLiteStream,
    SubscribersStream,
    SubscriberGroupStream,
)

STREAM_TYPES = [
    SubscribersStream,
    SubscriberGroupStream,
]


class TapMailerLite(Tap):
    """MailerLite tap class."""
    name = "tap-mailerlite"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "mailer_lite_auth_key",
            th.StringType,
            description="API KEY"
        ),
        th.Property(
            "mailer_lite_auth_value",
            th.StringType,
            description="API TOKEN"
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="Date Time"
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
