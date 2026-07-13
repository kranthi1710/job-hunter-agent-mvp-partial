from typing import Literal

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse

from services.search_service import SearchService

app = FastAPI(
    title="Job Intelligence Platform",
    description="Search jobs from multiple providers and export results to Excel.",
    version="1.0.0"
)

service = SearchService()


@app.get("/")
def root():
    return {
        "message": "Job Intelligence Platform API",
        "docs": "/docs",
        "health": "/health"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/search")
async def search_jobs(
    keyword: str,
    posted_within: Literal["all", "24h", "3d", "7d", "30d"] = "all",
    export_excel: bool = True
):
    """
    Search jobs and optionally generate an Excel report.
    """

    try:

        result = await service.search(
            keyword=keyword,
            posted_within=posted_within,
            export_excel=export_excel
        )

        return {
            "keyword": result["keyword"],
            "total_jobs": result["total_jobs"],
            "excel_file": result["excel_file"],
            "jobs": [
                job.model_dump(mode="json")
                for job in result["jobs"]
            ]
        }

    except Exception as ex:
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )


@app.get("/download")
async def download_excel(
    keyword: str,
    posted_within: Literal["all", "24h", "3d", "7d", "30d"] = "all"
):
    """
    Generate and download the Excel report.
    """

    try:

        result = await service.search(
            keyword=keyword,
            posted_within=posted_within,
            export_excel=True
        )

        if not result["excel_file"]:
            raise HTTPException(
                status_code=404,
                detail="Excel file was not generated."
            )

        return FileResponse(
            path=result["excel_file"],
            filename=result["excel_file"].split("/")[-1],
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    except HTTPException:
        raise

    except Exception as ex:
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )