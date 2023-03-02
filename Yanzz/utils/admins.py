from typing import Callable

from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message

from Yanzz import DEV_USERS, DRAGONS, pbot


def can_change_info(func: Callable) -> Callable:
    async def non_admin(_, message: Message):
        if message.from_user.id in DRAGONS:
            return await func(_, message)

        check = await pbot.get_chat_member(message.chat.id, message.from_user.id)
        if check.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            return await message.reply_text(
                "» ᴋᴀᴍᴜ ʙᴜᴋᴀɴ ᴀᴅᴍɪɴ sᴀʏᴀɴɢ."
            )

        admin = (
            await pbot.get_chat_member(message.chat.id, message.from_user.id)
        ).privileges
        if admin.can_change_info:
            return await func(_, message)
        else:
            return await message.reply_text(
                "`Anda tidak memiliki izin untuk mengubah info grup."
            )

    return non_admin


def can_restrict(func: Callable) -> Callable:
    async def non_admin(_, message: Message):
        if message.from_user.id in DEV_USERS:
            return await func(_, message)

        check = await pbot.get_chat_member(message.chat.id, message.from_user.id)
        if check.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            return await message.reply_text(
                "» ᴋᴀᴍᴜ ʙᴜᴋᴀɴ ᴀᴅᴍɪɴ sᴀʏᴀɴɢ."
            )

        admin = (
            await pbot.get_chat_member(message.chat.id, message.from_user.id)
        ).privileges
        if admin.can_restrict_members:
            return await func(_, message)
        else:
            return await message.reply_text(
                "`Anda tidak memiliki izin untuk membatasi pengguna di chat ini."
            )

    return non_admin
