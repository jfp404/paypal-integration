FROM python:3

COPY ./server /app

# we require requests version v0.11.0 or higher
    # RUN wget pypi.python.org/packages/source/r/requests/requests-2.2.1.tar.gz && \
    #     tar zxf requests-2.2.1.tar.gz && \
    #     cd requests-2.2.1 && \
    #     python setup.py install

    # RUN wget https://files.pythonhosted.org/packages/9a/5e/56ad487db7ea4ead74b5d67c2c0524c341d77db5d0fbf582e70bdde3ac9d/braintree-4.0.0.tar.gz && \
    #     tar zxf braintree-4.0.0.tar.gz && \
    #     cd braintree-4.0.0 && \
    #     python setup.py install

RUN pip install Flask


RUN pip install braintree

WORKDIR /app
ENTRYPOINT [ "python" ]
CMD [ "simpleServer.py" ]