%%Set up the figure and data
colordef(figure,'black');

theta_vec = linspace(0,pi,18);
phi_vec = linspace(0,2*pi,36);

[theta,phi] = meshgrid(theta_vec,phi_vec);

% H is your histogram data
%H = 1+(theta.*(sin(phi))); %Another example
H = 100*(rand(size(phi)));

Hmax = max(H(:));

r = 0.03*Hmax; %Box size

polar(nan,max(max(H.*cos(phi))));
hold all;
%%Make the Histogram
for kk = 1:numel(theta_vec);
    for jj = 1:numel(phi_vec);
        X=r*([0 1 1 0 0 0;1 1 0 0 1 1;1 1 0 0 1 1;0 1 1 0 0 0]-0.5);
        Y=r*([0 0 1 1 0 0;0 1 1 0 0 0;0 1 1 0 1 1;0 0 1 1 1 1]-0.5);
        Z=[0 0 0 0 0 1;0 0 0 0 0 1;1 1 1 1 0 1;1 1 1 1 0 1]*H(jj,kk);
        h= patch(X,Y,Z,0*X+H(jj,kk),'edgecolor','none');

          rotate(h,[0 0 1],45,[0 0 0]);
          rotate(h,[0 1 0],90 - 180/pi*phi_vec(jj),[0 0 0]);
          rotate(h,[0 0 1],180/pi*theta_vec(kk),[0 0 0]);

      end;
  end;

%%Adjust the plot
[Xs,Ys,Zs] = sphere(size(theta,2)+1);
hs = surf(Hmax*Xs,Hmax*Ys,Hmax*Zs);
set(hs,'facecolor','none','edgecolor','w','edgealpha',0.2)

camlight;
set(gca,{'xtick' 'ytick' 'ztick' 'vis' 'clim'},{[] [] [] 'on' [0 Hmax]});
axis equal vis3d;
box on;
view(3);
colorbar
drawnow;