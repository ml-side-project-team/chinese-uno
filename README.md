# chinese-uno
This repo should allow 6 players to play the game we call chinese uno <br />
Currently we want to implement this with python <br />
Use Num.py for linear algebra stuff later (ml portion) <br />
At first we were thinking of using the Model-View-Controller design pattern to implement this, but in a brain storm we've decided observer-subject pattern would work much better since we can swap out observers that care about different update events and the observers can send back output directly instead of a confusing controller middle man <br />
Player api should have a play method, update method and addScore method <br />
Player can be extended by Machine learning player that uses neural net to calculate what should be played and human player that uses human input to decide what to play <br />