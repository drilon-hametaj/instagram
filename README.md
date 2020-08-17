# instagram
Bot for instagram


In index.py si deve inserire la lista dei profili di instagram su cui il bot deve lavorare

In function -> login, bisogna inserire lo username e password


Funzionamento:
il bot effettua uno shuffle dell'array dei profili, in modo che raramente ci sia lo stesso path. Va a controllare i commenti delle foto e a considerare solo quei commenti
che hanno meno di 5 like. Se ha meno di 5 like, attraverso un generatore di numeri random, decide se mettere like o meno. Sempre con il generatore random, decide se andare a visualizzare
il profilo dell'utente che ha fatto il commento, mettere like a alcuni suoi post, sempre randomicamente decide se seguire o no questa persona
