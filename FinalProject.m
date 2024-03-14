%initialization of servos
trigger = 45; %80 for firing
tilt = 90; %even horizontal
%resolution = 680x480 camera
% given face position (x,y)
xface = 135;
yface = 240;
xcent = 680/2;
ycent = 480/2;
center = [680/2 480/2];
% xplane = linspace(-340,340,681);
% yplane = linspace(-240,240,481);
%tan(theta) = x/l -> theta = taninv(x/l)
%tan(phi) = y/l -> phi = taninv(y/l)
% l = linspace(0.1, 100,1000);
% theta = atand(x./l);
% phi = atand(y./l);
% plot(l,theta)
% hold on;
% plot(l,phi);
currenttilt = 90;
while(xalign == false)
    %xface =  get updated x position of face
    if(xface-10 < xcent <= xface+10) %within resonable distance from center
        %target is aligned
        xalign = true;
    elseif(xface < xcent) %NOTE: tilt servo has 0 as straight up and 180 as down
        %current tilt = curent tilt - 1
        %tilt servo(current angle)

    elseif(xface > xcent)
        %current tilt = curent tilt + 1
        %tilt servo(current angle)
    end
end

while(yalign == false)
    %yface =  get updated y position of face
    if(yface-3 < ycent <= yface+3)
        %target is aligned
        yalign = true;
    elseif(yface < ycent)
        %stepper reverse
        %stepper one step
    elseif(yface > ycent)
        %stepper forward
        %stepper onestep
    end
end
