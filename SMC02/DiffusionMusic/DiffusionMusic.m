%generate music with diffusion model
function diffMIDI()
voices=10;
MATRIX=[];

for i=1:voices
    numSteps=round(posnormrnd(50,100,1,1));  %length of the piece
    v=normrnd(0.0,1,1,1); %drift rate
    %v=1-exprnd(0.1);
    z=posnormrnd(60,10,1,1); %starting tone, 60=middle C
    time=posnormrnd(0.1,0.5,1,1); %speed;
    startTime=unifrnd(0,60,1,1); %startTime=time;
    
    timeSeries=DDM('numStep',numSteps,...
        'z',z,...
        'v', v,...
        'c',2,...
        'tau',1);
    % Filtering out negative values
     timeSeries(timeSeries<=0)=0;
  
    display(['NumStep: ' num2str(numSteps) ' time:' num2str(time)]);
    N=length(timeSeries);
    timing=startTime:time:startTime+(N*time);
    timing=timing(1:end-1); 
    M=zeros(N,6);
    M(:,1) = i;         %track 1
    M(:,2) = 1;         %channel 1
    M(:,3) = round(timeSeries);      % note numbers - middleC = 60
    M(:,4) = 280; %round(linspace(80,130,N))'; %volume? Velocity?
    M(:,5) = timing';  % timing of the note, in seconds
    M(:,6) = M(:,5) + time*1.2;   % duration, in seconds
    MATRIX=[MATRIX; M];
end

midi_new = matrix2midi(MATRIX);
writemidi(midi_new, 'testout.mid');

[y,Fs] = midi2audio(midi_new);

%audiowrite('out.wav',y, Fs);

%% compute piano-roll:
Notes=midiInfo(midi_new);
piano_roll(Notes);
[PR,t,nn] = piano_roll(Notes,1);

%% display piano-roll:
figure;
imagesc(t,nn,PR);
axis xy;
xlabel('time (sec)');
ylabel('note number');

soundsc(y,Fs);
%soundsc(y,Fs);

function [a]=posnormrnd(mu,sig,m,n)
a=normrnd(mu,sig,m,n);
while any(a<0)
    a=normrnd(mu,sig,m,n);
end
