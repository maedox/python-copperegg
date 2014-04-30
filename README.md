# A Python wrapper for the CopperEgg API.

**Here be dragons:**

This software has the ability to modify all your data through the CopperEgg API.

Make sure you have read and understood the code before using it for any purpose.

## Features

- Listing and updating probes.

### Coming soon
- Listing and editing probes by tag

Let me know if there are features you would like to see.

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

### Find probes by tag

#### Match probes tagged "dev" or "test":

	copperegg-cli --get-tags dev test

#### Match probes tagged "demo":

	copperegg-cli --get-tags demo

### Modifying probes

#### Enable or disable probes

	copperegg-cli --get-probes [probe id] --set-state enabled

	copperegg-cli --get-probes [probe id] --set-state disabled

- Disable all probes tagged "dev":

	copperegg-cli --get-tags dev --set-state disabled

#### Add all stations to demo probes

	copperegg-cli --get-tags demo --set-stations all

#### List available stations

	copperegg-cli --help-stations

#### Replace any stations with a specific list

	copperegg-cli --get-tags dev --set-stations lon amd nrk --replace-stations

*Coming soon: The ability to use regions names.*

## Disclaimer
*I am in no way affiliated with CopperEgg.*

- This software is provided as is.
- It should be safe, but don't blame me if something breaks.
- It is written and tested for use on GNU/Linux with Python 2.7+, 3.3+.

## CopperEgg API documentation
http://dev.copperegg.com/
