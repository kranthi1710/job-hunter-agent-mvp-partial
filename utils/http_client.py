from typing import Any, Dict, Optional

import httpx

from config import Config


class HttpClient:
    """
    Shared HTTP client for all providers.

    Features
    --------
    - Async
    - Timeout
    - Connection pooling
    - JSON parsing
    - Better error messages
    """

    def __init__(self):

        self.timeout = httpx.Timeout(
            Config.REQUEST_TIMEOUT
        )

        self.headers = {

            "User-Agent":
            "Job-Intelligence-Platform/1.0",

            "Accept":
            "application/json"

        }

    async def get(
        self,
        url: str,
        params: Optional[Dict] = None,
        headers: Optional[Dict] = None
    ) -> Any:

        request_headers = self.headers.copy()

        if headers:
            request_headers.update(headers)

        try:

            async with httpx.AsyncClient(
                timeout=self.timeout,
                follow_redirects=True
            ) as client:

                response = await client.get(
                    url=url,
                    params=params,
                    headers=request_headers
                )

                response.raise_for_status()

                content_type = response.headers.get(
                    "content-type",
                    ""
                )

                if "application/json" in content_type:

                    return response.json()

                raise Exception(
                    f"Expected JSON response but received: {content_type}"
                )

        except httpx.TimeoutException:

            raise Exception(
                f"Request timed out after {Config.REQUEST_TIMEOUT} seconds."
            )

        except httpx.HTTPStatusError as ex:

            raise Exception(
                f"HTTP {ex.response.status_code}: {ex.response.text}"
            )

        except httpx.RequestError as ex:

            raise Exception(
                f"Network error: {str(ex)}"
            )

        except Exception:

            raise