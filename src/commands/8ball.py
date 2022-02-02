@jx.command()
async def magic8ball(ctx):
    response = random.choice([
 "It is certain.",
 "It is decidedly so.",
 "Without a doubt.",
 "Yes definitely.",
 "You may rely on it.",
 "As I see it, yes.",
 "Most likely.",
 "Outlook good.",
 "Yes.",
 "Signs point to yes.",
 "Reply hazy, try again.",
 "Ask again later.",
 "Better not tell you now.",
 "Cannot predict now.",
 "Concentrate and ask again.",
 "Don't count on it.",
 "My reply is no.",
 "My sources say no.",
 "Outlook not so good.",
 "Very doubtful.",
    ])

    embed = discord.Embed(
        colour = discord.Color.blurple(),
        title = ":8ball: The ball predicts.. :8ball:",
        description = f"{response} {ctx.message.author.mention}."
    )

    await ctx.send(embed=embed)