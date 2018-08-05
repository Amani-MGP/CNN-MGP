function main(orf_coord,orf_seq,frag_seq)
% 5 August 2018
% Amani Abdullah
% CNN-MGP: Convolutional neural networks for Metagenomic Gene Prediction, 2018

% The main program will take orf_coord, orf_seq, frag_seq as input and produce Test_orfSeqs.csv as output. 
% It calls two functions:


% 1. read_orphelia_file.m that will pick the leftmost ORFs from each ORF-set.
read_orphelia_file(orf_coord,orf_seq,frag_seq);

% 2. test_one_hot_encoding.m that will perform one_hot_encoding for testinf data.
test_one_hot_encoding()


end%function