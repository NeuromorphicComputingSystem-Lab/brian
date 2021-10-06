%% SPIKING NEURAL NETWORK FOR HANDWRITING RECOGNITION (MNIST)---UNSUPERVISED LEARNING APPROACH
%  coded by Abhronil Sengupta on 24th May, 2015

%% clear data
clc;
clear all;
close all;

%% pre-processing of input images for digits 0,1,2 and 3 with 250 training instances for each digit
num_train=100;  % no of training instances of each image % 각각의 이미지마다 트레이닝을 몇 번 할 것인가
load P_vs_I_20kT_PW.mat;% 파일 로드
load MNIST_Greyscale_0_9.mat; % load MNIST dataset% 파일 로드
num_digits=10;   % no of digits used for recognition% 인식에 사용된 자릿수

temp=diag(ones(1,num_digits));% 레이블링을 위한 임시행렬 % diag는 정사각형의 대각행렬을 만드는 것으로 temp는 1의 숫자를 하나씩 가진 10 * 10 행렬이 만들어진다.
y=[];           % label for each image% 정답 레이블을 담기 위한 것으로 추측

for i=0:num_train-1
    x(1+num_digits*i,:)=Zero(:,1+i);% 100개의 MNIST dataset안에 들어있는 Zero sample을 x의 각 1 + num_digits * i의 행에 집어 넣었다.
    x(2+num_digits*i,:)=One(:,1+i);
    x(3+num_digits*i,:)=Two(:,1+i);
    x(4+num_digits*i,:)=Three(:,1+i);
    x(5+num_digits*i,:)=Four(:,1+i);
    x(6+num_digits*i,:)=Five(:,1+i);
    x(7+num_digits*i,:)=Six(:,1+i);
    x(8+num_digits*i,:)=Seven(:,1+i);
    x(9+num_digits*i,:)=Eight(:,1+i);
    x(10+num_digits*i,:)=Nine(:,1+i);% Nine까지 위와 동일하며 총 1000개의 데이터 샘플을 가진 x행렬이 만들어짐
    
    y=[y;temp];% 정답 레이블
end;



%% images applied as input spike trains and synaptic weights modified by STDP

% Fixed parameters
timeStepS = 1;                          % 1 msec % 1000 msec == 1 sec이다.
epochs = num_train*num_digits;          % No of training epochs% 훈련 횟수 = 100 * 10
InNeurons = size(x,2);                  % No of input neurons% 인풋 뉴런 개수 = 784 % size(행렬, 차원)
num_PF=0;                                % 보류
% Tunable parameters

OpNeurons = 10;                         % No of output neurons
durationS = 290;                         % 40 msec simulation for each image% 신호를 받는 주기 
tau_EPSP = 50;                               % EPSP/STDP response time in msec


Inh = 500;                                % Inhibitory strength% 억제성 연접후 막전위 % 억제 힘 
K_leak = 0.018;                            % 고정된 상수
Kconst = 300;


Ki = .05e05;         %5000                     % scaling factor for probability% 확률에 대한 척도 계수
Kf = .05e09;         %50000000
del_K = 0.018;
tau_STDP1 = 4.5;
tau_STDP2 = 5;
tau_Inh = 50;
eta1 = 0.03;                              % Learning rate
eta2 = 0.01;




sum_weights = zeros(1,OpNeurons);          % matrix 1x10.   [0,0,0,0,0,0,0,0,0,0]
volt = zeros(OpNeurons);          % 10x10 zeros matrix
K = Ki*ones(1,OpNeurons);       % 1x10 ones matrix * Ki
weights_e = 0.13*rand(InNeurons,OpNeurons);  % synaptic weight matrix 784x10
weights_com = zeros(280,280);                % matrix 280x280
% Run the simulation for 1000 images (each digit 0-3 presented with 250   % 1000개 이미지에 대해 시뮬레이션을 실행한다(각 숫자 0-3은 250으로 표시됨).
% different instances for 10 times)
% Update and show image
for num=0: OpNeurons-1
    % weights_e를 784X1로 쪼개서 28X28로 reshape한 후 weights_com에 넣는다.
    weights_com(1:28, num*28+1:(num+1)*28) = reshape(weights_e(:, num+1), [28,28]);
    colormap(jet);% 제트 컬러맵을 가져온다.
    imagesc(weights_com) % 스케일링된 색으로 이미지를 표시한다.
    drawnow % for문을 다 돌고 난 후 그래프가 그려진다.
    pause(0.04);% 일시정지 기능을 한다.
end

for tt = 1:1
    tt  
for i = 1:epochs %replace by epochs% 1000회 for문 돌림
    fprintf('\n  epoch is : %d \n',i);
    
    % initial conditions
    spikesPerS = 255/4*x(i,:); % 1x784 matrix. *(255/4)
    spikes = zeros(InNeurons,durationS/timeStepS);% 784x290 matrix
    EPSP = zeros(InNeurons,durationS/timeStepS + tau_EPSP);% 784x340 matrix
    u = zeros(OpNeurons,durationS/timeStepS + tau_EPSP); % 10x340 matrix
    prob = zeros(OpNeurons,durationS/timeStepS + tau_EPSP); % 10x340 matrix
%     z = zeros(OpNeurons,durationS/timeStepS+tau_EPSP);
    I = zeros(1,OpNeurons);      % 1x10 matrix
    t_post = zeros(1,OpNeurons); % 1x10 matrix
    t_pre = zeros(1,InNeurons);  % 1x784 matrix

    
    % generate spikes for a particular input according to Poisson process
    for train = 1:InNeurons% 1-784 for loop
        % 스파이크 생성에 기준이 될 난수 생성
        vt = rand(1, durationS/timeStepS);% 1x290 matrix.
        if x(i, train) > 0 % if not 0
           % poisson process에 따라 x matrix의 (현재 epoch)번째 row추출
           % for stmt 돌면서 784개 col에서 요소 하나씩 뽑아서 스파이크 생성
           spikes(train, :) = ((spikesPerS(1,train)*timeStepS)/1000 > vt);
        end;
    end
    
    % generate EPSP corresponding to spike train
    for train = 1:InNeurons
        for t = 1:durationS/timeStepS
            if spikes(train,t) == 1 % when spike exists
                % 50ms만큼 EPSP에 채운다
                EPSP(train,t:t+tau_EPSP-1) = ones(1,tau_EPSP);
            end;
        end;
    end;
    
    %Run the simulation
    for t = 1:durationS/timeStepS+tau_EPSP-1
        
        for train = 1:InNeurons
            if t<= durationS/timeStepS
            if spikes(train, t) == 1 % spike
                t_pre(1, train) = t; % 해당 위치에 timing 저장
                for l = 1:OpNeurons
                    % weights update
                    weights_e(train, l) = weights_e(train, l) - eta2*weights_e(train, l)*exp((t_post(l)-t_pre(train))/tau_STDP2) ;
                    if weights_e(train,l)>1
                        weights_e(train,l)=1;% weight is over 1. then 1
                    elseif weights_e(train,l)<0
                        weights_e(train,l)=0;% weight is less 0. then 0
                    end;
                end;
            end;
            end;
        end;
        
        for j = 1:OpNeurons
            I(j) = 0;
            for kk = 1:OpNeurons
                if t - t_post(kk) < tau_Inh && kk ~= j && t_post(kk) ~= 0
                    I (j) = Inh;% 억제
                end;
            end;
       
            u(j, t+1) = weights_e(:, j)'*EPSP(:, t) - I(j); %current sum
            if u(j, t+1) < 0
                u(j, t+1) =0 ;
            end;
            
            % u / K
            i_curr(j, t+1) = u(j, t+1) / K(j);
            % i_curr square * 400 * 0.0000000005
            pwr_mtj(j, t+1) = i_curr(j, t+1) * i_curr(j, t+1) * 400*0.5e-09;
            
            % u / K > 0.00013
            if u(j, t+1) / K(j) > 1.3e-04
                prob(j, t+1) = 1;
            % u / K < 0.000003
            elseif u(j, t+1) / K(j) < 3e-05
                prob(j, t+1) = 0;
            else
                % interpolation. 해당 쿼리 점에서 보간된 값을 반환. pchip으로 보간
                % Ich는 샘플 점을 포함하며 P는 대응값을 포함한다.
                % u/K는 쿼리 점의 좌표를 포함한다.
                prob(j, t+1) = interp1(Ich, P, u(j,t+1)/K(j), 'pchip');
            end;
            
            if rand < prob(j,t+1) % 0-1 사이의 난수보다 클 경우
                num_PF = num_PF+1;
                z(j, t+1) = 1;
                t_post(j) = t+1;
                K(j) = K(j) + del_K*K(j);
                if K(j) > Kf% 500000000 보다 클 경우
                    K(j) = Kf; % 500000000
                end;
                
                for k = 1:InNeurons
                           %if EPSP(k) == 1
                             weights_e(k,j) = weights_e(k,j) + eta1*weights_e(k,j)*exp((t_pre(k)-t_post(j))/tau_STDP1);
                           %else
                                %weights_e(k,j) = weights_e(k,j) - eta2/10;
                           %end;
                    % 
                    if weights_e(k,j) > 1
                        weights_e(k,j) = 1;
                    elseif weights_e(k,j) < 0
                        weights_e(k,j) = 0;
                    end;
                end;
                
            end;
            
            K(j) = K(j) - K_leak;
            if K(j) < Ki
                K(j) = Ki;
            end;
        end;
        
        i_max(i,t+1) = max(i_curr(:,t+1));
        prob_MTJ(i,t+1) = max(prob(:,t+1));
    end;
    
    pwr_mtj_avg(i)=max(max(pwr_mtj));
    % Update and show image
    for num=0: OpNeurons-1
        weights_com(1:28,num*28+1:(num+1)*28)=reshape(weights_e(:,num+1),[28,28]);
        colormap(jet);
        imagesc(weights_com)
        drawnow
        pause(0.04);
    end

    %Calculate voltage and conductances
    
    
end;
end;  
% 
% %Plot current vs learning epoch
% i_max_avg = mean(i_max,2);
% prob_MTJ_avg = mean(prob_MTJ,2);
% i = 1:100;
% plot(i,i_max_avg(1:100));
% figure();
% plot(i,prob_MTJ_avg(1:100));
%     
% Inh = 500;                                % Inhibitory strength
% Kconst = .3e06;
% tau_Inh = 50;
% class = zeros(OpNeurons,num_digits);
% spikes = zeros(InNeurons,durationS/timeStepS,epochs);
% z = zeros(OpNeurons,durationS/timeStepS+tau_EPSP,epochs);
% prob = zeros(OpNeurons,durationS/timeStepS+tau_EPSP,epochs);
% 
% for num=1:OpNeurons
%    sum_weights(num)=sum(weights_e(:,num));
% end;
% 
% Gunity=0.1/max(sum_weights)/400;
% volt=1/(Kconst*Gunity)
% 
% 
% for i = 1:epochs %replace by epochs
% % initial conditions
%     spikesPerS=255/4*x(i,:);
%     spikes = zeros(InNeurons,durationS/timeStepS,i);
%     EPSP = zeros(InNeurons,durationS/timeStepS+tau_EPSP);
%     u = zeros(OpNeurons,durationS/timeStepS+tau_EPSP);
%     
%     z = zeros(OpNeurons,durationS/timeStepS+tau_EPSP);
%     I = zeros(1,OpNeurons);    
%     t_post = zeros(1,OpNeurons);
%     t_pre = zeros(1,InNeurons);
% 
%     
%     % generate spikes for a particular input according to Poisson process
%     for train = 1:InNeurons
%         vt = rand(1,durationS/timeStepS);
%         if x(i,train)>0
%            spikes(train, :,i) = ((spikesPerS(1,train)*timeStepS)/1000 > vt);
%         end;
%     end
%     
%     % generate EPSP corresponding to spike train
%     for train = 1:InNeurons
%         for t = 1:durationS/timeStepS
%             if spikes(train,t,i) == 1
%                 EPSP(train,t:t+tau_EPSP-1) = ones(1,tau_EPSP);
%             end;
%         end;
%     end;
%     
%     %Run the simulation
%     for t = 1:durationS/timeStepS+tau_EPSP-1
%         for train = 1:InNeurons
%             if t<= durationS/timeStepS
%             if spikes(train,t,i) == 1
%                 t_pre(1,train) = t;
%                
%             end;
%             end;
%         end;
%         for j = 1:OpNeurons
%             I(j) = 0;
%             for kk = 1:OpNeurons
%                 if t-t_post(kk) < tau_Inh && t_post(kk)~=0
%                     I (j) = Inh;
%                 end;
%             end;
%        
%             u(j,t+1) = weights_e(:,j)'*EPSP(:,t)-I(j);
%             if u(j,t+1)<0
%                 u(j,t+1)=0;
%             end;
%             if u(j,t+1)/Kconst>1.3e-04
%                 prob(j,t+1,i) = 1;
%             elseif u(j,t+1)/Kconst<3e-05
%                 prob(j,t+1,i) = 0;
%             else
%                 prob(j,t+1,i) = interp1(Ich,P,u(j,t+1)/Kconst,'pchip');
%             end;
%             if rand < prob(j,t+1,i)
% %                 z(j,t+1,i) = 1;
%                 t_post(j)=t+1;
%                
%                 
%             end;
%             
%         end;
%  
%     end;
%     [val,ind] = max(sum(z(:,:,i),2));
%     [vald,digit] = max(y(i,:)); 
%     class(ind,digit) = class(ind,digit) + 1;    
%     
%    
% end;
% 
% 
% max_class = 0;
% for i = 1:size(class,1)%num of rows of class
%     max_class = max_class + max(class(i,:));
% end;
% 
% accuracy = max_class/num_train/num_digits
% 
% 
% count_spikes=zeros(OpNeurons,100);
% for i=1:100
%     for j=1:9
%         for k=1:340
%             count_spikes(j,i)=count_spikes(j,i)+z(j,k,i);
%         end
%     end
% end
% 


