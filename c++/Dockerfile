FROM gcc:latest
COPY . /cpptest
WORKDIR /cpptest
RUN g++ main.cpp -o Test
CMD [ "./Test" ]
