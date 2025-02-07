import nextcord
from nextcord import Interaction, SlashOption

TESTING_GUILD_ID = 123456789  # Replace with your testing guild id

client = nextcord.Client()


@client.slash_command(guild_ids=[TESTING_GUILD_ID])
async def choose_a_number(
    interaction: Interaction,
    number: int = SlashOption(
        name="picker",
        description="The number you want",
        choices={"one": 1, "two": 2, "three": 3},
    ),
):
    await interaction.response.send_message(f"You chose {number}!")


@client.slash_command(guild_ids=[TESTING_GUILD_ID])
async def hi(
    interaction: Interaction,
    member: nextcord.Member = SlashOption(name="user", description="User to say hi to"),
):
    await interaction.response.send_message(
        f"{interaction.user} just said hi to {member.mention}"
    )


client.run("token")
