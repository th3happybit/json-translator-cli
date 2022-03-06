import requests
import sys, getopt
import json

def translate(input, inputlanguage, outputlanguage):
    
    url = "https://microsoft-translator-text.p.rapidapi.com/translate"

    querystring = {"api-version":"3.0","from": f"{inputlanguage}","to":f"{outputlanguage}","textType":"plain","profanityAction":"NoAction"}

    payload = [{"Text": input}]
    payload = json.dumps(payload, indent=4)
    headers = {
        'content-type': "application/json",
        'x-rapidapi-host': "microsoft-translator-text.p.rapidapi.com",
        'x-rapidapi-key': ""
        }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    resJson = response.json()

    print("Translation: {} -> {}".format(input, resJson[0]['translations'][0]['text']))
    return resJson[0]['translations'][0]['text']

def translate_file(input_file, inputlanguage, output_file, outputlanguage):
    with open(input_file) as json_file:
        data = json.load(json_file)
        translated_data = data.copy()
        for key in data:
            if isinstance(data[key], str):
                translated_data[key] = translate(data[key], inputlanguage, outputlanguage)
        print(translated_data)
        with open(output_file, 'w') as output_json_file:
            json_text = json.dumps(translated_data, indent=2)
            output_json_file.write(json_text)

def main(argv):
    print('translate_cli.py -i <inputfile> -li <input language> -o <outputfile> -lo <output language>')
    inputfile = ''
    outputfile = ''
    languageinput = ''
    languageoutput = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile=", "li=", "lo="])
    except getopt.GetoptError:
        print('translate_cli.py -i <inputfile> --li=<input language> -o <outputfile> --lo=<output language>')
        sys.exit(2)
    print(opts)
    for opt, arg in opts:
        if opt == '-h':
            print('translate_cli.py -i <inputfile> --li=<input language> -o <outputfile> --lo=<output language>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("--li"):
            languageinput = arg
        elif opt in ("--lo"):
            languageoutput = arg
    print('Input file is ', inputfile)
    print('Input language is ', languageinput)
    print('Output file is ', outputfile)
    print('Output languageoutput is ', languageoutput)
    if inputfile and languageinput and languageoutput and outputfile:
        print("Translating...")
        translate_file(inputfile, languageinput, outputfile, languageoutput)

if __name__ == "__main__":
    main(sys.argv[1:])