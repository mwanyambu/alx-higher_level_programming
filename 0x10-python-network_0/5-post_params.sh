#!/bin/bash
#script posts data to server
curl -s -d "email=jmwanyambu@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" -X POST "$1"
