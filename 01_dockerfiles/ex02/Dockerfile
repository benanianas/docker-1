#FROM ruby:2.6.4
#RUN apt-get update && apt-get install -y build-essential nodejs sqlite3 git
#RUN	git clone https://github.com/chzabakh/ruby_app.git /opt/app
#WORKDIR /opt/app
#RUN bundle install
#RUN rake db:migrate
#RUN rake db:seed

FROM ft-rails:on-build
EXPOSE 3000
CMD ["rails", "s", "-b", "0.0.0.0", "-p", "3000"]

#docker build -t ft-rails:on-build .
#docker build -t finalrubyapp .
