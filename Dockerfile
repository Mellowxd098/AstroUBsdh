RUN git clone https://github.com/Mellowxd098/AstroUBsdh.git /root/Mellowxd098/
WORKDIR /root/Mellowxd098/
#stuff same as Ultroid 
COPY requirements.txt /deploy/
RUN pip3 install --no-cache-dir -r /deploy/requirements.txt
