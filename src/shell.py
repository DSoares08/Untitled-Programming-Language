import ciepseudocode

while True:
    text = input('ciepseudocode > ')
    result, error = ciepseudocode.run('<stdin>', text)

    if error:
        print(error.as_string)
    else:
        print(result)
