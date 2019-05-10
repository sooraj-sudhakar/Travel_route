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
Sample:
> *During our journey from Trivandrum to Thrissur, the road was in **good** condition, the weather was **fine** and the traffic was **less** during the wee hours. There was **lot** of restaurants and mall nearby Kochi area.*

<img src="https://github.com/sooraj-sudhakar/Travel_route/blob/master/data_taggin.gif" width="1024">

### Working
The tagged data will be saved as json format. This json format will be then taken as input file for training by the rasa module.The training can be started by running `train.py` and the trained model will be saved in the projects folder.The testing is done by running the `test.py`. During the testing phase, the trained model will be loaded and a sample sentence will be passed to the testing module. The module returns a json format with intents and entities. 

<img src="https://github.com/sooraj-sudhakar/Travel_route/blob/master/output.png" width="1024">

The word polarities(using nltk) of the entities will be used to calculated a score and in this manner the total score will be calculated. The difficulty score ranges from 0-5, 5 being the most difficult to travel. The score from each individual review in that route will be then averaged to get the overall difficulty score in that specified route. 
### Sample output

| Input text | Road condition |Traffic condition | Scenary data | Weather condition | Difficulty score |
| ------ | ------ | ------ | ------ | ------ | ------ |
| the traffic from thrissur to kochi was fine and weather is good |0 |fine |0 |good |2.8125
| There was few restuarants on the way from Kollam to Kottayam,the road was smooth and then traffic was less. |smooth |less |few restuarants |0 |1.4137
