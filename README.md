# split_stuff_in_csv
making everyones life easier by receiving an input file and writing a seccond file with the content as csv

Let's suppose you want to get into a sqlite all your linux files you can do something like:

```
find /home -type f | xargs ls -l > fileslist
```

then you can get this file containing the list of files and convert into a CSV with my script and import on sqlite3.

But you can make more stuff like going to some sites copying some tables pasting on a txt file and making it a CSV...
