{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "\"\"\"Code based on quizzes and exercises from Data Wrangling with MongoDB\"\"\"\n",
    "import json\n",
    "\n",
    "def insert_data(data, db):\n",
    "    # Insert the data into a collection 'vancouver'\n",
    "    db.vancouver.insert(data)\n",
    "        \n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    from pymongo import MongoClient\n",
    "    client = MongoClient(\"mongodb://localhost:27017\")\n",
    "    db = client.osm\n",
    "\n",
    "    with open('my_vancouver.xml.json') as f:\n",
    "        data = json.loads(f.read())\n",
    "        insert_data(data, db)\n",
    "        #print db.vancouver.find_one()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
