#!/usr/bin/env python3

import requests


def is_server_up(url):
    try:
        return requests.get(url, timeout=0.5).status_code == 200
    except (requests.ConnectionError, requests.ReadTimeout):
        return False


def status_symbol(up):
    return "🟢" if up else "🔴"
