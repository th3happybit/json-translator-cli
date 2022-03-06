# json-translator-cli
simple cli to translate your json i18n files

1. GET api key from: [Rapid api ms translator](https://rapidapi.com/microsoft-azure-org-microsoft-cognitive-services/api/microsoft-translator-text/)
2.  `pip install -r requirements.txt`
3.  `python translate_cli.py -h`

### Usage:
`python translate_cli.py -i <inputfile> --li=<input language> -o <outputfile> --lo=<output language>`

### Example:

`python translate_cli.py -i common.json -o common_fr.json --li=en --lo=fr`

### Contributing
Please feel free to fork this package and contribute by submitting a pull request to enhance the functionalities.
