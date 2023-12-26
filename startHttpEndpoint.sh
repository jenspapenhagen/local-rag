#!/bin/bash
echo starting the http endpoint under: http://127.0.0.1:5000/process_form
#curl --location '<http://127.0.0.1:5000/process_form>' --form 'query="What does the author think about Star Trek?"'
python httpEndpoint.py
#is there are problems with the db check http://127.0.0.1:6333/dashboard