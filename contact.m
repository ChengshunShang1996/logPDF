
num_list = [0.0008, 0.0016, 0.0024, 0.0032, 0.004, 0.0048];
for i = 1:6
    num = num_list(i);

    %%Set up the figure and data
    colordef(figure,'white');
    theta_vec = linspace(0,pi,18);
    phi_vec = linspace(0,2*pi,36);
    [theta,phi] = meshgrid(theta_vec,phi_vec);

    % H is your histogram data
    %H = 1+(cos(theta).*(sin(phi))); %Another example
    %H = 20*(cos(theta).* rand(size(phi)));
    % Load the H array from the text file
    file_name = ['number_of_contacts_in_all_directions_of_size_',num2str(num),'.txt'];
    H = load(file_name);
    Hmax = max(H(:));
    r = 0.05*Hmax; %Box size
    %polar(nan,max(max(H.*cos(phi))));
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
    %hs = surf(Hmax*Xs,Hmax*Ys,Hmax*Zs);
    %set(hs,'facecolor','none','edgecolor','blue','edgealpha',0.1)
    camlight;
    set(gca,{'xtick' 'ytick' 'ztick' 'vis' 'clim'},{[] [] [] 'on' [0 Hmax]});
    axis equal vis3d;
    box on;
    set(gca,'Visible','off')
    view([0 0 1]);
    %view(3);
    ax = gca;  % Get the current axes handle
    border_width = 0.01;  % Adjust this value to decrease border width
    ax.Position = [border_width, border_width, 1 - 2*border_width, 1 - 2*border_width];
    xlabel('X') 
    ylabel('Y') 
    zlabel('Z') 
    %colormap jet
    colorbar
    drawnow;

    pic_name = ['contact_',num2str(num),'.png'];
    saveas(gcf, pic_name)

end;