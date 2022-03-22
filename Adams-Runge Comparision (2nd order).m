x0=50;
y0=50;
width=1200;
height=900;
set(gcf,'position',[x0,y0,width,height]);


h = 0.001;
t = 0:h:1;


phi = exp(1)-1+0.01;
y0 = phi;
yexact = ((-1 + phi^2)*exp(sin(2*pi*t))+1).^0.5;
ystarR = zeros(size(t));
ystarR(1) = yexact(1);

ystarA = zeros(size(t));

ystarA(1) = yexact(1);
for i=1:(length(t)-1)
    y1 = (ystarA(i) - 1/ystarA(i)) * pi * cos(2*pi*t(i));
    y2 = 0;
    if i>1
        y2 = (ystarA(i-1) - 1/ystarA(i-1)) * pi * cos(2*pi*t(i-1));
    end
    ystarA(i+1) = ystarA(i) + h*(3*y1 - y2)/2;
end
for i=1:(length(t)-1)
    k1 = h*(ystarR(i) - 1/ystarR(i)) * pi * cos(2*pi*t(i));
    k2 = h*(ystarR(i)+k1/2 - 1/ystarR(i)+k1/2) * pi * cos(2*pi*(t(i)+h/2));
    ystarR(i+1) = ystarR(i) + k2;
end

tiledlayout(3,3)
nexttile;
plot(t,yexact);
legend('Exact');
nexttile;
plot(t,ystarA);
legend('Adams');
nexttile;
plot(t,ystarR);
legend('Runge');
nexttile([2 3]);
plot(t,yexact,t,ystarA,t,ystarR);
legend('Exact','Adams','Runge');