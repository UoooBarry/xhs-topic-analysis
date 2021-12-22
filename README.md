# 小红书搜索与文章拉取

## Setup

Mitmproxy installation guide: <https://docs.mitmproxy.org/stable/overview-installation/>

Install the libraries missing for the `get_search.py` script.

## Start

```bash
# Install mitmproxy, and other packages first


mitmproxy -s get_search.py # Record all the notes
python get_content.py # Get detail comment and body from the notes we get previously
```
