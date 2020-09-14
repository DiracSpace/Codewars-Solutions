#!/usr/bin/env python
import re
def decodeMorse(data):
    decoded_msg = ''
    morse_code_translation = {
        '.-':'A',      '-...':'B',
        '-.-.':'C',    '-..':'D',     '.':'E',
        '..-.':'F',    '--.':'G',     '....':'H',
        '..':'I',      '.---':'J',    '-.-':'K',
        '.-..':'L',    '--':'M',      '-.':'N',
        '---':'O',     '.--.':'P',    '--.-':'Q',
        '.-.':'R',     '...':'S',     '-':'T',
        '..-':'U',     '...-':'V',    '.--':'W',
        '-..-':'X',    '-.--':'Y',    '--..':'Z',
        '.----':'1',   '..---':'2',   '...--':'3',
        '....-':'4',   '.....':'5',   '-....':'6',
        '--...':'7',   '---..':'8',   '----.':'9',
        '-----':'0',   '--..--':',',  '.-.-.-':'.',
        '..--..':'?',  '-..-.':'/',   '-....-':'-',
        '-.--.':'(',   '-.--.-':')',  '*':'*',
        '-.-.--':'!',  '...---...':'SOS' # this is because there isnt proper spacing
    }

    if data == '':
        return ''
    else:
        print (data)
        data = re.sub("   ", " * ", data)
        for code in data.split():
            decoded_msg += morse_code_translation[str(code)]
        return decoded_msg.replace("*", " ").strip()
