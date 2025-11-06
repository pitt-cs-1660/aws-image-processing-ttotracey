FROM public.ecr.aws/lambda/python:3.13

# install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

############
#
# TODO: implement the rest of the image
#
############

WORKDIR ${LAMBDA_TASK_ROOT}
# #set PYTHONPATH, 
# ENV PYTHONPATH=/app

COPY pyproject.toml ${LAMBDA_TASK_ROOT}/
# install deps
RUN uv sync
# copy function code
COPY handler.py ${LAMBDA_TASK_ROOT}/
# sync the project
RUN uv sync --locked --no-install-project --no-editable

#set CMD
CMD ["handler.resize_handler"]