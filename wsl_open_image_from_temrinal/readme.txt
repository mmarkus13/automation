[Usage]
	"iop" is the command which calls the open_imgage.py script.
	within terminal you should cd to the directory where the picture is located


[Usecase]
	-For text there is 'cat'; for images to check content you can use 'iop' command with this
	-Useful mainly when there are a lof of huge files (and/or dealing with slow computer) and you don't want to use explorer.exe's search box; than this is slightly faster.
	-If you have txt and image filies within the same folder and would like to quicky find an information:
		grep -10 "searchterm" <textfile>.txt  # to find relevant info (optional)
		iop <image>  # note: that you have to paste the whole filename --including the extension (.jpg or .png or ...)
	#it is assumed that the pictures are named properly so you know what you are looking for.
		example.:	[bad]	Screenshot1234 is obviously better to be checked via GUI...
				[good]	Homeostatsis.png


[Prerequisites]
	requires WSL and xming

	[windows10]
	install xming & start (with defailt 0 port)

	[WSL]
	sudo apt install x11-apps
		[optional]
		sudo apt install x11-apps		# not needed for localhost
		touch /home/$USER/.Xauthority	# not needed for localhost

	export DISPLAY=localhost:0.0


[Installation] (within WSL)
	mkdir -p /home/$USER/scripts
	mv iop open_imgage.py /home/$USER/scripts
	chmod 750 -R /home/$USER/scripts/
	echo 'export PATH=$PATH:/home/'"$USER/scripts" >> /home/$USER/.bashrc
	
