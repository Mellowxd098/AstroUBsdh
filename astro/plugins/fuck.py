"""

Available Commands:

.sux

.fuk

.kiss"""


import asyncio

from astro import CMD_HELP
from astro.utils import admin_cmd


@astro.on(admin_cmd(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 101)

    input_str = event.pattern_match.group(1)

    if input_str == "fuk":

        await event.edit(input_str)

        animation_chars = ["👉       ✊️", "👉     ✊️", "👉  ✊️", "👉✊️💦"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 4])


@astro.on(admin_cmd(pattern=r"(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.2

    animation_ttl = range(0, 101)

    input_str = event.pattern_match.group(1)

    if input_str == "sux":

        await event.edit(input_str)

        animation_chars = ["🤵       👰", "🤵     👰", "🤵  👰", "🤵👼👰"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 4])


""


@astro.on(admin_cmd(pattern=r"(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.2

    animation_ttl = range(0, 101)

    input_str = event.pattern_match.group(1)

    if input_str == "kiss":

        await event.edit(input_str)

        animation_chars = ["🤵       👰", "🤵     👰", "🤵  👰", "🤵💋👰"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 4])


CMD_HELP.update({"fuck": "Nothing to say.\n.fuk\n.sux\n.kiss"})
