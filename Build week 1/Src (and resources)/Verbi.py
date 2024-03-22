import requests
import importlib.util
import os

# Carica la lingua da config.py
language_spec = importlib.util.spec_from_file_location("config", "config.py")
config = importlib.util.module_from_spec(language_spec)
language_spec.loader.exec_module(config)

def check_http_verbs(url):
    supported_verbs = []

    try:
        response = requests.options(url)
        if response.status_code == 200:
            supported_verbs.append('OPTIONS')
    except requests.exceptions.RequestException:
        pass

    try:
        response = requests.get(url)
        if response.status_code == 200:
            supported_verbs.append('GET')
    except requests.exceptions.RequestException:
        pass

    try:
        response = requests.head(url)
        if response.status_code == 200:
            supported_verbs.append('HEAD')
    except requests.exceptions.RequestException:
        pass

    try:
        response = requests.post(url)
        if response.status_code == 200:
            supported_verbs.append('POST')
    except requests.exceptions.RequestException:
        pass

    try:
        response = requests.put(url)
        if response.status_code == 200:
            supported_verbs.append('PUT')
    except requests.exceptions.RequestException:
        pass

    try:
        response = requests.delete(url)
        if response.status_code == 200:
            supported_verbs.append('DELETE')
    except requests.exceptions.RequestException:
        pass

    return supported_verbs