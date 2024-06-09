print("Make Your Story by filling []")
print("**********************************************************************")
print("Yesterday, I woke up feeling very [adjective].\n"
      "I decided to make myself a delicious breakfast of [noun] and [noun].\n"
      "While I was eating, a [noun] flew right by my window!\n"
      "I chased it outside as fast as my [body part] could go,\n"
      "but it disappeared into the [place].\n"
      "The rest of the day was pretty uneventful, but it was definitely an [adjective] morning!")
print("**********************************************************************")
adjective1, noun1, noun2, noun3, body_part, place, adjective2 = input("Enter your name and age separated by , : ").split(sep=",")

print(f"Fill the blank \n Yesterday, I woke up feeling very {adjective1}."
      f"\n I decided to make myself a delicious breakfast of {noun1} and {noun2}."
      f"\n While I was eating, a {noun3} flew right by my window!"
      f"\n I chased it outside as fast as my {body_part} could go, "
      f"\n but it disappeared into the {place}."
      f"\n The rest of the day was pretty uneventful, but it was definitely an {adjective2} morning!")
