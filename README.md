# My Concerts Bot

@MyConcertsBot is going to suggest you the best concerts in your surroundings in Telegram.

## Usage

Commands to search for concerts of artists:

`/artist Verdena`
`/artist Oasis`

Commands to search for concerts in a city:

`/city Rome`
`/city Amsterdam`



## Development
To generate .env file run this command and fill the data with your information
```bash
cp .env.example .env
```

To create virtual environment run this command
```bash
virtualenv -p python3 env
```

To activate virtual environment
```bash
. env/bin/activate
```

To install depdencencies
```bash
pip3 install -r requirements.txt
```

To deactivate virtual environment
```bash
deactivate
```

### Dependencies
- aiogram
- requests
- autopep8
