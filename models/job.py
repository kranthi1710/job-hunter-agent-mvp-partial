from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, Field


class Job(BaseModel):
    """
    Common job model used across all job providers.

    Every provider (RemoteOK, Greenhouse, Lever, etc.)
    converts its response into this structure.
    """

    title: str = Field(
        ...,
        description="Job title"
    )

    company: str = Field(
        ...,
        description="Company name"
    )

    location: Optional[str] = Field(
        default=None,
        description="Job location"
    )

    employment_type: Optional[str] = Field(
        default=None,
        description="Full-time, Contract, Internship etc."
    )

    experience_required: Optional[str] = Field(
        default=None,
        description="Required experience"
    )

    salary: Optional[str] = Field(
        default=None,
        description="Salary information"
    )

    skills: List[str] = Field(
        default_factory=list,
        description="Skills extracted from job description"
    )

    description: Optional[str] = Field(
        default=None,
        description="Complete job description"
    )

    apply_url: str = Field(
        ...,
        description="Application URL"
    )

    source: str = Field(
        ...,
        description="Job source"
    )

    posted_date: Optional[datetime] = Field(
        default=None,
        description="When job was posted"
    )

    application_end_date: Optional[datetime] = Field(
        default=None,
        description="Application closing date"
    )


    def posted_age(self) -> str:
        """
        Returns human readable job age.

        Example:
        2 hours ago
        3 days ago
        """

        if not self.posted_date:
            return "Unknown"

        difference = (
            datetime.utcnow()
            -
            self.posted_date
        )

        seconds = difference.total_seconds()

        if seconds < 3600:
            minutes = int(seconds / 60)
            return f"{minutes} minutes ago"

        hours = int(seconds / 3600)

        if hours < 24:
            return f"{hours} hours ago"

        days = int(hours / 24)

        return f"{days} days ago"