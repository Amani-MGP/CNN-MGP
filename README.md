# 
CNN-MGP: Convolutional neural networks for Metagenomic Gene Prediction, 2018


Datasets: 
datasets for training and testing are available in the Orphelia website http://orphelia.gobics.de/datasets.jsp

Main programs:

1. Open reading frame (ORF) extraction: We use Orphelia- a metagenomic ORF finding tool- to extract ORFs from each fragment http://orphelia.gobics.de/index.jsp. The output files are: orf.coords, orf.seq, frags.seq

2. one hot encoding: Execute  main program that will take orf.coord, orf.seq, frags.seq as input and produce   Test_orfSeqs.mat as output.  It calls two functions:
- read_orphelia_file.m that will pick the leftmost ORFs from each ORF-set.
- test_one_hot_encoding.m that perform one-hot encoding for ORFs.


    
3. Testing:
Execute test_CNN.py, that will take Test_orfSeqs.mat as input and will produce test_output.txt file as output.

4. Output:
Execute combine_results() that will take  test_output.txt file as input and will produce the final prediction in output_file.txt file
