from requests import get
from io import BytesIO
from random import randint, choice
from PIL import Image, ImageFont, ImageDraw
from textwrap import wrap
from base.module import command, BaseModule
from pyrogram.types import Message

class Amogus(BaseModule):
    @command("amogus")
    async def amogus_cmd(self, _, message: Message):
        tuntun = self.S["amogus"]["tun"]
        clrs = {'red': 1, 'lime': 2, 'green': 3, 'blue': 4, 'cyan': 5, 'brown': 6, 'purple': 7, 'pink': 8, 'orange': 9, 'yellow': 10, 'white': 11, 'black': 12}
        clr = randint(1,12)
        text = " ".join(message.command[1:])

        if message.reply_to_message:
            reply_text = message.reply_to_message.text
            if reply_text:
                text = reply_text

        if message.reply_to_message and len(message.command) > 1:
            text = " ".join(message.command[1:])

        tuntun_message = await message.reply(tuntun)
        
        url = "https://raw.githubusercontent.com/KeyZenD/AmongUs/master/"
        font = ImageFont.truetype(BytesIO(get(url+"bold.ttf").content), 60)
        imposter = Image.open(BytesIO(get(f"{url}{clr}.png").content))
        text_ = "\n".join(["\n".join(wrap(part, 30)) for part in text.split("\n")])
        w, h = ImageDraw.Draw(Image.new("RGB", (1,1))).multiline_textsize(text_, font, stroke_width=2)
        text = Image.new("RGBA", (w+30, h+30))
        ImageDraw.Draw(text).multiline_text((15,15), text_, "#FFF", font, stroke_width=2, stroke_fill="#000")
        w = imposter.width + text.width + 10
        h = max(imposter.height, text.height)
        image = Image.new("RGBA", (w, h))
        image.paste(imposter, (0, h-imposter.height), imposter)
        image.paste(text, (w-text.width, 0), text)
        image.thumbnail((512, 512))
        output = BytesIO()
        output.name = "imposter.webp"
        image.save(output)
        output.seek(0)
        await tuntun_message.delete()
        await message.reply_sticker(sticker=output)