from typing import List, Optional

from exports.excel_export import ExcelExporter
from models.job import Job
from providers.remoteok import RemoteOKProvider
from utils.date_utils import DateUtils


class SearchService:
    """
    Handles all business logic related to job searching.
    """

    def __init__(self):
        self.providers = [
            RemoteOKProvider()
        ]

        self.exporter = ExcelExporter()

    async def search(
        self,
        keyword: str,
        posted_within: str = "all",
        export_excel: bool = True
    ) -> dict:

        all_jobs: List[Job] = []

        # Collect jobs from every provider
        for provider in self.providers:

            try:

                jobs = await provider.fetch_jobs(keyword)

                all_jobs.extend(jobs)

            except Exception as ex:

                print(
                    f"Provider failed: "
                    f"{provider.__class__.__name__}"
                )

                print(ex)

        all_jobs = self._remove_duplicates(all_jobs)

        all_jobs = self._filter_jobs(
            all_jobs,
            posted_within
        )

        excel_file: Optional[str] = None

        if export_excel:

            excel_file = self.exporter.export(
                all_jobs
            )

        return {

            "keyword": keyword,

            "total_jobs": len(all_jobs),

            "excel_file": excel_file,

            "jobs": all_jobs

        }

    def _remove_duplicates(
        self,
        jobs: List[Job]
    ) -> List[Job]:

        unique = []

        seen = set()

        for job in jobs:

            key = (

                job.company.lower(),

                job.title.lower(),

                job.apply_url.lower()

            )

            if key in seen:
                continue

            seen.add(key)

            unique.append(job)

        return unique

    def _filter_jobs(
        self,
        jobs: List[Job],
        posted_within: str
    ) -> List[Job]:

        if posted_within == "all":
            return jobs

        mapping = {

            "24h": 24,

            "3d": 72,

            "7d": 168,

            "30d": 720

        }

        hours = mapping.get(posted_within)

        if not hours:
            return jobs

        filtered = []

        for job in jobs:

            if job.posted_date is None:
                continue

            if DateUtils.is_within_hours(
                job.posted_date,
                hours
            ):

                filtered.append(job)

        return filtered