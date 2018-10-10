# equihashverify
nodejs native binding to check for valid Equihash solutions

## Dependencies
````bash
sudo apt-get install build-essential libsodium-dev libboost-system-dev
````

## Usage
````javascript
var ev = require('bindings')('equihashverify.node');

var header = new Buffer(..., 'hex');
var solution = new Buffer(..., 'hex'); //do not include byte size preamble "fd4005"

ev.verify(header, solution, n, k);
//returns boolean
````

## Backward compatibility
````javascript
ev.verify(header, solution);
````

## Test Suite:
````bash
sudo npm install -g mocha
npm install
mocha
````

## Help

* Discord: https://discord.gg/45NNrMJ

* Email: team[at]zclassic-ce.org - vulnerability disclosure policy is explained [here](DISCLOSURE.md).
