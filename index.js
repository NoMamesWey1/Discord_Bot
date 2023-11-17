//setting up the connection
const mySecret = process.env['DISCORD BOT']//put your token here or hide it and call it like i did
const { Client,GatewayIntentBits } = require('discord.js')
require('discord-reply');
const client = new Client({
    intents: [GatewayIntentBits.Guilds,GatewayIntentBits.GuildMessages,GatewayIntentBits.MessageContent,GatewayIntentBits.GuildMembers,]
})
//displays on the console the bot
client.on("ready", () => {
  console.log(`Logged in as ${client.user.tag}!`)
})
//tells user bots online
if (client.on) {
  ("Hello! Bot is now online!")
}
//if it equals a certain message, it will respond
client.on("messageCreate", (message) => {
  if (message.content === 'ping' && message.author.id == 'YOUR CHANNEL ID') {
    message.channel.send('pong');
  }
})
//has the bot check for a certain message, deletes user message, and sends what the user put after bot say
client.on('messageCreate', message => {
   if (message.content.startsWith("bot say ")) {
      message.delete(1000); //Supposed to delete message
      message.channel.send(message.content.slice(7, message.content.length));
   }
});

client.login(mySecret)

