import discord

class InterductionGuides(discord.ui.View):
    def __init__(self):
        super().__init__()
        
    @discord.ui.button(label="More about sublevels")
    async def b1(self, interaction: discord.Interaction, button: discord.Button):
        pass
    
    @discord.ui.button(label="Traversing through places")
    async def b2(self, interaction: discord.Interaction, button: discord.Button):
        pass
    
    @discord.ui.button(label="Starting the reactor")
    async def b3(self, interaction: discord.Interaction, button: discord.Button):
        pass
    
    @discord.ui.button(label="Maintaining the reactor")
    async def b4(self, interaction: discord.Interaction, button: discord.Button):
        pass