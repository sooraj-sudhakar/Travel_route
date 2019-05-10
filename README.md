# Travel route
<img src="https://github.com/sooraj-sudhakar/Travel_route/blob/master/Misc/underprogress.jpg" width="78">

This works is intended to make the journey for the travellers much easier. This work helps in :
- Recommending frequently visited places.
- Informing the tourist beforehand regarding the difficulties associated with the route.

This is work makes use of the **custom entity extraction** from the user **reviews** using the **RASA nlu** module and then generating a difficulty score based on the positive and negative words from the reviews. 
### Dependancy
The main dependancy for this work would be RASA installation and nodejs (for acessing the gui based rasa trainer for input data tagging). If *Anaconda* package is installed by default then you wont need to install any other modules. 
```sh
pip install -r requirements.txt
pip install rasa_nlu
pip install rasa_nlu[spacy]
python -m spacy download en_core_web_md
python -m spacy link en_core_web_md en
pip install nodejs
npm i -g rasa-nlu-trainer
```
