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
      "{'lower': 128727, 'lower_colon': 9732, 'other': 2675, 'problemchars': 10}\n"
     ]
    }
   ],
   "source": [
    "\"\"\"Code based on quizzes and exercises from Data Wrangling with MongoDB\"\"\"\n",
    "import xml.etree.cElementTree as ET\n",
    "import pprint\n",
    "import re\n",
    "\n",
    "lower = re.compile(r'^([a-z]|_)*$')\n",
    "lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')\n",
    "problemchars = re.compile(r'[=\\+/&<>;\\'\"\\?%#$@\\,\\. \\t\\r\\n]')\n",
    "\n",
    "\n",
    "def key_type(element, keys):\n",
    "    if element.tag == \"tag\":\n",
    "        # \n",
    "        l = lower.search(element.attrib['k'])\n",
    "        l_c = lower_colon.search(element.attrib['k'])\n",
    "        p = problemchars.search(element.attrib['k'])\n",
    "        if l:\n",
    "            keys[\"lower\"] += 1\n",
    "        elif l_c:\n",
    "            keys[\"lower_colon\"] += 1\n",
    "        elif p:\n",
    "            keys[\"problemchars\"] += 1\n",
    "        else:\n",
    "            keys[\"other\"] += 1\n",
    "        pass\n",
    "    #    \n",
    "    return keys\n",
    "\n",
    "\n",
    "\n",
    "def process_map(filename):\n",
    "    keys = {\"lower\": 0, \"lower_colon\": 0, \"problemchars\": 0, \"other\": 0}\n",
    "    for _, element in ET.iterparse(filename):\n",
    "        keys = key_type(element, keys)\n",
    "\n",
    "    return keys\n",
    "\n",
    "\n",
    "\n",
    "def test():\n",
    "    keys = process_map('vancouver_canada.osm')\n",
    "    pprint.pprint(keys)\n",
    "\n",
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
