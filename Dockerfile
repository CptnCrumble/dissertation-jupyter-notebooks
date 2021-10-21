# WIP - scikit learn doesn't load, think it needs a specific python version

FROM python
WORKDIR /usr/src/app
RUN pip install notebook
RUN pip install scikit-learn
COPY . .
CMD ["jupyter", "notebook"]