{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'bounds': 1,\n",
      " 'member': 6328,\n",
      " 'nd': 481596,\n",
      " 'node': 387599,\n",
      " 'osm': 1,\n",
      " 'relation': 690,\n",
      " 'tag': 141144,\n",
      " 'way': 67187}\n"
     ]
    }
   ],
   "source": [
    "\"\"\"Code based on quizzes and exercises from Data Wrangling with MongoDB\"\"\"\n",
    "import xml.etree.cElementTree as ET\n",
    "import pprint\n",
    "\n",
    "def count_tags(filename):\n",
    "        # Dictionary with the tag name as the key \n",
    "        # and number of times each tag can be encountered \n",
    "        # in the osm-xml file as value.\n",
    "        tags = {}\n",
    "        # Parse through all tags \n",
    "        for event, elem in ET.iterparse(filename):\n",
    "            if elem.tag in tags:\n",
    "                tags[elem.tag] += 1\n",
    "            else:\n",
    "                tags[elem.tag] = 1\n",
    "        return tags\n",
    "                \n",
    "def test():\n",
    "    tags = count_tags('vancouver_canada.osm')\n",
    "    pprint.pprint(tags)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    test()"
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
