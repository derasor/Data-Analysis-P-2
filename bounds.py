{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[{'minlat': '49.195', 'maxlon': '-123.02', 'minlon': '-123.29', 'maxlat': '49.32'}]\n"
     ]
    }
   ],
   "source": [
    "\"\"\"Code based on quizzes and exercises from Data Wrangling with MongoDB\"\"\"\n",
    "import xml.etree.ElementTree as ET\n",
    "\n",
    "file = 'vancouver_canada.osm'\n",
    "\n",
    "def get_root(fname):\n",
    "    tree = ET.parse(fname)\n",
    "    return tree.getroot()\n",
    "\n",
    "def get_bounds(root):\n",
    "    bounds = []\n",
    "    # This loop is for generalization;\n",
    "    # it is not necessary in a correct OSM XML file,\n",
    "    # since there should be only one 'bounds' tag\n",
    "    for bound in root.findall('bounds'):\n",
    "        bounds.append(bound.attrib)\n",
    "    return bounds\n",
    "\n",
    "\n",
    "root = get_root(file)\n",
    "bounds = get_bounds(root)\n",
    "print bounds"
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
