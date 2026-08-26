def response(sentence):
    question = sentence.strip().endswith("?")
    yell = sentence.isupper()
    yell_question = question and yell
    silence = not sentence.strip()
    if silence :
        return "Fine. Be that way!"
    if yell_question :
        return "Calm down, I know what I'm doing!"
    if question :
        return "Sure."
    if yell :
        return "Whoa, chill out!"
    return "Whatever."
