import asyncio
from email.message import EmailMessage

import aiosmtplib
from more_itertools import chunked

from db import db
from message import msg


async def send_message(person):
    """Coroutine for sending messages."""
    person_email = person.pop('email')
    msg.text = person
    message = EmailMessage()
    message["From"] = "root@localhost"
    message["To"] = person_email
    message["Subject"] = msg.text
    message.set_content("Sent via aiosmtplib")

    await aiosmtplib.send(message, hostname="127.0.0.1", port=1025)


async def main():
    """Coroutine event loop."""
    tasks = [send_message(person) for person in db.persons]
    for chunk_of_tasks in chunked(tasks, 50):
        await asyncio.gather(*chunk_of_tasks)


if __name__ == '__main__':
    asyncio.run(main())
