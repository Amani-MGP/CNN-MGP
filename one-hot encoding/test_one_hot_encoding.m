function test_one_hot_encoding()


% 5 August 2018
% Amani Abdullah
% CNN-MGP: Convolutional neural networks for Metagenomic Gene Prediction, 2018


load('left_orfSeqs.mat')

k=length(orfSeqs);

x=zeros(705,4,k);

for i=1:k   
    seq=orfSeqs{i};
    seq=char(seq);
x(:,:,i)=one_hot_encoding(seq);

end %for



save('Test_orfSeqs.mat','x','-v7.3' )
save('gc.mat','gc','-v7.3')










end % function