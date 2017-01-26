%×÷Í¼
x = 0:1:50;
%-------------------------------------------------------
fid=fopen('NewGreedy Results.txt','r');
y_NewGreedy = fscanf(fid,'%d',[1,51]);
status=fclose(fid);
%-------------------------------------------------------
fid=fopen('Degree Results.txt','r');
y_DegreeGreedy = fscanf(fid,'%d',[1,51]);
status=fclose(fid);
%-------------------------------------------------------
fid=fopen('Betweenness Results.txt','r');
y_BetweennessGreedy = fscanf(fid,'%d',[1,51]);
status=fclose(fid);
%-------------------------------------------------------
fid=fopen('Closeness Results.txt','r');
y_ClosenessGreedy = fscanf(fid,'%d',[1,51]);
status=fclose(fid);
%-------------------------------------------------------
fid=fopen('Pagerank Results.txt','r');
y_PagerankGreedy = fscanf(fid,'%d',[1,51]);
status=fclose(fid);
%-------------------------------------------------------
fid=fopen('DegreeDiscount Results.txt','r');
y_DegreeDiscount = fscanf(fid,'%d',[1,51]);
status=fclose(fid);
%-------------------------------------------------------
fid=fopen('SingleDiscount Results.txt','r');
y_SingleDiscount = fscanf(fid,'%d',[1,51]);
status=fclose(fid);
%-------------------------------------------------------

plot(x,y_NewGreedy,'k-',x,y_DegreeGreedy,'b--',x,y_DegreeDiscount,'r--',x,y_BetweennessGreedy,'g-.',x,y_ClosenessGreedy,'m:x',x,y_PagerankGreedy,'k+:',x,y_SingleDiscount,'m-');
legend('NewGreedy','Degree','DegreeDiscount','Betweenness','Closeness','Pagerank','SingleDiscount')
xlabel('seed set size');
ylabel('Influence spread');