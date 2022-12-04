# Used for building the scripts
FROM ubuntu:20.04

RUN apt-get update && apt-get -y install python3 python3-pip
RUN pip install PyPDF2 fpdf