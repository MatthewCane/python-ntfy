import json, requests


def get_cached_messages(self, since: str = "all", scheduled: bool = False):
    """
    Get cached messages from the server

    :param since: The timestamp to start from. If set to "all", will return all messages. Optional
    :param scheduled: If true, will return scheduled messages. Optional
    :return: A list of messages

    :examples:
    response = client.get(since="all")
    response = client.get(since="all", scheduled=True)
    response = client.get(since="2019-01-01")
    response = client.get(since="2019-01-01", scheduled=True)
    """

    params = {"poll": "1"}
    if scheduled:
        params.update({"scheduled": scheduled})
    if since:
        params.update({"since": since})

    response = [
        json.loads(line)
        for line in requests.get(url=self.url + "/json", params=params, auth=self._auth)
        .text.strip()
        .splitlines()
    ]
    # Reverse the list so that the most recent notification is first
    return sorted(response, key=lambda x: x["time"], reverse=True)
