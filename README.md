The code is run in a docker environment. To build the container run "docker compose up --build" and to connect to bash run "docker compose exec dev-env bash".
Put your pdf files in a folder named PDFs and run parser.py to get the text files inside another folder named processed_texts. Now you can choose each of the texts inside the extractor.py file and extract the information running the code.

--Warning: In order to access openAI's API you'd need a key. It's recommended to add a file called .env and add the key inside it.