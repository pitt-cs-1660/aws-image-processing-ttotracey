FROM public.ecr.aws/lambda/python:3.13

# install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

############
#
# TODO: implement the rest of the image
#
############
WORKDIR /app

#copy pyproject.toml, 
COPY pyproject.toml

#run uv sync, 
RUN uv sync

#copy handler.py, 
COPY handler.py

#set PYTHONPATH, 
ENV PYTHONPATH=/app

#set CMD
CMD["python", "handler.py"]