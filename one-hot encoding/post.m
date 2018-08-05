function m=post(test_file)

% 5 August 2018
% Amani Abdullah
% CNN-MGP: Convolutional neural networks for Metagenomic Gene Prediction, 2018

fileID = fopen(test_file);
C = textscan(fileID, '%f');
fclose(fileID);
x=length(C{1}); % number of rows in the file
%convert from cell to regular matrix
m=zeros(x,1);  
m(:,1)=C{1}; % frag number

end%function