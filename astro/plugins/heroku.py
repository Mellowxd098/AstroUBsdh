
import asyncio
import math
import os

import heroku3
import requests

from astro.helps.heroku_helper import HerokuHelper
from astro.utils import admin_cmd, edit_or_reply, sudo_cmd

Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"


@astro.on(admin_cmd(pattern="(logs|log)"))
@astro.on(sudo_cmd(pattern="(logs|log)", allow_sudo=True))
async def giblog(event):
    herokuHelper = HerokuHelper(Config.HEROKU_APP_NAME, Config.HEROKU_API_KEY)
    logz = herokuHelper.getLog()
    with open("logs.txt", "w") as log:
        log.write(logz)
    await astro.send_file(
        event.chat_id, "logs.txt", caption=f"**Logs Of {Config.HEROKU_APP_NAME}**"
    )


@astro.on(admin_cmd(pattern="(rerun|restarts)"))
@astro.on(sudo_cmd(pattern="(restart|restarts)", allow_sudo=True))
async def restart_me(event):
    herokuHelper = HerokuHelper(Config.HEROKU_APP_NAME, Config.HEROKU_API_KEY)
    await event.edit("`App is Restarting. This is May Take Upto 10Min.`")
    herokuHelper.restart()


@astro.on(admin_cmd(pattern="usage$"))
@astro.on(sudo_cmd(pattern="usage$", allow_sudo=True))
async def dyno_usage(dyno):
    """
    Get your account Dyno Usage
    """
    await edit_or_reply(dyno, "`Trying To Fetch Dyno Usage....`")
    useragent = (
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/80.0.3987.149 Mobile Safari/537.36"
    )
    user_id = Heroku.account().id
    headers = {
        "User-Agent": useragent,
        "Authorization": f"Bearer {Config.HEROKU_API_KEY}",
        "Accept": "application/vnd.heroku+json; version=3.account-quotas",
    }
    path = "/accounts/" + user_id + "/actions/get-quota"
    r = requests.get(heroku_api + path, headers=headers)
    if r.status_code != 200:
        return await edit_or_reply(
            dyno, "`Error: something bad happened`\n\n" f">.`{r.reason}`\n"
        )
    result = r.json()
    quota = result["account_quota"]
    quota_used = result["quota_used"]

    """ - Used - """
    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)

    """ - Current - """
    App = result["apps"]
    try:
        App[0]["quota_used"]
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]["quota_used"] / 60
        AppPercentage = math.floor(App[0]["quota_used"] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)

    await asyncio.sleep(1.5)

    return await edit_or_reply(
        dyno,
        "**Dyno Usage Data**:\n\n"
        f"✗ **APP NAME =>** `{Config.HEROKU_APP_NAME}` \n"
        f"✗ **Usage in Hours And Minutes =>** `{AppHours}h`  `{AppMinutes}m`"
        f"✗ **Usage Percentage =>** [`{AppPercentage} %`]\n"
        "\n\n"
        "✗ **Dyno Remaining This Months 📆:**\n"
        f"✗ `{hours}`**h**  `{minutes}`**m** \n"
        f"✗ **Percentage :-** [`{percentage}`**%**]",
    )


