while True:
    text = input("Enter a string: ")

    if text.isalpha():
        reversed_text = ''.join(reversed(text))
        print("Output:", reversed_text)
        break
    else:
        print("Error Reported! Enter text only.")


