from slack import WebClient
import time


# TODO: consider creating default fail/success messages
# that includes name of job, timestamp, and fail or success emoji


class SlackEngine:
    def __init__(
        self, job_name="Default-Job-Name", api_token="", job_emoji=":computer:"
    ):

        self.job_name = job_name
        self.client = WebClient(token=api_token)
        self.job_emoji = job_emoji
        return

    def send_message(self, group, message):
        for user in group:
            try:
                response = self.client.chat_postMessage(
                    username=self.job_name,
                    channel=user,
                    text=message,
                    icon_emoji=self.job_emoji,
                )
            except Exception as e:
                print(e)

        return
