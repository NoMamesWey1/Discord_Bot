import random

roast = ["1. I’m not saying you’re ugly, but if I throw a stick, you fetch and bring it back.",
"2. Before we start, dude, you’ve got something on your chin … no, not that one … nope, keep going.",
"3. If your brain was made of dynamite, you couldn’t even blow your nose!",
"4. I’m not saying you’re boring, but if you’re a gray sprinkle on a rainbow cupcake!",
"5. You and I go way back, and you’ve always been annoying. I mean, you even used to make your happy meal cry.",
"6. We’ve been happily married for three months; shame it’s taken ten years to hit that number.",
"7. I know our son got his brains from you because, well, I still have mine.",
"8. The only reason I take you everywhere with me is that I’d rather do that than kiss your ugly face goodbye.",
"9. You love to act stupid. I know because I live with you, you’re naturally way dumber than that.",
"10. You’re so ugly your face makes onions cry!",
"11. Roasting you isn’t easy. It’s hard enough to imagine you with a personality.",
"12. I’m not saying you’re ugly, but you’re the reason God created miscarriages!",
"13. Give me a minute; I’m trying to think of an insult that’s dumb enough for you to understand!",
"14. I’m not saying you’re ugly, but the reason nobody wants to sleep with you is that they don’t want to be prosecuted for animal abuse.",
"15. You’ve got so many gaps in your teeth it looks like your tongue is in jail.",
"16. Maybe you should try to eat make-up to improve your ugly personality.",
"17. I know it looks like I’m listening to you, but really I’m just visualizing duck tape over your mouth.",
"18. This will be the first and last roast of the night, as we’ve already used up your entire vocabulary.",
"19. Do you know the best part about being your friend? Not having to see you all the time.",
"20. You’re the reason the gene pool should really have lifeguards.",
"21. The only way you’d get hurt from doing exercise would be if you sprained your finger, changing the channel.",
"22. Some might call you a smart ass, others a dumb ass; I say you’re just an ass.",
"23. It’s a parents job to raise their children right. So looking at you, it’s no wonder your dad quit after just one day.",
"24. Your bad personality is the reason I prefer animals to humans.",
"25. There’s somebody out there for everybody. For you, it’s a psychiatrist.",
"26. You’re so annoying; it’s because of you God gave us all a middle finger.",
"27. I’ve heard a smarter statement come out in a fart.",
"28. I’m sorry that this roast uses your entire vocabulary.",
"29. I would explain all of these roasts to you, but I forgot to bring you an English to dumbass dictionary.",
"30. I’d give you a nasty look but you’ve already got one.",
"31. You’re more disappointing than an unsalted pretzel.",
"32. I’m not saying you’re a commitment-phobe, but baby, my phone battery lasts longer than your relationships.",
"33. I don’t want to be mean, but babe, my hair straightener is hotter than you are.",
"34. I was going to stand here and make a joke about your life, but hey, it looks like life got there first.",
"35. It must be fun to wake up each morning knowing that you are that much closer to achieving your dreams of complete and utter mediocrity.",
"36. You’re such a momma’s boy, but newsflash, that makes you a son, not a sun, so stop thinking the earth revolves around you.",
"37. Accidents happen; the proof is sitting right there.",
"38. You’re so irritating you should come with a warning label.",
"39. Everyone is entitled to one, but yours is always the incorrect opinion.",
"40. Whenever you open your mouth, it’s like, ‘Woah, somebody took too many drugs this morning.",
"41. Every day I hope you get your chapstick confused with a glue stick so I can get a bit of peace and quiet.",
"42. You’re like the human version of athlete’s foot – annoying and hard to get rid of.",
"43. If you ever feel suicidal, at least you can jump off your own ego.",
"44. If your mum got given one piece of bad advice, it was not to swallow.",
"45. I believe you can achieve anything. Look around you; there are remarkably dumb people everywhere who you could aspire to be.",
"46. I’m not saying you’re ugly, but my baby’s diaper rash is nicer to look at.",
"47. We’ve been best friends a long time, but you’re the reason they put external use only on shampoo bottles.",
"48. And the best part of our relationship is the fact that you are no longer in it.",
"49. It’s not that you’re annoying; it’s just that I’d liken you to the human version of period cramps.",
"50. I would call you an idiot, but that would be a horrible insult to stupid people everywhere.",
"51. We were going to roast you, but apparently, it’s not good for the environment to burn trash.",
"52. I bet I could remove 90 percent of your good looks with a moist towelette.",
"53. I’m so sorry if my brutal honesty inconvenienced your overinflated sense of self.",
"54. It’s not that I don’t listen to you when you talk. It’s just that there is only so much stupid information I can process in one go.",
"55. I’m not an astronomer, but I am pretty sure the world revolves around the sun and not you.",
"56. You might look attractive, but I’d have to put a paper bag over that personality.",
"57. Everybody brings happiness to a room. You just do it when you leave!",
"58. You remind me of a cloud; when you disappear, my day gets that much brighter.",
"59. Your birth certificate should be a letter of apology from Durex.",
"60. Light travels faster than sound. This must be why you appear bright until you open your mouth."]

def get_response(message: str) -> str:
    msg = message.lower()
    # greeting
    if msg == 'hello':
        greetings = ['Hey there!','Hello','Bonjour','Hola','What do you want!?','Como puedo ayudar','What do you need?']
        return greetings[random.randint(0,len(greetings))]

    #rolling a random num 1-100
    if msg == 'roll':
        word = str(random.randint(1,100))
        word = 'The number you rolled is '+word
        return word

    # give list of commands the bot can do 
    if msg == '!help':
        return '`List of Commands:\n1.type hello - bot will respond with a greeting\n2.type roll- roll a random number between 1-100\n3.type roast - roast people`'

    # roast people. find a list of roast
    if msg == 'roast':
        return roast[random.randint(1,len(roast))]

    #turns bot offline  
    if msg == 'bot go offline':
        return 'Bot Offline'
  


    