"""
URL Metadata Preview Generator
Fetches Open Graph, Twitter Card, and meta tags from any URL.
"""

import argparse
import json
from src.fetcher import URLMetaFetcher


def parse_args():
    parser = argparse.ArgumentParser(description="URL Metadata Preview Generator")
    parser.add_argument("urls", nargs="+", help="URLs to fetch metadata from")
    parser.add_argument("-o", "--output", help="Save results to JSON file")
    parser.add_argument("--timeout", type=int, default=10, help="Request timeout in seconds")
    return parser.parse_args()


def main():
    args = parse_args()
    fetcher = URLMetaFetcher(timeout=args.timeout)
    results = []

    for url in args.urls:
        print(f"\n🔗 Fetching: {url}")
        meta = fetcher.fetch(url)
        results.append(meta)
        _print_meta(meta)

    if args.output:
        with open(args.output, "w") as f:
            json.dump(results, f, indent=2)
        print(f"\n💾 Saved to '{args.output}'")


def _print_meta(meta: dict):
    if meta.get("error"):
        print(f"  ❌ Error: {meta['error']}")
        return
    fields = [
        ("Title",       meta.get("og:title") or meta.get("title")),
        ("Description", meta.get("og:description") or meta.get("description")),
        ("Image",       meta.get("og:image")),
        ("Site Name",   meta.get("og:site_name")),
        ("Type",        meta.get("og:type")),
        ("Author",      meta.get("author")),
        ("Keywords",    meta.get("keywords")),
        ("Status",      meta.get("status_code")),
        ("Content-Type",meta.get("content_type")),
    ]
    for label, value in fields:
        if value:
            value_str = str(value)[:100]
            print(f"  {label:<14}: {value_str}")


if __name__ == "__main__":
    main()
