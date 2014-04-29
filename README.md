# A Python wrapper for the CopperEgg API.

**Here be dragons:**
*This software has the ability to modify all your data through the CopperEgg API.
Make sure you have read and understood the code before using it for any purpose.*

## Features

- Listing and updating probes.

Listing and editing probes by tag is coming soon.
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

## Usage

	import copperegg
	api = copperegg.CopperEgg()

### Listing probes

	api.list_probes()

### Get info on a specific probe

	api.get_probe(probe_id)

### Update any probe field
Set the check interval to 15 seconds for probe_id:

	api.update_probe(probe_id, {"frequency": 15})

## Disclaimer
*I am in no way affiliated with CopperEgg.*

This software is provided as is.
It should be safe, but don't blame me if something breaks.
It is written and tested for use on GNU/Linux with Python 2.7+, 3.3+.

## CopperEgg API documentation
http://dev.copperegg.com/
