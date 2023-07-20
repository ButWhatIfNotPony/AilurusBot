import discord
from discord.ext import commands

class Cryptography(commands.Cog):
    """Commands"""
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name='morse', aliases=['morsecode'])
    async def morseCode(self, ctx, *, _method, _message):
        """Encrypts or Decrypts Morse Code messages"""
        # Dictionary representing the morse code chart
        MORSE_CODE_DICT = { 'A': '.-', 'B': '-...', 'C': '-.-.',
                            'D': '-..', 'E': '.', 'F': '..-.',
                            'G': '--.', 'H': '....', 'I': '..', 
                            'J': '---', 'K': '-.-', 'L': '.-..', 
                            'M': '--', 'N': '-.', 'O': '---', 
                            'P': '.--', 'Q': '--.-', 'R': '.-.', 
                            'S': '...', 'T': '-', 'U': '..-', 
                            'V': '...-', 'W': '.--', 'X': '-..-', 
                            'Y': '-.--', 'Z': '--..', '1': '.----', 
                            '2': '..---', '3': '...--', '4': '....-', 
                            '5': '.....', '6': '-....', '7': '--...', 
                            '8': '---..', '9': '----.', '0': '-----', 
                            ', ': '--..--', '.': '.-.-.-', '?': '..--..', 
                            '/': '-..-.', '-': '-....-', '(': '-.--.', 
                            ')': '-.--.-' }
        # Function to encrpyt the string
        # according to the morse code chart
        def encrypt(message):
            cipher = ''
            for letter in message:
                if letter != ' ':
                    # Looks up the dictionary and adds the
                    # corresponding morse code
                    # along with a space to seperate
                    # morse codes for different characters
                    cipher += MORSE_CODE_DICT[letter] + ' '
                else:
                    # 1 space in dicates different characters
                    # and '\' indicate different words
                    cipher += ' '
            return cipher

        # Function to decrypt the string
        # from morse to english
        def decrypt(message):
            # Extra space added at the end to access the
            # last morse code
            message += ' '
            decipher = ''
            citext = ''
            for letter in message:
                # Checks for space
                if (letter != ' '):
                    # Counter to keep track of space
                    i = 0
                    # Storing morse code of a single character
                    citext += letter
                # In case of space
                else:
                    # If i = 1 that indicates a new character
                    i += 1
                    # If i = 2 that indicates a new word
                    if i == 2:
                        # Adding space to seperate words
                        decipher += ' '
                    else:
                        # Accessing the keys using their values (reverse of encryption)
                        decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                        citext = ''
            return decipher


        method = _method.upper()
        message = _message.upper()
        if method == "ENCRYPT" or method == "E":
            encrypted = encrypt(message)
            await ctx.send(f'Your encrypted message is: {encrypted}')
        elif method == "DECRYPT" or method == "D":
            decrypted = decrypt(message)
            await ctx.send(f'Your decrypted message is: {decrypted}')
        else:
            await ctx.send(f'There was an error.. Please check your command input.. :(')
        
        
# The setup function below is neccersary. Remeber we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(Cryptography(bot))