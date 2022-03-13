x0=50;
y0=50;
width=1200;
height=900;
set(gcf,'position',[x0,y0,width,height]);


h = 0.001;
t = 0:h:1;
a1 = 1/2;
a2 = 1/2;

phi = exp(1)-1+0.01;
y0 = phi;
yexact = ((-1 + phi^2)*exp(sin(2*pi*t))+1).^0.5;

ystar = zeros(size(t));
ystar(1) = y0;

for i=1:(length(t)-1)
    k1 = (ystar(i) - 1/ystar(i)) * pi * cos(2*pi*t(i));

    k2 = ((ystar(i) + k1*h) - 1/(ystar(i) + k1*h)) * pi * cos(2*pi*(t(i) + h));
    
    ystar(i+1) = ystar(i) + h*(a1*k1 + a2*k2);
end
tiledlayout(2,2)
nexttile;
plot(t,yexact);
legend('Exact');
nexttile;
plot(t,ystar);
legend('Approximate');
nexttile([1 2]);
plot(t,yexact,t,ystar);
legend('Exact','Approximate');