import discord
from bot_logic import gen_pass, coin_throw

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

password = ""

@client.event
async def on_ready():
    print(f'Señor hemos iniciado como {client.user}')

@client.event
async def on_message(message):
    global password  

    if message.author == client.user:
        return

    if message.content.startswith('$hola'):
        await message.channel.send("¡Hola!")
    elif message.content.startswith('$adios'):
        await message.channel.send("¡Adios!")
    elif message.content.startswith("$password"):
        if not password:  # Check if no password is generated
            password = gen_pass(15)
            await message.channel.send("Nueva contraseña generada!")
        else:
            await message.channel.send("Ya tienes una contraseña generada.")
    elif message.content.startswith("$throw_coin"):
        result = coin_throw()
        await message.channel.send(result)
    elif message.content.startswith("info"):
        info_message = (
            "¡Hola! Soy un bot que puede generar contraseñas, lanzar una moneda, saludarte y despedirme.\n"
            "Puedes usar los siguientes comandos:\n"
            "- `$hola`: Para saludarme.\n"
            "- `$adios`: Para despedirte.\n"
            "- `$password`: Genera una nueva contraseña o muestra la actual si ya fue generada.\n"
            "- `$throw_coin`: Lanza una moneda para obtener cara o cruz.\n"
        )
        await message.channel.send(info_message)
    elif password and message.content.startswith("password"):
        await message.channel.send("Tu contraseña es " + password)
    else:
        await message.channel.send("No tienes todavía una contraseña generada. Escribe `$password` para generar una y luego pregúntame de nuevo.")

client.run("TOKEN")
