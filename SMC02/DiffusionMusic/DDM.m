%SIMULATION OF THE DIFFUSION PROCESS -  VARIABILITY ACROSS TRIALS, plus
%other types of variability (variability of nondecision time, variability
%of starting point)
%this model will work with one or two barriers. If you want one barrier,
%just put b=-inf;
%-----------------
%THIS IS A GENERAL PURPOSEFULLY MODEL. It can be used with different kind
%of diffusion process (one/two boundaries, variability across trials,
%other kind of variabilitis).
%It is used for generating data. No plot showed during the process. If
%plotF=1, the plot of the distributions are still showed.

%DDMgaussOpt2 WILL *NOT* SHOW ANY FIGURE OF THE PROCESS.It will still show the other figures.

function [timeSeries]=diffProcess(varargin)
p=inputParser;
addParamValue(p, 'numStep', 30000);
addParamValue(p, 'z', 0); %starting point, if [] will be a/2
addParamValue(p, 'v', 0.3); %drift rate within trial
addParamValue(p, 'c', 0.1); %put [] is you want it to calculate for you
addParamValue(p, 'tau', 0.0001);
%notice that s
addParamValue(p, 'maxWalk', 2500); addParamValue(p, 'plotF', 1);
parse(p,varargin{:}); numStep=p.Results.numStep; z=p.Results.z;
%s=p.Results.s;
v=p.Results.v;  tau=p.Results.tau; c=p.Results.c;

if isempty(z)
    z=a/2;
end

timeseries(1:numStep,1)=NaN;
startPoint=z;
timeSeries=cumsum([startPoint; normrnd(v*tau,c*sqrt(tau),numStep,1)]);
end
