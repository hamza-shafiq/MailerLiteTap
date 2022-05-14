# tap-mailerlite

`tap-mailerlite` is a Singer tap for MailerLite.

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

### Setup:
Clone the git repo through the following command
```
git clone https://github.com/hamza-shafiq/MailerLiteTap.git tap-mailerlite
```

Install required packages to initialize the development environment
```
pip3 install pipx
pipx install poetry
poetry install
```

Run test in order to check your tap is configured successfully
```
poetry run pytest
```

### Now you can test your data streams
1. Discover – this is used to generate a catalog of what tables/endpoints/streams are available from a specific data source. The command to generate a catalog looks like the following:
```
tap-mailerlite --config config.json --discover > catalog.json
```

2. Once the discover is run, the user must select what streams they want to pull
```
singer-discover --input catalog.json --output catalog-selected.json
```

3. Sync – this is used to sync all the available data from the streams you’ve selected from the data source. The command to sync data looks like the following:
```
tap-mailerlite --config config.json --catalog catalog-selected.json > data.txt
```

4. You can then convert the data in the data.txt file to CSVs using target-csv:
```
cat data.txt | target-csv
```

