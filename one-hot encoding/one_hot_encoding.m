function hot_array=one_hot_encoding(seq) 

% 5 August 2018
% Amani Abdullah
% CNN-MGP: Convolutional neural networks for Metagenomic Gene Prediction, 2018



hot_array = zeros(705,4);

for i=1:length(seq)
if seq(i)== 'A'
    
    hot_array(i,:)= [1 0 0 0];
elseif seq(i)=='T'
    
   hot_array(i,:)= [0 0 0 1];
    
    elseif seq(i)=='C'
    
   hot_array(i,:)= [0 1 0 0];
    
     elseif seq(i)=='G'
    
   hot_array(i,:)= [0 0 1 0];
end%if


end%for 
    
end % function