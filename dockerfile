
FROM 19110418/doan:3
    COPY . /doan
    WORKDIR /doan
    ENV DISPLAY=host.docker.internal:0.0   
    CMD python3 program.py

    
