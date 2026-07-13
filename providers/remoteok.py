from datetime import datetime
from typing import List

from config import Config
from models.job import Job
from utils.http_client import HttpClient


class RemoteOKProvider:
    """
    Fetch jobs from the RemoteOK public API.
    """

    def __init__(self):
        self.client = HttpClient()

    async def fetch_jobs(
        self,
        keyword: str = ""
    ) -> List[Job]:

        response = await self.client.get(
            Config.REMOTEOK_URL
        )

        if not isinstance(response, list):
            return []

        jobs: List[Job] = []

        # RemoteOK returns metadata as first element
        for item in response[1:]:

            if not isinstance(item, dict):
                continue

            job = self._convert(item)

            if job is None:
                continue

            if keyword:

                searchable = (
                    f"{job.title} "
                    f"{job.company} "
                    f"{job.description or ''} "
                    f"{' '.join(job.skills)}"
                ).lower()

                if keyword.lower() not in searchable:
                    continue

            jobs.append(job)

        return jobs

    def _convert(
        self,
        data: dict
    ) -> Job | None:

        apply_url = (
            data.get("apply_url")
            or data.get("url")
            or ""
        )

        if not apply_url:
            return None

        tags = data.get("tags") or []

        if not isinstance(tags, list):
            tags = []

        return Job(

            title=data.get(
                "position",
                "Unknown Position"
            ),

            company=data.get(
                "company",
                "Unknown Company"
            ),

            location=data.get(
                "location",
                "Remote"
            ),

            employment_type=data.get(
                "type"
            ),

            experience_required=None,

            salary=data.get(
                "salary"
            ),

            skills=tags,

            description=data.get(
                "description"
            ),

            apply_url=apply_url,

            source="RemoteOK",

            posted_date=self._parse_date(
                data.get("date")
            ),

            application_end_date=None
        )

    def _parse_date(
        self,
        value
    ):

        if not value:
            return None

        try:

            return datetime.fromisoformat(
                value.replace(
                    "Z",
                    "+00:00"
                )
            )

        except Exception:

            return None