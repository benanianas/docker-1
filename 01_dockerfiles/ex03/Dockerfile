FROM ubuntu
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get -y update && apt-get -y upgrade && apt-get install -y postfix wget openssh-server ca-certificates tzdata
RUN wget https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.deb.sh
RUN bash script.deb.sh
RUN apt-get install gitlab-ce -y
RUN mkdir /etc/gitlab/ssl && chmod 700 /etc/gitlab/ssl && openssl req -x509 -days 365 -newkey rsa:4096 -nodes -keyout "/etc/gitlab/ssl/privateKey.key" -out "/etc/gitlab/ssl/certificate.crt" -subj "/C=MA/"
RUN sed -i -e "s/external_url 'http:\/\/gitlab.example.com'/external_url 'https:\/\/10.12.6.15\/'/g" /etc/gitlab/gitlab.rb
RUN echo "nginx['redirect_http_to_https'] = true" >> /etc/gitlab/gitlab.rb
RUN echo "nginx['ssl_certificate'] = \"/etc/gitlab/ssl/certificate.crt\"" >> /etc/gitlab/gitlab.rb
RUN echo "nginx['ssl_certificate_key'] = \"/etc/gitlab/ssl/privateKey.key\"" >> /etc/gitlab/gitlab.rb
RUN echo "gitlab_rails['gitlab_shell_ssh_port'] = 6922" >> /etc/gitlab/gitlab.rb
RUN echo "Port 6922" >> /etc/ssh/ssh_config
RUN echo "Port 6922" >> /etc/ssh/sshd_config
ENTRYPOINT service ssh restart && (/opt/gitlab/embedded/bin/runsvdir-start &) && gitlab-ctl reconfigure && gitlab-ctl tail

#docker build -t mylab .
#docker run -it -p 443:443 -p 80:80 -p 6922:6922 --rm mylab
