from telethon.tl.types import (
    ChannelParticipantsKicked,
)

from userbot.events import edit_or_reply, kyy_cmd
from userbot import CMD_HELP, CMD_HANDLER as cmd


@kyy_cmd(outgoing=True, pattern=r"^\.allunban(?: |$)(.*)", groups_only=True)
async def _(event):
    xx = await edit_or_reply("`Sedang Mencari List Banning.`")
    p = 0
    (await event.get_chat()).title
    async for i in event.client.iter_participants(
        event.chat_id,
        filter=ChannelParticipantsKicked,
        aggressive=True,
    ):
        try:
            await event.client.edit_permissions(event.chat_id, i, view_messages=True)
            p += 1
        except BaseException:
            pass
    await event.edit("`Sukses Menghapus List Banning`")


CMD_HELP.update(
    {
        "allunban": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.allunban`\
    \n↳ : Membatalkan semua Ban Di Anggota Grup."
    }
)
