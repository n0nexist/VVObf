import string

print(""" 
 __   __   __   __   ______     ______     ______  
/\\ \\ / /  /\\ \\ / /  /\\  __ \\   /\\  == \\   /\\  ___\\ 
\\ \\ \\'/   \\ \\ \\'/   \\ \\ \\/\\ \\  \\ \\  __<   \\ \\  __\\ 
 \\ \\__|    \\ \\__|    \\ \\_____\\  \\ \\_____\\  \\ \\_\\   
  \\/_/      \\/_/      \\/_____/   \\/_____/   \\/_/   
> best php 7.4 obfuscator
> coded by n0nexist
""")


letters = string.ascii_letters

other = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "+": "plus",
    "=": "equals",
    "a": "dolluh",
    " ": "space",
    ";": "semicolon",
    "_": "underscore",
    "'": "singlequote",
    "?": "qmark",
    "!": "emark",
    "$": "dool"
}

def get_var(text):
    temp = "${"
    for x in text:
        temp += get_char(x)+" ."
    temp = temp[:-2]
    temp += "}"
    return temp.replace("}; .","} .")

def get_char(findme):
    c = 0
    if findme != "a" and findme in letters:
        for x in letters:
            if x==findme:
                return ("$"*c)+"a"
                break
            c+=1
    else:
        return get_var(other[findme])

def get_sentence(text):
    formed = ""
    for x in text:
        try:
            formed += get_char(x)
        except KeyError:
            if x == '"':
                x = "\\\""
            elif x == "\\":
                x = "\\\\"
            formed += f"\"{x}\""
        formed += "."
    formed = formed[:-1]
    return formed

code = input("paste your line of code: ")    
output = input("output file: ")

print("* obfuscating..")
obf = ""
try:
    obf = get_sentence(code)
except Exception as ee:
    print("error while obfuscating: "+str(ee))
    exit()
print("* saving to file..")
template = "<?php extract(array_combine(range(base64_decode(\"YQ==\"), base64_decode(\"eQ==\")), range(base64_decode(\"Yg==\"), base64_decode(\"eg==\"))));$z = base64_decode(\"QQ==\");extract(array_combine(range('A', 'Y'), range('B', 'Z')));extract(array(base64_decode(\"emVybw==\") => base64_decode(\"MA==\"),base64_decode(\"b25l\") => base64_decode(\"MQ==\"), base64_decode(\"dHdv\") => base64_decode(\"Mg==\"), base64_decode(\"dGhyZWU=\") => base64_decode(\"Mw==\"), base64_decode(\"Zm91cg==\") => base64_decode(\"NA==\"), base64_decode(\"Zml2ZQ==\") => base64_decode(\"NQ==\"), base64_decode(\"c2l4\") => base64_decode(\"Ng==\"), base64_decode(\"c2V2ZW4=\") => base64_decode(\"Nw==\"), base64_decode(\"ZWlnaHQ=\") => base64_decode(\"OA==\"), base64_decode(\"bmluZQ==\") => base64_decode(\"OQ==\"), base64_decode(\"cGx1cw==\") => base64_decode(\"Kw==\"), base64_decode(\"ZXF1YWxz\") => base64_decode(\"PQ==\"), base64_decode(\"ZG9sbHVo\") => base64_decode(\"YQ==\"), base64_decode(\"c3BhY2U=\") => base64_decode(\"IA==\"), base64_decode(\"c2VtaWNvbG9u\") => base64_decode(\"Ow==\"), base64_decode(\"dW5kZXJzY29yZQ==\") => base64_decode(\"Xw==\"), base64_decode(\"c2luZ2xlcXVvdGU=\") => base64_decode(\"Jw==\"), base64_decode(\"cW1hcms=\") => base64_decode(\"Pw==\"), base64_decode(\"ZW1hcms=\") => base64_decode(\"IQ==\"), base64_decode(\"ZG9vbA==\") => base64_decode(\"JA==\")));(($$a . $$$$$$$$$$$$$$$$$a . $$$$a . ${$$$a . $$$$$$$$$$$$$$a . $$$$$$$$$$$a . $$$$$$$$$$$a . $$$$$$$$$$$$$$$$$$$$a . $$$$$$$a} . $$$$$$$$$$$$$$$$$$$a . $$$$a . ${$$$$$$$$$$$$$$$$$$$$a . $$$$$$$$$$$$$a . $$$a . $$$$a . $$$$$$$$$$$$$$$$$a . $$$$$$$$$$$$$$$$$$a . $$a . $$$$$$$$$$$$$$a . $$$$$$$$$$$$$$$$$a . $$$$a} . $$$$$a . $$$$$$$$$$$$$$$$$$$$a . $$$$$$$$$$$$$a . $$a . $$$$$$$$$$$$$$$$$$$a . $$$$$$$$a . $$$$$$$$$$$$$$a . $$$$$$$$$$$$$a)(\"\","+obf+"))();?>"
try:
    f = open(output,"w")
    f.write(template)
    f.close()
except Exception as e:
    print("error while saving to file: "+str(e))
    exit()

print("! done")