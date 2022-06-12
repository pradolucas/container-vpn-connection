FROM yoff/openfortivpn

EXPOSE 1111

COPY ./config /etc/openfortivpn/config
COPY ./docker-entrypoint.sh .
RUN chmod +x docker-entrypoint.sh
# COPY ./connect_oraculo.py .

# RUN cat etc/resolv.conf | egrep -o '([0-9.]{1,4}{3})'
# RUN ["cat", "etc/resolv.conf"]"$@"
# CMD [ "bash", "-c", "echo", "'nameserver 192.168.0.10'", ">>", "/etc/resolv.conf", "&&" ,"echo", "'nameserver 127.0.0.11'", ">>", "/etc/resolv.conf", "&&", "..."]
