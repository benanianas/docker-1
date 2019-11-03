FROM ruby:2.6.4
RUN apt-get update && apt-get install -y build-essential nodejs sqlite3 git
ONBUILD RUN	git clone https://github.com/benanianas/rubyapp.git /opt/app
ONBUILD WORKDIR /opt/app
ONBUILD RUN bundle install
ONBUILD RUN rake db:migrate
ONBUILD RUN rake db:seed

#FROM ft-rails:on-build
#EXPOSE 3000
#CMD ["rails", "s", "-b", "0.0.0.0", "-p", "3000"]

#docker build -t ft-rails:on-build .
#docker build -t finalrubyapp .
#docker run -it -p 3000:3000 finalrubyapp
