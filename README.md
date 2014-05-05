# A Python wrapper for the CopperEgg API.

**Here be dragons:**

This software has the ability to modify all your data through the CopperEgg API.

Make sure you have read and understood the code before using it for any purpose.

## Features

- Listing, updating, adding and deleting probes.
- Set stations, tags and more.
- Enable stations by region

### Recently added
- Search for probes by name using case-insensitive regexp's, substring search.

### Coming soon
- Allow changing all possible settings for a probe

Let me know if there are features you would like to see in the future.

## Requirements
- A CopperEgg account and API token.
- Python 2.7+, 3.3+
- Requests (http://docs.python-requests.org/)

## Installation

    sudo python setup.py install

OR

	sudo python3 setup.py install

Append this to ~/.netrc to enable automatic authentication with your API token:

	machine api.copperegg.com login [your token] password U

## Module usage

	import copperegg
	api = copperegg.CopperEgg()

### Listing probes

	api.list_probes()

### Get info on a specific probe

	api.get_probe(probe_id)

### Update any probe field
Set the check interval to 15 seconds for probe_id:

	api.update_probe(probe_id, {"frequency": 15})

## Command-line usage

**Note the --noop argument which should make this utility quite safe.
Adding --noop will just print what would be done without actually making
any requests to the CopperEgg API. Pay close attention to your CLI arguments
and when in doubt, use --noop.**

### View available commands

	copperegg-cli --help

### Logging and standard output verbosity
By default copperegg-cli will print log messages to stdout and to ~/.copperegg-cli.log
There are a few ways to change this behavior.

#### Disable stdout printing

	copperegg-cli --silent

#### Change log level

	copperegg-cli --log-level DEBUG

	copperegg-cli --log-level WARNING

### View all probes

	copperegg-cli --get-probes all

Or for more verbose output:

	copperegg-cli --get-probes all --log-level DEBUG | less

### Finding probes
You may supply multiple filters for the --get- arguments.

#### Find all probes where the name contains "test"

	copperegg-cli --get-names test

#### Find all probes tagged or where the name starts with "production"

	copperegg-cli --get-names '^production' --get-tags production

#### Match probes tagged "dev" or "test":

	copperegg-cli --get-tags dev test

#### Match probes tagged "demo":

	copperegg-cli --get-tags demo

### Modifying probes
Tip: Add the --noop argument to see changes without actually applying them.

#### If probe name starts with "dev", tag it "dev" and check every 300 seconds

	copperegg-cli --get-names '^dev' --set-tags dev --set-frequency 300

#### Enable or disable probes

	copperegg-cli --get-probes [probe id] --set-state enabled

	copperegg-cli --get-probes [probe id] --set-state disabled

Disable all probes tagged "dev":

	copperegg-cli --get-tags dev --set-state disabled

#### Add all stations to demo probes

	copperegg-cli --get-tags demo --set-stations all

#### List available stations

	copperegg-cli --help-stations

#### Replace any stations with a specific list

	copperegg-cli --get-tags dev --set-stations lon amd nrk --replace-stations

*New:* You can now use region names too. Here's how to enable EU, APAC and Newark:

	copperegg-cli --get-tags dev --set-stations eu apac nrk

If you want to enable stations in EU only:

	copperegg-cli --get-tags dev --set-stations eu --replace-stations

## Disclaimer
*I am in no way affiliated with CopperEgg.*

- This software is provided as is.
- It should be safe, but don't blame me if something breaks.
- It is written and tested for use on GNU/Linux with Python 2.7+, 3.3+.

## CopperEgg API documentation
http://dev.copperegg.com/
