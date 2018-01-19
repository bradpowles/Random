def takeInput(message):
    try:
        reply = raw_input(message)
    except:
        reply = input(message)
    return reply
