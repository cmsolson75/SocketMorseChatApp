from playsound import playsound

morse_key = {"a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".", "f":"..-.", "g":"--.", "h":"....", "i":"..", "j":".---", "k":"-.-", "l":".-..", "m":"--", "n":"-.", "o":"---", "p":".--.", "q":"--.-", "r":".-.", "s":"...", "t":"-", "u":"..-", "v":"...-", "w":".--", "x":"-..-", "y":"-.--", "z":"--..", "1":".----", "2":"..---", "3":"...--", "4":"....-", "5":".....", "6":"-....", "7":"--...", "8":"---..", "9":"----.", "0":"-----", " ": " "}
sound_key = {".":"audio_files/short.wav","-":"audio_files/long.wav", " ":"audio_files/pause.wav"}

def translate_morse(char) -> str:
    """
    returns None if cannot translate character
    """
    return morse_key[char]

def play_morse(morse):
    for char in morse:
        playsound(sound_key[char])

def output_morse(string):
    pause_sound = "audio_files/pause.wav"
    for char in string.lower():
        if char in morse_key:
            translated = translate_morse(char)
            print(translated, end="", flush=True)
            play_morse(translated)
            playsound(pause_sound)

    print()

if __name__ == "__main__":
    while True:
        user_input = input("translate: ")
        output_morse(user_input)
        user_question = input("Type y to exit or press enter not to exit: ")
        if user_question.lower() == "y":
            break
