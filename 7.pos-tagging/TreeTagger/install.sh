#!/bin/bash

# get Linux tagger package
wget https://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/data/tree-tagger-linux-3.2.4.tar.gz

# get tagging scripts
wget https://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/data/tagger-scripts.tar.gz

# get parameter files
wget https://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/data/english.par.gz
wget https://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/data/french.par.gz

# get installation script
wget https://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/data/install-tagger.sh

# install
sh install-tagger.sh

# append cmd and bin to PATH variable
export PATH=$PATH:$HOME/7.pos-tagging/TreeTagger/cmd
export PATH=$PATH:$HOME/7.pos-tagging/TreeTagger/bin

# test
echo 'A Lannister always pays his debts.' | tree-tagger-english
