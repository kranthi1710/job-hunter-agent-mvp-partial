import asyncio

from services.search_service import SearchService


def get_posted_filter() -> str:
    """
    Ask the user how recent the jobs should be.
    """

    print("\nPosted Date Filter")
    print("-" * 30)
    print("1. All Jobs")
    print("2. Last 24 Hours")
    print("3. Last 3 Days")
    print("4. Last 7 Days")
    print("5. Last 30 Days")

    option = input("\nSelect an option (1-5): ").strip()

    mapping = {
        "1": "all",
        "2": "24h",
        "3": "3d",
        "4": "7d",
        "5": "30d"
    }

    return mapping.get(option, "all")


async def main():

    print("=" * 60)
    print("        Job Intelligence Platform")
    print("=" * 60)

    keyword = input("\nEnter job keyword: ").strip()

    if not keyword:
        print("Keyword cannot be empty.")
        return

    posted_filter = get_posted_filter()

    export = input(
        "\nGenerate Excel Report? (y/n): "
    ).strip().lower()

    export_excel = export == "y"

    service = SearchService()

    try:

        result = await service.search(
            keyword=keyword,
            posted_within=posted_filter,
            export_excel=export_excel
        )

    except Exception as ex:

        print("\nSearch failed!")
        print(ex)
        return

    print("\n")
    print("=" * 60)
    print("Search Completed")
    print("=" * 60)

    print(f"Keyword      : {result['keyword']}")
    print(f"Jobs Found   : {result['total_jobs']}")

    if result["excel_file"]:
        print(f"Excel Report : {result['excel_file']}")

    jobs = result["jobs"]

    if not jobs:

        print("\nNo jobs found.")
        return

    print("\nTop Results")
    print("-" * 60)

    for index, job in enumerate(jobs[:10], start=1):

        print(f"\n{index}. {job.title}")

        print(f"   Company : {job.company}")
        print(f"   Location: {job.location}")
        print(f"   Source  : {job.source}")
        print(f"   Apply   : {job.apply_url}")

    print("\nDone.")


if __name__ == "__main__":
    asyncio.run(main())