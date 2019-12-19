# What's 

Model used [Node2Vec](https://github.com/aditya-grover/node2vec) to embed twitter accounts.
The accounts are restricted to japanese users which have more than 10000 followers.
Data is collected on Oct 2019.


# How to use

download data and model files to `./data/`

- https://drive.google.com/open?id=1Ex0KNd0AE6NoJlb3Jw-6aj5K0dyzUMED
- https://drive.google.com/open?id=17J9wEkVXlfJYTBk-q-dukB98LrdQwSkD
- https://drive.google.com/open?id=1WvYewmS8edolRDAe5eZs-Rw_MI4K06Ar

the graph data used to train is
- https://drive.google.com/open?id=1DabUavG3Kr0AT9iw2cCsIoL5g-HeEG8d

enter venv environment 
```
pip install requirments.txt
```
run 
```
sh start_server.sh
```
