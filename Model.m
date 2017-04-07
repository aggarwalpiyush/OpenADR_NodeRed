clear all;
%% suppose SOC to be increased from 0 to 100
%% declaration/ initialization of parameters
c_start=clock;
i_max=30
SOC_now=40; % initial SOC
cost=0;		% variable initialization
duration=0;	% variable initialization
net_cost=0;	% variable initialization
Q_max=60000;	% Capacity of batter in KWh

%% code for user input
prompt='What is desired SOC?';
SOC_final= input(prompt);
prompt='When will you unplug the vehicle (for Today enter 1),(for Tomorrow enter 2)?';
day_unplug=input(prompt);
prompt='When will you unplug the vehicle (ex. enter 17 if want to unplug at 17:35)?';
t_unplug=input(prompt);
if (day_unplug==1)
    if (c_start(4)>t_unplug)
        prompt='Unplug time can not be before plug time. Please enter unplug time again (0-23) hr of day';
        t_unplug=input(prompt);
    end
end

%% While loop for main simulation

while SOC_now<SOC_final
c = clock;
    t_now=c(4);
    delta_soc=SOC_final-SOC_now;
fileID = fopen('C:\Users\Piyush\c_rate.txt');    % Reading of file for suggested charging rate from algorithm
C = textscan(fileID,'%s');	%Reading of data from file
fclose(fileID)	% Close file
i_calc=str2num(cell2mat(C{1}))    	% storing of read data into a variable

fileID1 = fopen('C:\Users\Piyush\current_price.txt');
C1 = textscan(fileID1,'%s');
fclose(fileID1)
price_now=cell2mat(C1{1});    
price_now=str2num(price_now(3:5)); % Current Price in Cents/Kwh
t_left=t_unplug-t_now;  	% Duration in hours (available) left for charging

t_calc=(delta_soc*Q_max)/(240*100*i_calc)		% Required number of hours to reach desired SOC if charging rate remains constant at i_calc

if (t_left>t_calc)
    c_rate=i_calc;
else c_rate=i_max;
end

    
pause(60);
%calculation of new SOC after every minute
SOC_now=SOC_now + (100-(((Q_max/240) -(c_rate*1/60))/(Q_max/240))*100) % considering charge time of 1 min per loop
cost=price_now*240*c_rate*60/3600;
net_cost=net_cost+cost
duration=duration+60   %seconds
end
