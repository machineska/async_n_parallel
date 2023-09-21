import re
import time
from urllib.request import Request, urlopen

URLs = [
    "https://www.bitecode.dev/p/relieving-your-python-packaging-pain",
    "https://www.bitecode.dev/p/hype-cycles",
    "https://www.bitecode.dev/p/why-not-tell-people-to-simply-use",
    "https://www.bitecode.dev/p/nobody-ever-paid-me-for-code",
    "https://www.bitecode.dev/p/python-cocktail-mix-a-context-manager",
    "https://www.bitecode.dev/p/the-costly-mistake-so-many-makes",
    "https://www.bitecode.dev/p/the-weirdest-python-keyword",
]

title_pattern = re.compile(r"<title[^>]*>(.*?)</title>", re.IGNORECASE)

user_agent = (
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0"
)


def fetch_url(url):
    start_time = time.time()

    headers = {"User-Agent": user_agent}
    with urlopen(Request(url, headers=headers)) as response:
        html_content = response.read().decode("utf-8")
        match = title_pattern.search(html_content)
        title = match.group(1) if match else "Unknown"

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken ({url}): {elapsed_time:.4f} seconds\n", end="")
    return title


def main():
    for url in URLs:
        title = fetch_url(url)
        print(f"URL: {url}\nTitle: {title}", flush=True)


if __name__ == "__main__":
    # Let's time how long all this takes
    global_start_time = time.time()
    main()
    global_elapsed_time = time.time() - global_start_time
    print(f"Total time taken for all URLs: {global_elapsed_time:.4f} seconds")

