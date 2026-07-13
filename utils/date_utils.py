from datetime import datetime, timezone


class DateUtils:

    @staticmethod
    def is_within_hours(posted_date, hours: int) -> bool:
        if posted_date is None:
            return False

        if posted_date.tzinfo is None:
            posted_date = posted_date.replace(tzinfo=timezone.utc)

        now = datetime.now(timezone.utc)

        difference = now - posted_date

        return difference.total_seconds() <= hours * 3600

    @staticmethod
    def age(posted_date):

        if posted_date is None:
            return "Unknown"

        if posted_date.tzinfo is None:
            posted_date = posted_date.replace(tzinfo=timezone.utc)

        now = datetime.now(timezone.utc)

        delta = now - posted_date

        if delta.days > 0:
            return f"{delta.days} days ago"

        hours = delta.seconds // 3600

        if hours > 0:
            return f"{hours} hours ago"

        minutes = delta.seconds // 60

        return f"{minutes} minutes ago"

    @staticmethod
    def format_date(posted_date):

        if posted_date is None:
            return ""

        return posted_date.strftime("%Y-%m-%d %H:%M")