import asyncio

from providers.remoteok import RemoteOKProvider


async def main():

    provider = RemoteOKProvider()

    jobs = await provider.fetch_jobs("python")

    print(f"Jobs Found: {len(jobs)}")

    for job in jobs[:5]:

        print()

        print(job.company)

        print(job.title)

        print(job.location)

        print(job.apply_url)


asyncio.run(main())