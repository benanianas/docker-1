FROM debian

RUN apt-get update &&\
	apt-get install -y wget &&\
	apt-get install -y tar bzip2 &&\
	wget https://files.teamspeak-services.com/releases/server/3.9.1/teamspeak3-server_linux_amd64-3.9.1.tar.bz2 &&\
	tar -xf  teamspeak3-server_linux_amd64-3.9.1.tar.bz2
WORKDIR teamspeak3-server_linux_amd64
CMD		./ts3server_minimal_runscript.sh
